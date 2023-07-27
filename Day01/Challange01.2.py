file = open("./Day01/input.txt", "r")

input_data = file.read()

floor = 0

iterator = 1
for char in input_data:
    if char == "(":
        floor += 1

    elif char == ")":
        floor -= 1

    if floor == -1:
        print("Position ", iterator)
        break

    iterator += 1