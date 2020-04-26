#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
for line in fileinput.input():
	if line.startswith('#'): continue 
	line = line.rstrip() 
	data.append(float(line))
    
count = 0
sum = 0
for i in data:
    count += 1
    sum += i
mean = sum/count

s = 0
for i in data:
    s += (i - mean) ** 2
sd = (s / count) ** 0.5 

data.sort()
min = data[0]
max = data[-1]

if count % 2 == 0:
    m = int((len(data)/2) - 1)
    n = int(len(data)/2)
    med = (data[m] + data[n]) / 2
else:
    m = int((len(data)/2) - 0.5)
    med = data[m]

print(f'Count: {count}')
print(f'Minimum: {min}')
print(f'Maximum: {max}')
print(f'Mean: {mean}')
print(f'Std. dev: {sd:.3f}')
print(f'Median: {med}')


"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
