from socket import socket
default_header_size = 10
encoding = '866'

def send_msg(conn:socket,msg:bytes,header_size: int = default_header_size) -> bool:
    size_msg = f'{len(msg):{header_size}}'

    if conn.send(size_msg.encode(encoding=encoding)) != header_size:
        return False

    if conn.send(msg) != len(msg):
        print('ERROR: can"t send message')
        return False

    return True

def recv_msg(conn: socket, header_size: int = default_header_size, size_pack: int = default_header_size):
    data = conn.recv(header_size)

    if not data:
        return False

    data = data.decode(encoding=encoding)
    if not data.isnumeric():
        return False

    size_msg = int(data)
    msg = b''

    while True:
        if size_msg <= size_pack:
            data = conn.recv(size_msg)
            if not data:
                return False

            msg += data
            break

        data = conn.recv(size_pack)
        if not data:
            return False

        size_msg = size_pack
        msg += data
