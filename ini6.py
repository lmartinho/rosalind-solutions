f = open("rosalind_ini6.txt", "r")
line = f.readline()
words = line.strip().split(" ")
count = {}
for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

for word in count:
    print("%s %d" % (word, count[word]))
