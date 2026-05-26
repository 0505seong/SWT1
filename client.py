import sys,socket

HOST = '10.103.72.248'
PORT = 8888

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

while True:
    user_input = input('Message')
    s.send(user_input.encode('utf-8'))

    echo = s.recv(1024)
    if not echo: break
    print('Echo from Server: ' +echo.decode('utf-8'))
s.close()