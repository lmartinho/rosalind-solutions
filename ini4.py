f = open("rosalind_ini4.txt", "r")
line1 = f.readline()
a,b = [int(number) for number in line1.split(" ")]
print(sum([x for x in range(a, b) if x % 2 != 0]))
