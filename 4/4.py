def get_problem_1_solution():

    possible_passwords = []

    for password in range(153517, 630395):
        if satisfies_criteria(str(password)):
            possible_passwords.append(str(password))

    print(f'Number of possible different passwords within given range is {len(possible_passwords)}.')

    return possible_passwords


def satisfies_criteria(password: str):
    return contains_at_least_double_adjacent(password) and has_no_decreasing_numbers(password)


def contains_at_least_double_adjacent(password: str):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True

    return False


def has_no_decreasing_numbers(password):
    for i in range(len(password) - 1):
        if password[i] > password[i + 1]:
            return False

    return True


def contains_double_adjacent(password: str):
    for i in range(len(password) - 1):
        if password.count(password[i]) == 2:
            return True

    return False


def get_problem_2_solution():
    possible_passwords = get_problem_1_solution()
    number_of_possible_passwords_after_condition = 0

    for password in possible_passwords:
        if contains_double_adjacent(password):
            number_of_possible_passwords_after_condition += 1

    print(f'Number of possible passwords after new conditions is {number_of_possible_passwords_after_condition}.')


get_problem_2_solution()
