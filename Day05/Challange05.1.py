file = open("./Day05/input.txt", "r")

input_strings = file.readlines()

nice_lines = 0

for line in input_strings:
    if line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u") < 3:
        continue

    i = 1
    double_found = False
    while i < len(line):
        if line[i] == line [i-1]:
            double_found = True
            break

        i += 1

    if double_found == False:
        continue

    if line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy") > 0:
        continue

    nice_lines += 1

print(nice_lines)