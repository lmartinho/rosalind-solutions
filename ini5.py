f = open("rosalind_ini5.txt", "r")
i = 1
even_lines = []
for line in f:
    if i % 2 == 0:
        even_lines.append(line.strip())
    i += 1

[print(line) for line in even_lines]
