NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
MOVES = [NORTH, EAST, SOUTH, WEST]
LEFT = "L"
RIGHT = "R"
TURNS = [LEFT, RIGHT]
FORWARD = "F"


class Ship:

    def __init__(self, north, east, direction):
        self.north = north
        self.east = east
        self.direction = direction

    def __str__(self):
        return f"Ship is at location {self.north} North and {self.east} East, moving in direction {self.direction}."

    def exec_command(self, *args):
        command = args[0]
        param = args[1]
        if command in MOVES:
            self.move(command, param)
        elif command in TURNS:
            self.turn(command, param)
        elif command == FORWARD:
            self.forward(param)

    def move(self, direction, distance):
        if direction == NORTH:
            self.north += distance
        elif direction == EAST:
            self.east += distance
        elif direction == SOUTH:
            self.north -= distance
        elif direction == WEST:
            self.east -= distance

    def turn(self, direction, degrees):
        cur_dir_i = MOVES.index(self.direction)
        dir_mul = 1
        if direction == LEFT:
            dir_mul = -1
        next_dir_i = cur_dir_i + (degrees // 90) * dir_mul
        if next_dir_i < 0:
            next_dir_i += 4
        if next_dir_i >= 4:
            next_dir_i -= 4
        self.direction = MOVES[next_dir_i]

    def forward(self, distance):
        self.move(self.direction, distance)