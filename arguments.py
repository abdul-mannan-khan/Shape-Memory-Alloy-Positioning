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
    group.add('--initial_deflection', required=False, default=0, type=float, help='Initial condition of deflection (default 0)')
    group.add('--initial_force', required=False, default=0, type=float, help='Initial force in newton (default 0)')
    group.add('--initial_martensitic_fraction_of_detwinned_martensite', required=False, default=1, type=float, help='Initial martensitic fraction of detwinned martensite (default 1)')
    group.add('--initial_position', required=False, default=0.12, type=float, help='initial position in meter (default 0.12)')
    group.add('--initial_temperature', required=False, default=20, type=float, help='initial temperature in celcius (default 20)')
    group.add('--number_of_coils', required=False, default=55, type=int, help='number of coils (default 55)')
    group.add('--spring_diameter', required=False, default=0.0025, type=float, help='diameter of spring in meter (default 0.0025)')
    group.add('--wire_diameter', required=False, default=0.0005, type=float, help='diameter of wire in meter (default 0.0005)')
    group.add('--twinned_martensite_shear_modulus', required=False, default=5 * 10 ** 10, type=float, help='Twinned Martensite Shear Modulus (default 5*10^10)')
    group.add('--austenite_shear_modulus', required=False, default=10 ** 11, type=float, help='Austenite Shear Modulus (default 10^11)')
    group.add('--austenitic_start_temperature', required=False, default=59, type=float, help='Austenitic Start Temperature in celcius (default 59)')
    group.add('--austenitic_finish_temperature', required=False, default=71, type=float, help='Austenitic Finish Temperature in celcius (default 71)')
    group.add('--austenitic_constant', required=False, default=100000000, type=float, help='Austenitic Constant (default 100000000)')
    group.add('--martensitic_start_temperature', required=False, default=55, type=float, help='Martensitic Start Temperature in celcius (default 55)')
    group.add('--martensitic_finish_temperature', required=False, default=43, type=float, help='Martensitic Finish Temperature in celcius (default 43)')
    group.add('--martensitic_constant', required=False, default=40000000, type=float, help='Martensitic Constant (default 40000000)')
    group.add('--max_recoverable_deflection', required=False, default=0.001, type=float, help='Maximum recoverable deflection (default 0.001)')
    group.add('--critical_detwinning_starting_stress', required=False, default=0.5 * 10 ** 9, type=float, help='Critical detwinning Starting stress (default 0.5*10^9)')
    group.add('--critical_detwinning_finishing_stress', required=False, default=1.02 * 10 ** 9, type=float, help='Critical detwinning Finishing stress (default 1.02*10^9)')
    group.add('--delta_max', required=False, default=60 / 55, type=float, help='maximum deflection that can take place in a safe range (default 60/55)')
    group.add('--shear_stress', required=False, default=1.6 * 10 ** 9, type=float, help='shear stress (default 1.6*10^9)')
    group.add('--force_applied', required=False, default=4, type=float, help='force applied in newton (default 4)')
    group.add('--sigma_o', required=False, default=1, type=float, help='sigma_o (default 1)')
