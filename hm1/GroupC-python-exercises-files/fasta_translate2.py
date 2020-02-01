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
    dna2pro:dict
    the dictionary form of codontable
    ------------------------
    '''
    f = open(table_path, 'r')
    line = f.readline()
    dna2pro = {}
    while line != '':
        dna2pro[line[0:3]] = line[4]
        line = f.readline()
    f.close()    
    print(dna2pro)

    return dna2pro

codonTable2dict('./codon_table.txt')