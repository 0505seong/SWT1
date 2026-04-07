#16414.py
import sys

def solve():

    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    K = int(input_data[0])  
    
 
    clicks = {}
    for i in range(2, len(input_data)):
        clicks[input_data[i]] = i
    sorted_students = sorted(clicks.keys(), key=lambda x: clicks[x])
    
    for student_id in sorted_students[:K]:
        print(student_id)

if __name__ == '__main__':
    solve()