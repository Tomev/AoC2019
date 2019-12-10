from ship import ShipComputer
from std import get_program_from_input


def get_solution_to_problem_1():
    cpu = ShipComputer()
    cpu.input.append(1)
    program = get_program_from_input('input')
    # program = get_program_from_input('test3')
    cpu.set_program(program)
    cpu.run_program()


def get_solution_to_problem_2():
    cpu = ShipComputer()
    cpu.input.append(2)
    program = get_program_from_input('input')
    # program = get_program_from_input('test3')
    cpu.set_program(program)
    cpu.run_program()


get_solution_to_problem_1()
get_solution_to_problem_2()