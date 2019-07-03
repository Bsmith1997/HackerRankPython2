#!/bin/python

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    return ' '.join(map(string.capitalize, s.split(' ')))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
