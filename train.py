from app.config import Config
from app.environments import get_environment
from app.model import Model
from app.policies import get_policy
from app.replay_buffer import ReplayBuffer
from app.rollout import rollouts
from torch.utils.tensorboard import SummaryWriter
import argparse
import torch
import sys
import yaml
import yamale

CONFIG_SCHEMA_PATH = 'app/config/schema.yaml'


def main():
    arguments = sys.argv[1:]
    options = parse_arguments(arguments)
    config = load_config(options.config)
    environment = get_environment(config.environment_type, config.environment)
    policy = get_policy(config.policy_type, config.policy, environment)
    replay_buffer = ReplayBuffer(config.batch_size, config.max_buffer_size,
                                 environment.observation_size,
                                 environment.action_size)
    model = Model(config.model, environment, policy)
    writer = SummaryWriter(log_dir='runs/' + options.name)
    train(model, replay_buffer, environment, config, writer)

    # save trained model
    if config.save_model is not None:
        model.save(options.save_model)


def parse_arguments(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str, help='path to config file')
    parser.add_argument(
        '-name',
        type=str,
        default='baseline',
        help='name of experiment, it is used for tensorboard logging')
    options = parser.parse_args(arguments)
    return options


def load_config(config_path):
    schema = yamale.make_schema(CONFIG_SCHEMA_PATH)
    data = yamale.make_data(config_path)
    yamale.validate(schema, data, strict=True)
    config = Config(**data[0][0])
    return config


def train(model, replay_buffer, environment, config, writer):
    """
    Trains the model according to the configuration and environment.

    :type model: app.model.Model
    :type replay_buffer: app.replay_buffer.ReplayBuffer
    :type environment: app.environments.environment.Environment
    :type config: app.config.Config
    :type writer: torch.utils.tensorboard.SummaryWriter
    """
    model.train_mode()
    for iteration in range(config.iterations):
        # explore environment
        trajectories = rollouts(
            environment,
            model.policy,
            config.environment_steps,
            max_trajectory_length=config.max_trajectory_length)
        replay_buffer.add_trajectories(trajectories)

        # statistics to log to tensorboard
        policy_loss_sum = 0
        q1_loss_sum = 0
        q2_loss_sum = 0
        alpha_loss_sum = 0
        reward_sum = 0
        observation_count = 0
        for trajectory in trajectories:
            reward_sum += trajectory.rewards.sum()
            observation_count += len(trajectory.rewards)
        reward_average = reward_sum / observation_count

        # train model
        for gradient_step in range(config.gradient_steps):
            batch_numpy = replay_buffer.random_batch()
            policy_loss, q1_loss, q2_loss, alpha_loss = model.train_batch(
                observations=torch.from_numpy(
                    batch_numpy.observations).float(),
                next_observations=torch.from_numpy(
                    batch_numpy.next_observations).float(),
                actions=torch.from_numpy(batch_numpy.actions).float(),
                rewards=torch.from_numpy(batch_numpy.rewards).float(),
                terminals=torch.from_numpy(batch_numpy.terminals).float())
            policy_loss_sum += policy_loss
            q1_loss_sum += q1_loss
            q2_loss_sum += q2_loss
            alpha_loss_sum += alpha_loss
            
        # write to tensorboard
        policy_loss_average = policy_loss_sum / config.gradient_steps
        q1_loss_average = q1_loss_sum / config.gradient_steps
        q2_loss_average = q2_loss_sum / config.gradient_steps
        alpha_loss_average = alpha_loss_sum / config.gradient_steps
        writer.add_scalar('loss/policy', policy_loss_average, iteration)
        writer.add_scalar('loss/q1', q1_loss_average, iteration)
        writer.add_scalar('loss/q2', q2_loss_average, iteration)
        writer.add_scalar('loss/alpha', alpha_loss_average, iteration)
        writer.add_scalar('reward', reward_average, iteration)

        print(f'Iteration: {iteration} / {config.iterations}')


if __name__ == '__main__':
    main()
