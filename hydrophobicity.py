#!/usr/bin/env python3

# Write a program that computes hydrophobicity in a window
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

import argparse 
import biotools 

# setup
parser = argparse.ArgumentParser(
	description='hydrophobicity calculator')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='fasta file')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='window size')
parser.add_argument('--method', required=True, type=int,
	metavar='<int>', help='calculation method: int_scale [0], kd [1]')
# finalization
arg = parser.parse_args()

is_scale = { 'A': 0.17,'R':0.81,'N':0.42,'D': 1.23,'C':-0.24,
             'Q': 0.58,'E':2.02,'G':0.01,'H': 0.96,'I':-0.31,
             'L':-0.56,'K':0.99,'M':-0.23,'F':-1.13,'P':0.45,
             'S': 0.13,'T':0.14,'W':-1.85,'Y':-0.94,'V': 0.07 }

kd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }
	   
def hyd(pro, method):
	scale = None
	if   method == 0: scale = is_scale
	elif method == 1: scale = kd
	#else: make it fail
	h = 0
	for aa in pro:
		if aa in scale:
			h += scale[aa]
	return h

for name, pro in biotools.read_fasta(arg.file):
	pro = pro.upper()
	if pro[-1] == '*': pro = pro[0:-1]
	for i in range(0, len(pro) - arg.window + 1):
		win = pro[i:i+arg.window]
		print(i, hyd(win, arg.method))



"""
python3 hydrophobicity.py --input proteins.fasta.gz --window 11 --method kd
"""
