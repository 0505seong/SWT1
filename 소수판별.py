import time

n = int(input('자연수 넣어라'))

start_time=time.time()
for i in range(2,n):
    if n%i == 0:
        print(f'{n}은 {i}로 나누어 떨어집니다')
        break
else:
    print(f'{n}은 소수입니다')

print('걸린 시간: ',time.time()-start_time)