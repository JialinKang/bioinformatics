from fasta_translate1 import fafile2dict
import sys


def codonTable2dict(table_path):
    '''
    trans codon table into a dict

    Parameter
    ------------------------
    table_path: str
    the path of codon_table
    ------------------------

    Return
    ------------------------
    codondict:dict
    the dictionary form of codontable
    ------------------------
    '''
    f = open(table_path, 'r')
    line = f.readline().replace('\n','')
    codondict = {}
    while line != '':
        codondict[line[0:3]] = line[4]
        line = f.readline()
    f.close()    

    return codondict


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
        for frag in range(0, len(seq), 3):
            if len(seq)-frag < 3:
                break
            else:
                protein = protein + codon[seq[frag:frag+3]]
        # print(protein)
        f.write(protein)
        f.write('\n')

    f.close()
    return describe, protein
        


if __name__ == "__main__":
    codon = codonTable2dict('./codon_table.txt')
    genedict = fafile2dict()
    (describe,protein) = dna2pro(codon, genedict, 'gene2protein.fa')
    sys.stdout.write(describe + '\n')
    sys.stdout.write('the protein sequence is :' + '\n')
    sys.stdout.write(protein + '\n')