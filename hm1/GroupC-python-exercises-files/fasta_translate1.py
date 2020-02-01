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
    line = sys.stdin.readline()
    seq = {}
    while line != '':
        if line[0] == '>':
            name = line.replace('\n','')
            seq[name] = ''
        else:
            seq[name] += line.replace('\n','').strip()
        line = sys.stdin.readline()
    print(seq)
    return seq

if __name__ == "__main__":
    fafile2dict()

