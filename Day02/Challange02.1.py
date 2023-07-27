file = open("./Day02/input.txt")

lines = file.readlines()

total_area = 0

for line in lines:

    length = int(line.split("x")[0])
    width = int(line.split("x")[1])
    height = int(line.split("x")[2])

    total_area += (2 * length * width + 2 * length * height + 2 * width * height)
    total_area += min(length * width, length * height, width * height)

print(total_area)