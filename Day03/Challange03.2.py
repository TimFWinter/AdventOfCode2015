file = open("./Day03/input.txt", "r")

input_data = file.read()

present_map = {}

present_map.update({"0, 0" : 1})

current_x_position = 0
current_y_position = 0

alternate_x_position = 0
alternate_y_position = 0 

iterator = 1
for char in input_data:

    if char == "^":
        if iterator % 2 != 0:
            current_y_position += 1
        else:
            alternate_y_position += 1

    elif char == ">":
        if iterator % 2 != 0:
            current_x_position += 1
        else:
            alternate_x_position += 1

    elif char == "v":
        if iterator % 2 != 0:
            current_y_position -= 1
        else:
            alternate_y_position -= 1

    elif char == "<":
        if iterator % 2 != 0:
            current_x_position -= 1
        else:
            alternate_x_position -= 1
    
    if iterator % 2 != 0:
        presents_there = present_map.get(str(current_x_position) + ", " + str(current_y_position))
    else:
        presents_there = present_map.get(str(alternate_x_position) + ", " + str(alternate_y_position))

    try:
        presents_there = int(presents_there)
    
    except:
        presents_there = 0
    
    if iterator % 2 != 0:
        present_map.update({str(current_x_position) + ", " + str(current_y_position) : presents_there + 1})
    else:
        present_map.update({str(alternate_x_position) + ", " + str(alternate_y_position) : presents_there + 1})

    iterator += 1

print(len(present_map))