from Bio import SeqIO
def Ros5(file):
    for seq_record in SeqIO.parse(file,"fasta"):
        CG = seq_record.seq.count('G')+seq_record.seq.count('C')
        CGpt = 100*(CG/len(seq_record.seq))
        print(seq_record.id)
        print(CGpt)
Ros5('rosalind_gc.txt')
