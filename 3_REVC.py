def Rosalind3(s):
    rev = s[::-1]
    comp = ""
    for i in rev:
        if i == 'A':
            comp = comp + i.replace('A','T')
        elif i == 'G':
            comp = comp + i.replace('G','C')
        elif i == 'C':
            comp = comp + i.replace('C','G')
        elif i == 'T':
            comp = comp + i.replace('T', 'A')
    print(comp)

input = open("rosalind_revc.txt","r")
Rosalind3(input.read())

#or you can take advantage of case sensitivity:
def forumAns(s):
    return s.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]

print(forumAns(input.read()))
