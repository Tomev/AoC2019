class ShipComputer:
    EXIT_CODE = 99

    def __init__(self):
        self.initial_program = []

        self.instructions = {
            1: self.perform_instruction_1,
            2: self.perform_instruction_2,
            3: self.perform_instruction_3,
            4: self.perform_instruction_4,
            5: self.perform_instruction_5,
            6: self.perform_instruction_6,
            7: self.perform_instruction_7,
            8: self.perform_instruction_8,
            9: self.perform_instruction_9
        }

        self.address_getters = {
            0: self.get_position_mode_address,
            1: self.get_immediate_mode_address,
            2: self.get_relative_mode_address
        }
        self.name = 'CPU'

        self.program = []
        self.ip = 0  # Instruction pointer
        self.input = []
        self.output = 0
        self.relative_base = 0
        self.ic = 0

        self.program_finished = False

    def reset(self):
        self.ip = 0
        self.program = self.initial_program
        self.output = 0
        self.input = []
        self.program_finished = False
        self.relative_base = 0
        self.ic = 0

    def run_program(self):

        while not self.program_finished:
            self.ic = self.get_instruction_code(self.program[self.ip])

            # print(f'Instruction {self.program[self.ip]}, ip:{self.ip}')

            if self.ic == 3 and len(self.input) == 0:
                print(f'{self.name}: Input required.')
                break

            if self.ic == self.EXIT_CODE:
                self.program_finished = True
                break

            self.instructions[self.ic]()

    def get_instruction_code(self, code: int):
        code_str = str(code)
        if len(code_str) > 2:
            ic = int(code_str[-2] + code_str[-1])
        else:
            ic = self.program[self.ip]
        return ic

    def get_parameter_value(self, parameter_number: int):
        value_address = self.get_address_from_parameter(parameter_number)
        return self.program[value_address]

    def get_address_from_parameter(self, parameter_number: int):
        code = str(self.program[self.ip])

        if len(code) < 3:
            return self.program[self.ip + parameter_number]

        while len(code) < 5:
            code = '0' + code

        parameter_mode = int(code[-2 - parameter_number])

        address_getter = self.address_getters.get(parameter_mode, self.get_position_mode_address)
        address = address_getter(parameter_number)
        self.adjust_program_memory(address)
        return address

    def get_input(self):
        return self.input.pop(0)

    def set_program(self, new_program):
        self.program = new_program
        self.initial_program = new_program

    def reset_program(self):
        self.program = self.initial_program

    def adjust_program_memory(self, requested_index):

        # print(f'Adjusting {len(self.program)} to {requested_index + 1}.')

        while len(self.program) <= requested_index:
            self.program.append(0)

    def perform_instruction_1(self):
        output_address = self.get_address_from_parameter(3)
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        self.program[output_address] = param1 + param2
        self.ip += 4

    def perform_instruction_2(self):
        output_address = self.get_address_from_parameter(3)
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        self.program[output_address] = param1 * param2
        self.ip += 4

    def perform_instruction_3(self):
        output_address = self.get_address_from_parameter(1)
        self.adjust_program_memory(output_address)
        self.program[output_address] = self.get_input()
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
        address = self.get_address_from_parameter(3)
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        if param1 < param2:
            result = 1
        else:
            result = 0
        self.program[address] = result
        self.ip += 4

    def perform_instruction_8(self):
        address = self.get_address_from_parameter(3)
        self.adjust_program_memory(address)
        param1 = self.get_parameter_value(1)
        param2 = self.get_parameter_value(2)
        if param1 == param2:
            result = 1
        else:
            result = 0
        self.program[address] = result
        self.ip += 4

    def perform_instruction_9(self):
        param1 = self.get_parameter_value(1)
        self.relative_base += param1
        self.ip += 2

    def get_position_mode_address(self, parameter_number):
        return self.program[self.ip + parameter_number]

    def get_immediate_mode_address(self, parameter_number):
        return self.ip + parameter_number

    def get_relative_mode_address(self, parameter_number):
        return self.program[self.ip + parameter_number] + self.relative_base
