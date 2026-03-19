#오전오후
import datetime
now= datetime.datetime.now()

HOUR= now.hour
if HOUR > 12:
    print('지금은 오후입니다')
else:
    print('지금은 오전입니다')