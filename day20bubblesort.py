#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
#
switches = 0
i = 0
s = 0
while i < n:
    while s < n-1:
        if a[s] < a[s+1]:
            s += 1
        elif a[s] > a[s+1]:
            a[s], a[s+1] = a[s+1], a[s]
            switches += 1
            s = 0
    i += 1
#print(a)
print("Array is sorted in " + str(switches) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))
