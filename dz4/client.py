from socket import *
import json
import argparse

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def start(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.address, self.port))
                msg = {'action': 'authenticate', 'user': {'account_name': 'test', 'password': 'test'}}
                msg_str = json.dumps(msg)
                s.send(msg_str.encode('utf-8'))
                data = s.recv(1000000)
                print('Сообщение от сервера: ', data.decode('utf-8'))
            except:
                print('Сервер отключен')


def main():
    parser = argparse.ArgumentParser(description='Client parser.')
    parser.add_argument('address', type=str, default='localhost', help='Address value')
    parser.add_argument('port', type=int, default=7777, help='Port value')
    args = parser.parse_args()

    root = Client(args.address, args.port)
    root.start()
    
if __name__ == "__main__":    
    main()
