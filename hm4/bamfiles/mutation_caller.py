import pysam
import numpy as np
import math
from itertools import chain
import argparse


G = ['AA', 'CC', 'GG', 'TT', 'AC' ,'AG', 'AT', 'CG', 'CT', 'GT']

def likelihood(b, G):
    probability = []
    for g in G:
        probability.append(prob(b, g))
    return probability
    
def prob(b, g):
    e = 0.1
    if b == g[0]:
        if b == g[1]:
            return 0.5*(1-e + 1-e)
        else:
            return 0.5*(1-e + e/3)
    else:
        if b == g[1]:
            return 0.5*(e/3 + 1-e)
        else:
            return 0.5*(e/3+e/3)

parser = argparse.ArgumentParser()
parser.add_argument('-n', default='./normal.bam')
parser.add_argument('-c', default='./cancer.bam')
args = parser.parse_args([])
print(args.n, args.c)
normalsam = pysam.AlignmentFile(args.n, "rb")
cancersam = pysam.AlignmentFile(args.c, "rb")

for (pileupcolumn_nor, pileupcolumn_can) in zip(normalsam.pileup(), cancersam.pileup()):

    if pileupcolumn_nor.n < 20 or pileupcolumn_can.n < 20:
        print('Insufficient coverage at position', pileupcolumn_nor.pos)
    else:
        print ("\ncoverage at base %s = %s" %(pileupcolumn_nor.pos, pileupcolumn_nor.n))
        lk_nor = []
        lk_can = []
        
        for pileupread_nor in pileupcolumn_nor.pileups:
            if not pileupread_nor.is_del and not pileupread_nor.is_refskip:
                b = pileupread_nor.alignment.query_sequence[pileupread_nor.query_position]
                lk_nor.append(likelihood(b, G))
        
        for pileupread_can in pileupcolumn_can.pileups:
            if not pileupread_can.is_del and not pileupread_can.is_refskip:
                c = pileupread_can.alignment.query_sequence[pileupread_can.query_position]
                lk_can.append(likelihood(c, G))
    
        lk_nor_prob = np.prod(lk_nor, axis = 0)
        lk_nor_list = lk_nor_prob.tolist()
        
        
        lk_can_prob = np.prod(lk_can, axis = 0)
        lk_can_list = lk_can_prob.tolist()

        if math.log(max(lk_nor_list)) < -50:
            print('Position {} has ambiguous genotype'.format(pileupcolumn_nor.pos))
        else:
            if math.log(lk_can_list[lk_nor_list.index(max(lk_nor_list))]) < -75:
                print('Position {} has a candidate somatic mutation (Log-likelihood={})'.format(pileupcolumn_nor.pos, round(math.log(lk_can_list[lk_nor_list.index(max(lk_nor_list))]), 6)))
                
normalsam.close()
cancersam.close()
