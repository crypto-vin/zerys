import socket
import threading
import sys
import csv

class Server:
    def __init__(self):
        self.HEADER = 64
        port = 3389
        self.PORT = port
        #self.SERVER = '127.0.0.1'
        self.SERVER = ''
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!DISCONNECT'
        self.user_list = ['Admin', 'Martin']
        self.passwords = ['Vin2am@254', '@Martin1111']
        self.phones = ['+254712897106 +254713136333', 
                       '+254712618137']

        self.allowed_accs = ['topfreelancer87@yahoo.com vinmunyalo14@gmail.com',
                             'topfreelancer87@yahoo.com']

        f = open("data.csv", 'w', newline='')
        writer = csv.writer(f)
        parameters = (self.user_list, self.passwords, self.phones, self.allowed_accs)
        for parameter in parameters:
            writer.writerow(parameter)
        print('Data writen!')

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
    
    def strip_msg(self, msg):
        half = msg.find(' ')
        username = (msg[: half ])
        password = (msg[half + 1 :])
        self.username, self.password = username, password

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected")

        connected = True
        while connected:
            account = False
            passwd = False
            try:
                msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            except:
                break
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    sys.exit()
                    
                print(f"[{addr}] {msg}")
            
                self.strip_msg(msg)

            try:
                if self.username in self.user_list:
                    account = True

                if self.password in self.passwords:
                    passwd = True

                if account:
                    ind = self.user_list.index(self.username)
                    print(f'{self.username} exists')
                    if self.password == self.passwords[ind]:
                        conn.send(f'exists, {self.allowed_accs[ind]}- {self.phones[ind]}> {self.username}'.encode(self.FORMAT))
                        return 'exists'
                        break             
                    else:
                        conn.send('incorrect_pwd'.encode(self.FORMAT))
                        return 'incorrect_pwd'
                        break
                else:
                    print(f'{self.username} does not exist')
                    conn.send('null'.encode(self.FORMAT))
                    break

            except Exception as err:
                print(err)
                break
                
        conn.close()

    def start(self):
        self.server.listen()
        print(f'[LISTENING] Server is listening on {self.SERVER}')
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def run(self):
        print('[STARTING] server is starting... ')
        self.start()

if __name__ == "__main__":
    app = Server()
    app.run()
    sys.exit(app.exec_())