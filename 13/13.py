from ship import ShipComputer
from std import Point, get_program_from_input


class Tile:
    def __init__(self, position: Point, tile_type: str):
        self.position = position
        self.tile_type = tile_type


def get_solution_to_problem_1():

    program = get_program_from_input('input')
    computer = ShipComputer()
    computer.set_program(program)
    computer.run_program()
    tiles = get_tiles_from_output(computer.outputs)
    block_tiles_number = 0

    for tile in tiles:
        if tile.tile_type == '#':
            block_tiles_number += 1

    print_map(tiles)
    print(block_tiles_number)


def get_tiles_from_output(output):
    i = 0
    tiles_types = [' ', '|', '#', '_', 'O']
    tiles = []
    while i < len(output):
        tiles.append(Tile(Point(output[i], output[i + 1]), tiles_types[output[i + 2]]))
        i += 3

    return tiles


def get_map(tiles):
    max_x = tiles[0].position.x
    max_y = tiles[0].position.y

    for tile in tiles:
        if tile.position.x > max_x:
            max_x = tile.position.x
        if tile.position.y > max_y:
            max_y = tile.position.y

    game_map = [[' ' for j in range(max_x + 1)] for i in range(max_y + 1)]

    for tile in tiles:
        game_map[tile.position.y][tile.position.x] = tile.tile_type

    return game_map


def print_map(tiles):
    game_map = get_map(tiles)

    for row in game_map:
        print(''.join(row))


def get_solution_to_problem_2():
    program = get_program_from_input('input')
    computer = ShipComputer()
    program[0] = 2
    computer.set_program(program)
    computer.input = [1]
    computer.run_program()
    tiles = get_tiles_from_output(computer.outputs)

    computer.debug = True

    while not computer.program_finished:
        print(computer.input)
        x = input()
        computer.input = [int(x)]
        computer.run_program()
        print_map(tiles)


# get_solution_to_problem_1()
get_solution_to_problem_2()

