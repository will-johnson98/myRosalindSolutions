DNA = []
with open ("rosalind_hamm.txt", 'rt') as myfile:
    for line in myfile:
        DNA.append(line)
for i in range(len(DNA)):
    DNA[i] = DNA[i].rstrip('\n')

print(sum(a!=b for a, b in zip(DNA[0],DNA[1])))
