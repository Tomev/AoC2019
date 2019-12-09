from ship import ShipComputer
from std import get_program_from_input


def get_solution_to_problem_1():
    cpu = ShipComputer()
    cpu.input.append(1)
    program = get_program_from_input('input')
    cpu.set_program(program)
    cpu.run_program()


get_solution_to_problem_1()