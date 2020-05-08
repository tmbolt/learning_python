#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

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


def kd(seq):
    sum = 0
    for aa in seq:
        if aa == 'I': sum += 4.5
        if aa == 'V': sum += 4.2
        if aa == 'L': sum += 3.8
        if aa == 'F': sum += 2.8
        if aa == 'C': sum += 2.5
        if aa == 'M': sum += 1.9
        if aa == 'A': sum += 1.8
        if aa == 'G': sum += -0.4
        if aa == 'T': sum += -0.7
        if aa == 'S': sum += -0.8
        if aa == 'W': sum += -0.9
        if aa == 'Y': sum += -1.3
        if aa == 'P': sum += -1.6
        if aa == 'H': sum += -3.2
        if aa == 'E': sum += -3.5
        if aa == 'Q': sum += -3.5
        if aa == 'D': sum += -3.5
        if aa == 'N': sum += -3.5
        if aa == 'K': sum += -3.9
        if aa == 'R': sum += -4.5 
    return sum/len(seq)    
        


def hydro(seq, win, hyd):
    #check every window
    for i in range(len(seq) - win + 1):
        ss = seq[i:i+win]
        if 'P' not in ss and kd(ss) > hyd: return True
    #once all checked if not true then 
    return False

 
for name, seq in read_fasta(sys.argv[1]):
    nterm = seq[:30]
    cterm = seq[30:]
    if hydro(nterm, 8, 2.5) and hydro(cterm, 11, 2):
        print(name)

#if n term has the signal and if the c term has hydrophobe, then print the name 

"""
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
