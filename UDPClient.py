import socket
from threading import Thread


def wait_response(s):
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            data = data.decode('utf-8')
            print("Received from server: " + data)




def main():
    host = ''
    port = 5000
    server = ('10.6.161.65', 8880)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    d = Thread(target=wait_response, args=(s,))
    d.setDaemon(True)
    d.start()

    message = raw_input("\n->")

    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        message = raw_input("->")
    s.close()

if __name__ == '__main__':
        main()
