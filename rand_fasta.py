#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that finds creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line: python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

def rand_dna(len_seq, a, c, g, t):
    dnaseq = []
    for i in range(len_seq):
        r = random.random()
        if   r < a:     dnaseq.append('A')
        elif r < a+c:   dnaseq.append('C')
        elif r < a+c+g: dnaseq.append('G')
        else:           dnaseq.append('T')
        
    return ''.join(dnaseq)
    
count = int(sys.argv[1])
min = int(sys.argv[2])
max = int(sys.argv[3])
a = float(sys.argv[4])
c = float(sys.argv[5])
g = float(sys.argv[6])
t = float(sys.argv[7])

for i in range(count):
    x = random.randint(min, max)
    dna = rand_dna(x, a, c, g, t)
    print(f'>{i}')
    print(dna)

"""
def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()
"""
"""

"""
