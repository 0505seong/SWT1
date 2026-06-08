#기말고사 버전
import os

def get_dir(prompt):
    while True:
        path = input(prompt)

        if not os.path.exists(path):
            print('잘못 입력하였다')
        elif not os.path.isdir(path):
            print('디렉토리가 아니다')
        else:
            return path

def compare_dir(dir1, dir2):
    try:
        entry1 = {}
        with os.scandir(dir1) as it:
            for e in it:
                entry1[e.name] = e

        entry2 = {}
        with os.scandir(dir2) as it:
            for e in it:
                entry2[e.name] = e

    except PermissionError:
        print('접근 권한이 없습니다')
        return '다름'

    if set(entry1.keys()) != set(entry2.keys()):
        return '다름'

    for name in entry1:
        e1 = entry1[name]
        e2 = entry2[name]

        if e1.is_dir() and e2.is_dir():
            if compare_dir(e1.path, e2.path) == '다름':
                return '다름'
        elif e1.is_file() and e2.is_file():
            if e1.stat().st_size != e2.stat().st_size:
                return '다름'
        else:
            pass

    return '같음'


a = get_dir('첫 번째 디렉토리: ')
b = get_dir('두 번째 디렉토리: ')

print(compare_dir(a, b))
