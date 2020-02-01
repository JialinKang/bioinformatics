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
    print(codon_dict)
    f.close()

    return codon_dict




if __name__ == "__main__":
    codonHard2dict('codon_table_hard.txt')