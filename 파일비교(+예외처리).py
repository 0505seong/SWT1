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

def compare_dir(dir1,dir2):
    entry1 = {e.name: e for e in os.scandir(dir1)}
    entry2 = {e.name: e for e in os.scandir(dir2)}

    if set(entry1.keys()) != set(entry2.keys()):
        return '다름'
    
    for name in entry1:
        e1= entry1[name].stat().st_size
        e2= entry2[name].stat().st_size
        if e1 != e2:
            return '다름'
        

    return '같음'


a = get_dir('C:/Users/USER/Desktop')
b = get_dir('C:/Users/USER/Desktop')

print(compare_dir(a,b))


