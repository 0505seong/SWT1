import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = input().strip()
    stack = []
    is_vps = True
    
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_vps = False
                break
            stack.pop()
            
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
