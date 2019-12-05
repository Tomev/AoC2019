from ship import ShipComputer


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


def get_solution_to_problem_1():
    program = read_input('input1.txt')
    program[1] = 12
    program[2] = 2

    computer = ShipComputer()
    computer.set_program(program)
    computer.run_program()

    print(f'Solution to problem 1 is {computer.program[0]}')


def get_solution_to_problem_2():
    desired_output = 19690720

    verb = 0
    noun = 0

    solution_found = False
    initial_program = read_input('input1.txt')
    computer = ShipComputer()

    for verb in range(100):
        for noun in range(100):
            program = initial_program.copy()
            program[1] = noun
            program[2] = verb
            computer.set_program(program)
            computer.run_program()
            if computer.program[0] == desired_output:
                solution_found = True
                break

        if solution_found:
            break

    print(f'Solution to problem 2 is {100 * noun + verb}')


get_solution_to_problem_1()
get_solution_to_problem_2()
