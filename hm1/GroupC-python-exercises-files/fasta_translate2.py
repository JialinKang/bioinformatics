def codonTable2dict(table_path):
    f = open(table_path, 'r')
    line = f.readline()
    dna2pro = {}
    while line != '':
        dna2pro[line[0:3]] = line[4]
        line = f.readline()
    f.close()    
    print(dna2pro)

codonTable2dict('./codon_table.txt')