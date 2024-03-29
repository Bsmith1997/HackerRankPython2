#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aliceScore = 0
    bobScore= 0
    for x in range(3):
        if a[x] > b[x]:
            aliceScore += 1
        elif b[x] > a[x]:
            bobScore += 1
    result = (aliceScore, bobScore)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
