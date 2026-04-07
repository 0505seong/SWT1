#7785.py
people = set()
n = int(input())
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        people.add(name)
    else:
        people.discard(name)

people = sorted(people, reverse=True) 
for name in people:
    print(name)