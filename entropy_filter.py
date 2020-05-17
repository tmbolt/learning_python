#!/usr/bin/env python3

# Write a program that masks areas of low complexity sequence
# Use argparse for command line arguments (see example below)
# Use read_fasta() from biotools.py

import argparse
import biotools as bt
import math

# setup
parser = argparse.ArgumentParser(
	description='Brief description of program.')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='the fasta file')
# optional arguments with default parameters
parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='optional integer argument [%(default)i]')
parser.add_argument('--threshold', required=False, type=float, default=1.1,
	metavar='<float>', help='optional floating point argument [%(default).3f]')
# switches
parser.add_argument('--lowercase', action='store_true',
	help='on/off switch')
# finalization
arg = parser.parse_args()

    
def entropy(seq):
	a, c, g, t = 0, 0, 0, 0
	for nt in seq:
		if   nt == 'A': a += 1
		elif nt == 'C': c += 1
		elif nt == 'G': g += 1
		elif nt == 'T': t += 1
	total = a + c + g + t
	if total == 0: return None
	pa = a / total
	pc = c / total
	pg = g / total
	pt = t / total
	
	p = []
	if pa > 0: p.append(pa)
	if pc > 0: p.append(pc)
	if pg > 0: p.append(pg)
	if pt > 0: p.append(pt)
	
	sum = 0
	h = 0
	for i in range(len(p)):
		assert(p[i] > 0)
		h += p[i] * math.log2(p[i])
		sum += p[i]
	assert(math.isclose(sum, 1.0))
	return -h


for name, seq in bt.read_fasta(arg.file):
	dna = list(seq)
	for i in range(len(seq) - arg.window + 1):
		ss = seq[i:i+arg.window]
		if entropy(ss) < arg.threshold: 
			for j in range(i, i + arg.window):
				if arg.lowercase:
					if   dna[j] == 'A': dna[j] = 'a'
					elif dna[j] == 'C': dna[j] = 'c'
					elif dna[j] == 'G': dna[j] = 'g'
					elif dna[j] == 'T': dna[j] = 't'
				else:
					dna[j] = 'N'
	print(f'>{name}')
	print(''.join(dna))
	
#now do option that will make N as the lowercase acgt


"""
python3 entropy_filter.py --help
usage: entropy_filter.py [-h] --input <path> [--window <int>]
                         [--threshold <float>] [--lowercase]

Low complexity sequence masker.

optional arguments:
  -h, --help           show this help message and exit
  --input <path>       fasta file
  --window <int>       optional integer argument [15]
  --threshold <float>  entropy threshold [1.100000]
  --lowercase          report lower case instead of N


python3 entropy_filter.py --input genome.fa.gz | head -20
>I
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAAAAATTGAGATAAGAAAACATTTTACTTTTTCAAAATTGTTTTCATGC
TAAATTCAAAACNNNNNNNNNNNNNNNAAGCTTCTAGATATTTGGCGGGTACCTCTAATT
TTGCCTGCCTGCCAACCTATATGCTCCTGTGTTTAGGCCTAATACTAAGCCTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAAAAGAATATGGTAGCTACAGAAACGGTAGTACACTCTTCTGNNNNNNNNNNNNNN
NTGCAATTTTTATAGCTAGGGCACTTTTTGTCTGCCCAAATATAGGCAACCAAAAATAAT
TGCCAAGTTTTTAATGATTTGTTGCATATTGAAAAAAACANNNNNNNNNNNNNNNGAAAT
GAATATCGTAGCTACAGAAACGGTTGTGCACTCATCTGAAANNNNNNNNNNNNNNNNNNN
NNGCACTTTGTGCAGAATTCTTGATTCTTGATTCTTGCAGAAATTTGCAAGAAAATTCGC
"""
