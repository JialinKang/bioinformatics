## EN 580.688, Spring2020, HW1, GroupC
## Wen Shi, JEHD ID: wshi13
## January 29th, 2020

## Fourth script
import sys

## Read the FASTA file
file = sys.stdin
seqdic = {}
while True:
    line = file.readline()
    if len(line) == 0:
        break
    if line.startswith('>'):
        describe = line
        seq = ''
        seqdic[describe] = seq
    else:
        sequence = line.rstrip()
        seqdic[describe] = seqdic[describe] + sequence

## Read in the codon table
table = open('codon_table_hard.txt')
codontable = {}
while True:
    line = table.readline().rstrip()
    if len(line) == 0:
        break
    line = line.split()
    tri = line[2]
    ac = line[1]
    tri = tri.split(',')
    for a in tri:
        codontable[a] = ac

## Translate and output into fasta format
prodic = {}
for describe in seqdic:
    sequence = seqdic[describe]
    protein = ''
    prolen = len(sequence)//3
    for i in range(prolen):
        tri = sequence[i*3:i*3+3]
        if tri not in codontable:
            sys.stderr.write('Codon Error: ' + tri + '\n')
        else:
            ac = codontable[tri]
            protein = protein + ac
    sys.stdout.write(describe + protein + '\n')