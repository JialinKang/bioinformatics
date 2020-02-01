from fasta_translate1 import fafile2dict
from fasta_translate2 import dna2pro, codonTable2dict



if __name__ == "__main__":
    codon = codonTable2dict('./codon_table.txt')
    genedict = fafile2dict()
    dna2pro(codon, genedict, 'genes2protein.fa')