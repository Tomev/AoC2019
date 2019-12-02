from math import floor


def read_input(input_path):
    file = open(input_path, "r+")
    lines = file.readlines()
    file.close()

    input_vector = []

    for line in lines:
        input_vector.append(int(line))

    return input_vector


def count_module_fuel_requirement(mod):
    fuel_req = floor(mod / 3) - 2
    if fuel_req < 0:
        fuel_req = 0
    return fuel_req


def count_additional_fuel_requirement(fuel_req):
    add_fuel_req = 0
    last_additional_fuel_req = fuel_req
    while last_additional_fuel_req != 0:
        last_additional_fuel_req = count_module_fuel_requirement(last_additional_fuel_req)
        add_fuel_req += last_additional_fuel_req

    return add_fuel_req


def count_module_full_fuel_requirement(mod):
    mod_fuel_req = count_module_fuel_requirement(mod)
    additional_fuel_req = count_additional_fuel_requirement(mod_fuel_req)
    return mod_fuel_req + additional_fuel_req


def print_first_problem_solution():
    modules = read_input('input1.txt')
    fuel_reqs = []
    for module in modules:
        fuel_reqs.append(count_module_fuel_requirement(module))

    print(f'First problem solution is: {sum(fuel_reqs)}.')


def print_second_problem_solution():
    modules = read_input('input1.txt')
    fuel_reqs = []
    for module in modules:
        fuel_reqs.append(count_module_full_fuel_requirement(module))

    print(f'Second problem solution is: {sum(fuel_reqs)}.')


# print_first_problem_solution()
print_second_problem_solution()
