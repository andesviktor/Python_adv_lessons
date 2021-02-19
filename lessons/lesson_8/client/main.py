import socket,sys,time
from msgutils import send_msg,recv_msg
# sock = socket.socket()
#
# try:
#     sock.connect(('localhost',12345))
# except ConnectionRefusedError:
#     print('No found server!')
#     exit()
#
#
#
#
# sock.close()


with socket.socket() as sock:
    sock.connect(('localhost',12345))
    send_msg(sock,'Hello, server !'.encode(encoding='866'))
    print(recv_msg(sock).decode(encoding='866'))

    data
    with open('input.txt') as f:
        data += ''.join(f.readlines())

    send_msg(sock,data.encode(encoding='866'))
    print(recv_msg(sock).decode(encoding='866'))
