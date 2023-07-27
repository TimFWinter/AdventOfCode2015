file = open("./Day03/input.txt", "r")

input_data = file.read()

present_map = {}

present_map.update({"0, 0" : 1})

current_x_position = 0
current_y_position = 0

for char in input_data:

    if char == "^":
        current_y_position += 1

    elif char == ">":
        current_x_position += 1

    elif char == "v":
        current_y_position -= 1

    elif char == "<":
        current_x_position -= 1
        
    presents_there = present_map.get(str(current_x_position) + ", " + str(current_y_position))

    try:
        presents_there = int(presents_there)
    
    except:
        presents_there = 0

    present_map.update({str(current_x_position) + ", " + str(current_y_position) : presents_there + 1})

print(len(present_map))