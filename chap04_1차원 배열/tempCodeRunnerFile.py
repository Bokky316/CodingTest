from collections import Counter
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
counter = Counter(array)
v = int(sys.stdin.readline())
print(counter[v])
