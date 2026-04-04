N = int(input())

for _ in range(N):
    ox_list = input()
    total_score = 0
    current_score = 0 
    
    for result in ox_list:
        if result == 'O':
            current_score += 1     
            total_score += current_score
        else:
            current_score = 0     
            
    print(total_score)
