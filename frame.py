#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

#single loop #IMUGLYANDIAMPROUD
print('single loop')
for i in range (0, len(dna)):
    if i in range (0, len(dna), 3):
        frame = 0
    elif i in range (1, len(dna), 3):
        frame = 1
    else:
        frame = 2
    print(i, frame, dna[i])

#modulus, %, is the remainder after division
print('my smart ass dad wanted to try after cringing at my code')
for i in range (0, len(dna)):
   print(i, i % 3, dna[i])  

#nested loops
print('nested loops')
for i in range (0, len(dna), 3):
    for j in range (0,3):
        frame = j
        position = i+j
        letter = dna[i+j]
        print(position, frame, letter)


"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""