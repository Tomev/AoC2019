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


def run_program(program):
    i = 0
    while True:

        if program[i] == 99:
            break

        operation_result = 0

        if program[i] == 1:
            operation_result = program[program[i+1]] + program[program[i+2]]
        if program[i] == 2:
            operation_result = program[program[i+1]] * program[program[i+2]]

        program[program[i+3]] = operation_result
        i += 4

    return program


def get_solution_to_problem_1():
    program = read_input('input1.txt')
    program[1] = 12
    program[2] = 2
    print(f'Solution to problem 1 is {run_program(program)[0]}')


def get_solution_to_problem_2():
    desired_output = 19690720

    verb = 0
    noun = 0

    solution_found = False

    for verb in range(100):
        for noun in range(100):
            program = read_input('input1.txt')
            program[1] = noun
            program[2] = verb
            program = run_program(program)
            if program[0] == desired_output:
                print(f'Verb = {verb}, Noun = {noun}, Out = {program[0]}')
                solution_found = True
                break

        if solution_found:
            break

    print(f'Solution to problem 2 is {100 * noun + verb}')


# get_solution_to_problem_1()
get_solution_to_problem_2()
