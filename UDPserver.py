import socket
from threading import Thread


def wait_response(s, c_a):
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            c_a.addr = addr
            data = data.decode('utf-8')
            print("Recived from client: " + data)


class Upd_client_address_container(object):
    addr = ''


def main():
    host = "10.6.161.65"
    port = 8880

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    connection_addr = Upd_client_address_container()

    d = Thread(target=wait_response, args=(s, connection_addr,))
    d.deamon = True
    d.start()

    print("Server started")
    message = 'Connection with server established'
    while message != 'q':
        if connection_addr.addr:
            s.sendto(message.encode('utf-8'), connection_addr.addr)
            message = raw_input("->")
    s.close()


if __name__ == "__main__":
    main()
