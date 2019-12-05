class ShipComputer:
    initial_program = []
    program = []
    ip = 0                  # Instruction pointer
    instructions = dict()   # Dict of instructions
    EXIT_CODE = 99

    def __init__(self):
        self.instructions[1] = self.perform_instruction_1
        self.instructions[2] = self.perform_instruction_2

    def run_program(self):
        self.ip = 0
        while True:
            if self.program[self.ip] == self.EXIT_CODE:
                break
            self.instructions[self.program[self.ip]]()

    def set_program(self, new_program):
        self.program = new_program
        self.initial_program = new_program

    def reset_program(self):
        self.program = self.initial_program

    def perform_instruction_1(self):
        self.program[self.program[self.ip + 3]] = self.program[self.program[self.ip + 1]] + \
                                                  self.program[self.program[self.ip + 2]]
        self.ip += 4

    def perform_instruction_2(self):
        self.program[self.program[self.ip + 3]] = self.program[self.program[self.ip + 1]] * \
                                                  self.program[self.program[self.ip + 2]]
        self.ip += 4


