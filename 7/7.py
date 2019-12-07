from ship import ShipComputer
from itertools import permutations


def str_vec_to_int_vec(str_vec):
    input_vector = []

    for string in str_vec:
        input_vector.append(int(string))

    return input_vector


def read_input(input_path):
    file = open(input_path, "r+")
    lines = file.readline()
    file.close()

    strings = lines.split(',')
    return str_vec_to_int_vec(strings)


def get_thrusters_signal(phase_setting):
    program = read_input('input1')
    computer = ShipComputer()

    for phase in phase_setting:
        program_input = [phase, computer.output]
        computer.input = program_input
        computer.set_program(program)
        computer.run_program()

    return computer.output


def get_solution_to_problem_1():
    phase_settings = [str_vec_to_int_vec(list(''.join(p))) for p in permutations('01234')]
    highest_thrusters_signal = 0

    for phase_setting in phase_settings:
        thrusters_signal = get_thrusters_signal(phase_setting)
        if highest_thrusters_signal < thrusters_signal:
            highest_thrusters_signal = thrusters_signal

    print(f'Highest thrusters signal is {highest_thrusters_signal}.')


get_solution_to_problem_1()

