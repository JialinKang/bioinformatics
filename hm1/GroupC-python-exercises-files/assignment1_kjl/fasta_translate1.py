import sys

def fafile2dict():
    '''
    read a single FASTA file (SHH.fa) into a dictionary object
    and print out the dictionary

    Rerurn
    --------------
    seq:dict
    the single gene dict, {descriptor_str:sequence_str}
    --------------
    '''
    line = sys.stdin.readline().replace('\n','')
    seq = {}
    while line != '':
        if line[0] == '>':
            name = line.replace('>','')
            seq[name] = ''
        else:
            seq[name] += line.replace('\n','').strip()
        line = sys.stdin.readline()
    return seq

if __name__ == "__main__":
    seq = fafile2dict()
    print(seq)
    

