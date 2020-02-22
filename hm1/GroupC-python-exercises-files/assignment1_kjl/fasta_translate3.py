from fasta_translate1 import fafile2dict
from fasta_translate2 import codonTable2dict
import sys

def dna2pro(codon, gene, fafilename):
    '''
    translate gene FASTA file and print in FASTA format

    Parameter
    ----------------
    codon:dict
    the codon table dictionary form {'codon':'protein'}
    gene:dict
    the gene dictionary form {'gene name':'DNA sequence'}
    fafilename:str
    the name of protein sequence file
    ----------------
    '''
    f = open(fafilename, 'a')
    for describe,seq in gene.items():
        protein = ''
        sys.stdout.write(describe)
        for frag in range(0, len(seq), 3):
            if len(seq)-frag < 3:
                break
            else:
                protein = protein + codon[seq[frag:frag+3]]
        # print(protein)
        sys.stdout.write('the protein sequence is :' + '\n')
        sys.stdout.write(protein + '\n')
        f.write(protein)
        f.write('\n')

    f.close()
    return describe, protein

if __name__ == "__main__":
    codon = codonTable2dict('./codon_table.txt')
    genedict = fafile2dict()
    dna2pro(codon, genedict, 'genes2protein.fa')
    # (describe,protein) = dna2pro(codon, genedict, 'gene2protein.fa')
    
    