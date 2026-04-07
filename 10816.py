#10816.py
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

count_dict = Counter(cards)


print(*(count_dict[t] if t in count_dict else 0 for t in targets))
