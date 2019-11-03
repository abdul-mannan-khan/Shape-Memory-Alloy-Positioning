def add_soft_actor_critic_arguments(parser):
    group = parser.add_argument_group('soft actor-critic arguments')
    group.add('--iterations', required=False, default=100000, type=int, help='number of iterations (default 100,000)')
    group.add('--environment_steps', required=False, default=100, type=int, help='number of environment steps to train for (default 100)')
    group.add('--gradient_steps', required=False, default=10, type=int, help='number of gradient steps to train for (default 10)')
    group.add('--temperature', required=False, default=0.1, type=float, help='weight multiplied to entropy in objective (alpha in SAC paper, default 0.1)')
    group.add('--learning_rate_value', required=False, default=0.001, type=float, help='learning rate for value function approximator (default 0.001)')
    group.add('--learning_rate_q', required=False, default=0.001, type=float, help='learning rate for Q-function approximator (default 0.001)')
    group.add('--learning_rate_policy', required=False, default=0.001, type=float, help='learning rate for policy function (default 0.001)')
    group.add('--exponential_weight', required=False, default=0.9, type=float, help='weight in exponential moving average of value weights (0 < tau <= 1, default 0.9)')
    group.add('--discount_factor', required=False, default=0.99, type=float, help='discount factor (0 < gamma <= 1, default 0.99)')

def add_simulated_environment_arguments(parser):
    group = parser.add_argument_group('simulated environment arguments')
    group.add('--number_of_coils', required=False, default=10, type=int, help='number of coils (default 10)')
    group.add('--initial_temperature', required=False, default=293.15, type=float, help='initial temperature in kelvin (default 293.15)')
    group.add('--wire_diameter', required=False, default=0.005, type=float, help='diameter of wire in meter (default 0.005)')
    group.add('--twinned_martensite_shear_modulus', required=False, default=1, type=float, help='Twinned Martensite Shear Modulus (default 1)')
    group.add('--austenite_shear_modulus', required=False, default=1, type=float, help='Austenite Shear Modulus (default 1)')
    group.add('--martensitic_start_temperature', required=False, default=1, type=float, help='Martensitic Start Temperature (default 1)')
    group.add('--martensitic_finish_temperature', required=False, default=2, type=float, help='Martensitic Finish Temperature (default 2)')
    group.add('--martensitic_constant', required=False, default=1, type=float, help='Martensitic Constant (default 1)')
    group.add('--austenitic_start_temperature', required=False, default=1, type=float, help='Austenitic Start Temperature (default 1)')
    group.add('--austenitic_finish_temperature', required=False, default=2, type=float, help='Austenitic Finish Temperature (default 2)')
    group.add('--austenitic_constant', required=False, default=1, type=float, help='Austenitic Constant (default 1)')
    group.add('--max_recoverable_deflection', required=False, default=1, type=float, help='Maximum recoverable deflection (default 1)')
    group.add('--initial_deflection_condition', required=False, default=1, type=float, help='Initial condition of deflection (default 1)')
    group.add('--initial_force', required=False, default=1, type=float, help='Initial force (default 1)')
    group.add('--critical_detwinning_starting_stress', required=False, default=1, type=float, help='Critical detwinning Starting stress (default 1)')
    group.add('--critical_detwinning_finishing_stress', required=False, default=2, type=float, help='Critical detwinning Finishing stress (default 2)')
    group.add('--shear_transformation_coefficient', required=False, default=1, type=float, help='Shear transformation coefficient (default 1)')
    group.add('--initial_martensitic_fraction_of_twinned_martensite', required=False, default=1, type=float, help='Initial martensitic fraction of twinned martensite (default 1)')
    group.add('--initial_martensitic_fraction_of_detwinned_martensite', required=False, default=1, type=float, help='Initial martensitic fraction of detwinned martensite (default 1)')
    group.add('--initial_spring_diameter', required=False, default=0.1, type=float, help='initial spring diameter in meter (default 0.1)')
    group.add('--final_spring_diameter', required=False, default=0.2, type=float, help='final spring diameter in meter (default 0.2)')
    group.add('--intermediate_spring_diameter', required=False, default=0.15, type=float, help='intermediate spring diameter in meter (default 0.2) (default 0.15)')
    group.add('--initial_pitch_angle', required=False, default=0, type=float, help='initial pitch angle in radians (default 0)')
    group.add('--final_pitch_angle', required=False, default=0, type=float, help='final pitch angle in radians (default 0)')
    group.add('--intermediate_pitch_angle', required=False, default=0, type=float, help='final pitch angle in radians (default 0)')
