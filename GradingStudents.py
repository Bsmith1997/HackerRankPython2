#!/bin/python

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            grade = grade + 5 - (grade % 5)
        newGrades.append(grade)
    return newGrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
