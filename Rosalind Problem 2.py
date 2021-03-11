input = open("rosalind_rna.txt", "r")

def DNAtoRNA(x):
    return x.replace('T', 'U')

DNA = input.read()
print(DNAtoRNA(DNA))

