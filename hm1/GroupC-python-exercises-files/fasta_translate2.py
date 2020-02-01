from fasta_translate1 import fafile2dict


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
    line = f.readline()
    codondict = {}
    while line != '':
        codondict[line[0:3]] = line[4]
        line = f.readline()
    f.close()    
    print(codondict)

    return codondict


def dna2pro(codon, gene):
    for seq in gene.values():
        protein = ''
        for frag in range(0, len(seq), 3):
            if len(seq)-frag < 3:
                break
            else:
                protein = protein + codon[seq[frag:frag+3]]
        print(protein)


if __name__ == "__main__":
    codon = codonTable2dict('./codon_table.txt')
    genedict = fafile2dict()
    dna2pro(codon, genedict)