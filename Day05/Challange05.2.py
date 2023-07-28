file = open("./Day05/input.txt", "r")

input_strings = file.readlines()

nice_lines = 0

for line in input_strings:

    pair_twice = False

    iterator = 1
    while iterator < len(line):
        if line.count(line[iterator - 1] + line[iterator]) > 1:
            pair_twice = True
            break

        iterator += 1

    if pair_twice == False:
        continue

    distatnt_pair = False
    iterator = 2
    while iterator < len(line):
        if line[iterator - 2] == line[iterator]:
            distatnt_pair = True

        iterator += 1

    if distatnt_pair == False:
        continue

    nice_lines += 1


print(nice_lines)