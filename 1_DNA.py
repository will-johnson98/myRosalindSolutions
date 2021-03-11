input = open("rosalind_dna.txt", "r")
DNA = input.read()
countA = 0
countC = 0
countG = 0
countT = 0
for i in DNA:
    if i == "A":
        countA = countA + 1
    elif i == "T":
        countT = countT + 1
    elif i == "G":
        countG = countG + 1
    elif i == "C":
        countC = countC + 1
print(countA, countC, countG, countT)
