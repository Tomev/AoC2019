class ShipComputer:
    initial_program = []
    program = []
    ip = 0  # Instruction pointer
    instructions = dict()  # Dict of instructions
    EXIT_CODE = 99
    input = [0]
    output = 0

    def __init__(self):
        self.instructions[1] = self.perform_instruction_1
        self.instructions[2] = self.perform_instruction_2
        self.instructions[3] = self.perform_instruction_3
        self.instructions[4] = self.perform_instruction_4
        self.instructions[5] = self.perform_instruction_5
        self.instructions[6] = self.perform_instruction_6
        self.instructions[7] = self.perform_instruction_7
        self.instructions[8] = self.perform_instruction_8

    def run_program(self):
        self.ip = 0

        while True:
            ic = self.get_instruction_code(self.program[self.ip])
            if ic == self.EXIT_CODE:
                break
            self.instructions[ic]()

    def get_instruction_code(self, code: int):
        code_str = str(code)
        if len(code_str) > 2:
            ic = int(code_str[-1]) + int(code_str[-2])
        else:
            ic = self.program[self.ip]
        return ic

    def get_parameter_value(self, parameter_number: int):
        code = str(self.program[self.ip])

        if len(code) < 3:
            return self.program[self.program[self.ip + parameter_number]]

        while len(code) < 5:
            code = '0' + code

        parameter_mode = code[-2 - parameter_number]

        if parameter_mode == '1':
            return self.program[self.ip + parameter_number]
        else:
            return self.program[self.program[self.ip + parameter_number]]

    def get_input(self):
        return self.input.pop(0)

    def set_program(self, new_program):
        self.program = new_program
        self.initial_program = new_program

    def reset_program(self):
        self.program = self.initial_program

    def perform_instruction_1(self):
        output_address = self.program[self.ip + 3]
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        self.program[output_address] = param1 + param2
        self.ip += 4

    def perform_instruction_2(self):
        output_address = self.program[self.ip + 3]
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        self.program[output_address] = param1 * param2
        self.ip += 4

    def perform_instruction_3(self):
        self.program[self.program[self.ip + 1]] = self.get_input()
        self.ip += 2

    def perform_instruction_4(self):
        param1 = self.get_parameter_value(1)
        print(f'Output: {param1}.')
        self.output = param1
        self.ip += 2

    def perform_instruction_5(self):
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        if param1 != 0:
            self.ip = param2
        else:
            self.ip += 3

    def perform_instruction_6(self):
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        if param1 == 0:
            self.ip = param2
        else:
            self.ip += 3

    def perform_instruction_7(self):
        address = self.program[self.ip + 3]
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        if param1 < param2:
            result = 1
        else:
            result = 0
        self.program[address] = result
        self.ip += 4

    def perform_instruction_8(self):
        address = self.program[self.ip + 3]
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        if param1 == param2:
            result = 1
        else:
            result = 0
        self.program[address] = result
        self.ip += 4
