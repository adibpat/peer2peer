#########################################
#              Peer File                #
#########################################
import socket
import time

class peerSocket(object):
    PORT = 65423
    cookie = ''

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_rs(self,server_address):
        self.client_socket.connect((server_address,65423))        

    def register_rs(self):
        data = 'REGISTER'
        self.client_socket.send(data)
        print 'Sent ',data
        self.cookie = self.client_socket.recv(1024)

    def keep_alive_rs(self):
        ka = 'KEEPALIVE ' + self.cookie
        self.client_socket.send(ka)

if __name__ == '__main__':
    cs = peerSocket()
    cs.connect_rs('localhost')
    cs.register_rs()
    #client_socket.cookie = client_socket.client_socket.recv(512)
    print cs.cookie
    while(1):
        time.sleep(5)
        cs.keep_alive_rs()
