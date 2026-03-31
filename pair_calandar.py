from itertools import accumulate

M = input('월을 입력해주세요: ')
month = M + '월'
print(f'{month:>13}')
print('일 월 화 수 목 금 토')
M = int(M)

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
datesum = list(accumulate(date))

# 1월 1일을 목요일(4)로 가정 (2026년 기준)
start_day = 4 

# 해당 월의 1일 요일 계산
if M == 1:
    day = start_day
else:
    day = (start_day + datesum[M-2]) % 7

# 1. 공백 출력: 1일의 요일(day)만큼 빈칸을 띄웁니다.
for i in range(day):
    print('  ', end=' ')

# 2. 날짜 출력
for i in range(1, date[M-1] + 1):
    print(f'{i:>2}', end=' ')
    day += 1 # 날짜를 하나 적을 때마다 요일 카운트 증가
    
    if day % 7 == 0: # 토요일(7, 14, 21...)이 되면 줄바꿈
        print()
