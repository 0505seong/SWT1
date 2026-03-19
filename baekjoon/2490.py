a,b,c,d= map(int, input().split())
f,g,h,i= map(int, input().split())
k,l,m,n= map(int, input().split())
hap_1 = a+b+c+d
hap_2 = f+g+h+i
hap_3 = k+l+m+n

result = ['E','A','B','C','D']

print(result[4-hap_1])
print(result[4-hap_2])
print(result[4-hap_3])
