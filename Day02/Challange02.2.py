file = open("./Day02/input.txt")

lines = file.readlines()

total_length = 0

for line in lines:

    length = int(line.split("x")[0])
    width = int(line.split("x")[1])
    height = int(line.split("x")[2])

    total_length += min(2 * length + 2 * width, 2 * length + 2 * height, 2 * width + 2 * height)
    total_length += length * width * height

print(total_length)