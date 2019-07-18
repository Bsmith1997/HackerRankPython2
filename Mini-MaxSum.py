#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minSum = sum(arr) - arr[len(arr) - 1]
    maxSum = sum(arr) - arr[0]

    print minSum, maxSum

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
