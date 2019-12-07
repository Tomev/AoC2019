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


apcs = []  # Amplifiers Controllers Software for each amplifier
names = ['CUP A', 'CUP B', 'CUP C', 'CUP D', 'CUP E']


def outside_input():
    print('Outside input')
    return 0


for name in names:
    apcs.append(ShipComputer())
    apcs[-1].name = name


def get_thrusters_signal(phase_setting, program):
    computer = ShipComputer()
    next_input = 0
    for phase in phase_setting:
        computer.input = [phase, next_input]
        computer.set_program(program.copy())
        computer.run_program()
        next_input = computer.output
        computer.reset()

    return next_input


def get_thrusters_loopback_signal(phase_setting, program):

    for i in range(5):
        apcs[i].reset()
        apcs[i].set_program(program)
        apcs[i].input = [phase_setting[i]]

    next_input = 0
    i = 0

    while not apcs[-1].program_finished:
        apcs[i].input.append(next_input)
        apcs[i].run_program()
        next_input = apcs[i].output
        i = (i + 1) % len(apcs)

    return apcs[-1].output


def get_solution_to_problem_1():
    program = read_input('input1')
    phase_settings = [str_vec_to_int_vec(list(''.join(p))) for p in permutations('01234')]
    highest_thrusters_signal = 0

    for phase_setting in phase_settings:
        thrusters_signal = get_thrusters_signal(phase_setting, program)
        if highest_thrusters_signal < thrusters_signal:
            highest_thrusters_signal = thrusters_signal

    print(f'Highest thrusters signal is {highest_thrusters_signal}.')


def get_solution_to_problem_2():
    program = read_input('input1')
    phase_settings = [str_vec_to_int_vec(list(''.join(p))) for p in permutations('56789')]
    highest_thrusters_signal = 0

    for phase_setting in phase_settings:
        thrusters_signal = get_thrusters_loopback_signal(phase_setting, program)
        if highest_thrusters_signal < thrusters_signal:
            highest_thrusters_signal = thrusters_signal

    print(f'Highest loopback thrusters signal is {highest_thrusters_signal}.')


get_solution_to_problem_1()
get_solution_to_problem_2()

