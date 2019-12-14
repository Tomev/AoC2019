from math import gcd


class Moon:

    def __init__(self, x, y, z, vx=0, vy=0, vz=0):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def update_velocities(self, moons):
        for moon in moons:

            if moon.x > self.x:
                self.vx += 1
            if moon.x < self.x:
                self.vx -= 1

            if moon.y > self.y:
                self.vy += 1
            if moon.y < self.y:
                self.vy -= 1

            if moon.z > self.z:
                self.vz += 1
            if moon.z < self.z:
                self.vz -= 1

    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def __str__(self):
        return f'pos=[{self.x}, {self.y}, {self.z}], v=[{self.vx}, {self.vy}, {self.vz}]'


def get_moons():
    f = open('input')
    line = f.readline()
    moons = []

    while line:
        line = line[0:-2]
        line_parts = line.split(',')
        x = int(line_parts[0].split('=')[1])
        y = int(line_parts[1].split('=')[1])
        z = int(line_parts[2].split('=')[1])
        moons.append(Moon(x, y, z))

        line = f.readline()

    f.close()

    return moons


def get_solution_to_problem_1():
    moons = get_moons()
    steps_number = 1000

    for i in range(steps_number):

        # print(f'After {i} steps:')
        # for moon in moons:
        #    print(moon)

        for moon in moons:
            moon.update_velocities(moons)
        for moon in moons:
            moon.update_position()

    total_energy = 0

    for moon in moons:
        total_energy += moon.get_total_energy()

    print(total_energy)


def get_solution_to_problem_2():
    initial_moons = get_moons()
    moons = get_moons()
    steps_to_repeat_x = -1
    steps_to_repeat_y = -1
    steps_to_repeat_z = -1
    step = 0

    while steps_to_repeat_x < 0 or steps_to_repeat_y < 0 or steps_to_repeat_z < 0:
        for moon in moons:
            moon.update_velocities(moons)
        for moon in moons:
            moon.update_position()

        x_repeated = y_repeated = z_repeated = True

        for i in range(len(moons)):
            if not (initial_moons[i].vx == moons[i].vx and initial_moons[i].x == moons[i].x):
                x_repeated = False
            if not (initial_moons[i].vy == moons[i].vy and initial_moons[i].y == moons[i].y):
                y_repeated = False
            if not (initial_moons[i].vz == moons[i].vz and initial_moons[i].z == moons[i].z):
                z_repeated = False

        step += 1

        if x_repeated and steps_to_repeat_x < 0:
            steps_to_repeat_x = step

        if y_repeated and steps_to_repeat_y < 0:
            steps_to_repeat_y = step

        if z_repeated and steps_to_repeat_z < 0:
            steps_to_repeat_z = step

    result = steps_to_repeat_x * steps_to_repeat_y // gcd(steps_to_repeat_x, steps_to_repeat_y)
    result = result * steps_to_repeat_z // gcd(steps_to_repeat_z, result)

    print(result)

get_solution_to_problem_2()
