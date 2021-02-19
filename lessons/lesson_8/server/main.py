import socket
from msgutils import send_msg, recv_msg

with socket.socket() as sock:
    sock.bind(('', 12345))
    sock.listen(1)
    conn, addr = sock.accept()

    print(f'COnnected: {conn}')

    print(recv_msg(sock).decode(encoding='866'))
    send_msg(sock, 'Hello, client !'.encode(encoding='866'))


# sock = socket.socket()
# sock.bind(('', 12345))
#
# sock.listen(1)
#
# conn, _ = sock.accept()
#
# print(f'Connected: {_}')
#
# data_all = ''
# while True:
#     data = conn.recv(10).decode(encoding='utf-8')
#     if not data:
#         break
#
#     data_all += data
# conn.close()
# print(data_all)