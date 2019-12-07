class SpaceObject:
    name = ''
    directly_orbits = ''
    indirectly_orbits = set()

    def __init__(self, name, direct_orbit):
        self.name = name
        self.directly_orbits = direct_orbit
        self.indirectly_orbits = set()

    def __repr__(self):
        if self.directly_orbits == '':
            space_object = 'nothing'
        else:
            space_object = self.directly_orbits

        return f'{self.name} directly orbits {space_object} and indirectly orbits {list(self.indirectly_orbits)}.'

    def get_orbits_number(self):
        orbits_number = 0
        if self.directly_orbits != '':
            orbits_number += 1
        return orbits_number + len(list(self.indirectly_orbits))


def count_orbits():
    orbits_num = 0

    for space_object in space_map:
        orbits_num += space_object.get_orbits_number()

    return orbits_num


def get_space_map(input_path):
    s_map = [SpaceObject('COM', '')]

    file = open(input_path, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        name_orbit = line.split(')')
        s_map.append(SpaceObject(name_orbit[1].strip(), name_orbit[0].strip()))

    fill_indirect_orbits(s_map)

    return s_map


def fill_indirect_orbits(space_objects):
    for space_object in space_objects:
        if space_object.directly_orbits == '':
            continue

        next_orbited_object = get_object_by_name(space_objects, space_object.directly_orbits)

        while next_orbited_object.directly_orbits != '':
            next_orbited_object = get_object_by_name(space_objects, next_orbited_object.directly_orbits)
            space_object.indirectly_orbits.add(next_orbited_object.name)


def get_object_by_name(space_objects, name):

    for space_object in space_objects:
        if space_object.name == name:
            return space_object


def count_orbital_transfers(source, target: str):
    number_of_transfers = 0
    current_position = source

    while current_position.name != target:
        number_of_transfers += 1
        current_position = get_object_by_name(space_map, current_position.directly_orbits)

    return number_of_transfers - 1


def get_problem_1_solution():
    print(f'Solution to problem 1 is {count_orbits()}.')


def get_problem_2_solution():
    # Find intersection of objects orbited by YOU and SAN
    san = get_object_by_name(space_map, 'SAN')
    you = get_object_by_name(space_map, 'YOU')
    shared_orbits = list(san.indirectly_orbits.intersection(you.indirectly_orbits))

    # More optimal search can be proposed, but this one should suffice for this task
    # I imagine that finding shared orbit closest to COM is also the proper approach

    min_distance = count_orbital_transfers(san, shared_orbits[0]) + count_orbital_transfers(you, shared_orbits[0])

    for shared_orbit in shared_orbits:
        distance = count_orbital_transfers(san, shared_orbit) + count_orbital_transfers(you, shared_orbit)
        if distance < min_distance:
            min_distance = distance

    print(f'Solution to problem 2 is {min_distance}.')


space_map = get_space_map('input1')
get_problem_1_solution()
get_problem_2_solution()
