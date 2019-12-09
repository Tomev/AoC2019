def get_program_from_input(input_path):
    return read_input(input_path)


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