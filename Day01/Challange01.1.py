file = open("./Day01/input.txt", "r")

input_data = file.read()

floor = 0

for char in input_data:
    if char == "(":
        floor += 1

    elif char == ")":
        floor -= 1

print(floor)