import sys
octal_str = sys.stdin.readline().strip()

if octal_str == '0':
    print('0')
else:
    octal_to_bin = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }

    res = "".join([octal_to_bin[digit] for digit in octal_str])
    
    print(res.lstrip('0'))
