#!/bin/python
from __future__ import division
import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    print format(len([x for x in arr if x > 0])/n, ".6f")
    print format(len([x for x in arr if x < 0])/n, ".6f")
    print format(len([x for x in arr if x == 0])/n, ".6f")

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
