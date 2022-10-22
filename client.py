import socket
import csv

class Client:
    def __init__(self):
        self.HEADER = 64
        self.PORT = 3389
        self.SERVER = '34.70.106.233'
        #self.SERVER = '127.0.0.1'
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!DISCONNECT'
        self.ADDR = (self.SERVER, self.PORT)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send_msg(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        try:
            received_msg = self.client.recv(2040).decode(self.FORMAT)
        except:
            print('No message received')
        else:
            self.received_msg = received_msg
            print(f'Received: {received_msg}')

    # Get each message from received text
    def decode_msgs(self, msg):
        boundary = msg.find(',')
        boundary2 = msg.find('-')
        boundary3 = msg.find('>')
        boundary4 = msg.find('<')
        self.msg1 = (msg[: boundary ])
        self.msg2 = (msg[boundary + 2 : boundary2])
        self.msg3 = (msg[boundary2 + 2 : boundary3])
        self.msg4 = (msg[boundary3 + 2 : boundary4])
        self.msg5 = (msg[boundary4 + 2 :])
    
    # Get parameters from received message
    def get_parameters(self, msg2, msg3):
        print('Getting parameters')
        
        accounts = msg2.split()
        self.account_list = accounts
        print(self.account_list)

        phones = msg3.split()
        self.phone_list = phones
        print(self.phone_list)

 
        with open('bin/params.csv', 'w', newline= '') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(self.msg4.split())
            writer.writerow(self.account_list)
            writer.writerow(self.phone_list)
            print('Rows written')
    
    #Run the client side
    def run(self, username, password):
        self.send_msg(f'{username} {password}')
        if self.received_msg != 'incorrect_pwd' and self.received_msg != 'null':
            try:
                self.decode_msgs(self.received_msg)
            except:
                print('Can\'t decode message')

            if self.msg1:
                self.get_parameters(self.msg2, self.msg3)
                return 'exists'

        elif self.received_msg=='incorrect_pwd':
            return 'incorrect_pwd'

        elif self.received_msg=='null':
            return 'null'
            


if __name__ == "__main__":
    app = Client()
    app.run('Admin', 'Vin2am@254')