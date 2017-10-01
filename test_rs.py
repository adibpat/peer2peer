#########################################
#           RS Server File              #
#########################################
import socket

class RfpServer(object):
    PORT = 65423
    HOST = ''
    cookie_list = []
    RSconnections = []
    
    def __init__(self):
        """ Initialize socket"""
        self.listen_socket = listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((self.HOST, self.PORT))
        listen_socket.listen(5)

    def generate_cookie(self):
        cl = len(self.cookie_list)
        for cookie in range(1,cl+1):
            if cookie not in self.cookie_list:
                self.cookie_list.append(cookie)
                return cookie
        return (cl+1)
        
    def serve(self):
        client_connection, client_address = self.listen_socket.accept()
        while True:
            request = client_connection.recv(1024)
            rlist = request.split()
            if not request:
                break
            elif rlist[0] == 'REGISTER':
                print 'Received', request
                cookie = self.generate_cookie()
                param = ['host','cookie']
                keys = [client_address, cookie]
                self.RSconnections.append(dict(zip(param,keys)))
                print 'RS connection list: ',self.RSconnections
                client_connection.send(str(cookie))
                print 'Sent cookie ',cookie
            else:
                print 'Received ',request

if __name__ == '__main__':
    rs = RfpServer()
    rs.serve()
