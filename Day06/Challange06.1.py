file = open("./Day06/input.txt", "r")
instructions = file.readlines()

def turn_on_lights(x1: int, y1: int, x2: int, y2: int):

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            light_grid[x][y] = True

def turn_off_lights(x1: int, y1: int, x2: int, y2: int):

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            light_grid[x][y] = False

def toggle_lights(x1: int, y1: int, x2: int, y2: int):

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            light_grid[x][y] = not light_grid[x][y]

light_grid = [[False for i in range(0, 1000)] for j in range(0, 1000)]

for line in instructions:
    if line.split()[0] == "toggle":
        toggle_lights(int(line.split()[1].split(",")[0]), int(line.split()[1].split(",")[1]), int(line.split()[3].split(",")[0]), int(line.split()[3].split(",")[1]))

    elif line.split()[1] == "on":
        turn_on_lights(int(line.split()[2].split(",")[0]), int(line.split()[2].split(",")[1]), int(line.split()[4].split(",")[0]), int(line.split()[4].split(",")[1]))

    elif line.split()[1] == "off":
        turn_off_lights(int(line.split()[2].split(",")[0]), int(line.split()[2].split(",")[1]), int(line.split()[4].split(",")[0]), int(line.split()[4].split(",")[1]))

active_lights = 0

for row in light_grid:
    for light in row:
        if light == True:
            active_lights += 1

print(active_lights)