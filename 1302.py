#1302.py
from collections import Counter

n = int(input())
books = [input() for _ in range(n)]

c = Counter(books)
max_count = max(c.values())

# 가장 많이 팔린 책 중 사전순으로 가장 앞선 것
candidates = [b for b, cnt in c.items() if cnt == max_count]
print(sorted(candidates)[0])