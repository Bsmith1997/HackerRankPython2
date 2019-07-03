import itertools

A = list(map(int, raw_input().split()))
B = list(map(int, raw_input().split()))

for i in itertools.product(A, B):
    print i,
