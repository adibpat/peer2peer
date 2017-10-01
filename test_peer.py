#!/usr/bin/python

#########################################
#              Peer File                #
#########################################
import socket
import time

class peerSocket(object):
    PORT = 65423
    cookie = ''
    APL = []
    
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

    def get_act_peer(self):
        ap = 'PQuery'
        self.APL = []
        self.client_socket.send(ap)
        while(True):
           rdata = self.client_socket.recv(1024)
           data = rdata.split()
           print data
           if not rdata:
               break
           elif len(data) == 2:
               print rdata
           elif len(data) == 3:
               print 'Received full list'
               break

if __name__ == '__main__':
    cs = peerSocket()
    cs.connect_rs('localhost')
    cs.register_rs()
    #client_socket.cookie = client_socket.client_socket.recv(512)
    print cs.cookie
    cs.get_act_peer()    
    while(1):
        time.sleep(5)
        cs.keep_alive_rs()

        
