from fasta_translate1 import fafile2dict
from fasta_translate2 import dna2pro, codonTable2dict
import sys


def codonHard2dict(table_hard):
    '''
    transform codon_table_hard to dict form

    Parameter
    -----------------
    table_hard:str
    the path of codon_table_hard.txt
    -----------------

    Return
    -----------------
    codon_dict:dict
    the codon_table_hard dictionary form
    -----------------
    '''
    f = open(table_hard, 'r')
    line_list = f.readline().replace('\n','').split()
    codon_dict = {}
    while line_list != []:
        codon_list = line_list[2].split(',')
        for codon in codon_list:
            codon_dict[codon] = line_list[1]
        line_list = f.readline().replace('\n','').split()
    f.close()

    return codon_dict

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
        codon_error = []
        
        sys.stdout.write(describe)
        sys.stdout.write('the error codon is :' + '\n')
        for frag in range(0, len(seq), 3):
            if len(seq)-frag < 3:
                break
            else:
                if seq[frag:frag+3] not in codon.keys():
                    sys.stderr.write('Codon Error: ' + seq[frag:frag+3] + '\n')
                    codon_error.append(seq[frag:frag+3])
                    continue
                else:
                    protein = protein + codon[seq[frag:frag+3]]
        f.write(protein)
        sys.stdout.write('the protein sequence is :' + '\n')
        sys.stdout.write(protein + '\n')
        f.write('\n')

    f.close()


if __name__ == "__main__":
    codon = codonHard2dict('codon_table_hard.txt')
    genedict = fafile2dict()
    dna2pro(codon, genedict, 'genesmess.fa')