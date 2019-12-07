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
    program = read_input('input1')
    computer = ShipComputer()
    computer.input = [1]
    computer.set_program(program)
    computer.run_program()


def get_solution_to_problem_2():
    program = read_input('input1')
    computer = ShipComputer()
    computer.input = [5]
    computer.set_program(program)
    computer.run_program()


get_solution_to_problem_1()
get_solution_to_problem_2()

