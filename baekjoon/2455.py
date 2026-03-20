d_1,u_1=map(int,input().split())
d_2,u_2=map(int,input().split())
d_3,u_3=map(int,input().split())
d_4,u_4=map(int,input().split())

p_1 = u_1+d_1
p_2 = p_1-d_2+u_2
p_3= p_2-d_3+u_3
p_4= p_3-d_4+u_4

p=[p_1,p_2,p_3,p_4]

print(max(p))
