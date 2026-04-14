N = int(input())
han =0
for i in range(1,N+1):
    if i < 100:
        han +=1
    else:
        R = list(str(i))
        if int(R[2])-int(R[1]) == int(R[1])-int(R[0]):
            han+=1
print(han)
