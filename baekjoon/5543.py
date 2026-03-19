#백준 5543
a_burgar= int(input())
b_burgar= int(input())
c_burgar= int(input())
coke= int(input())
sidar= int(input())

burgar= 0
water= 0

if a_burgar <= b_burgar and a_burgar <= c_burgar:
  burgar= a_burgar
elif b_burgar <= a_burgar and b_burgar <= c_burgar:
  burgar= b_burgar
else:
  burgar= c_burgar

if coke <= sidar:
  water= coke
else:
  water= sidar

print(burgar+water-50)
