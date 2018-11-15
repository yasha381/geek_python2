
import json
from typing import Any, Dict
from socket import *
import argparse

class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.mapping = {
            'authenticate': self.handle_authenticate
        }

    
    def handle_authenticate(self, request):
        if request['user'] == {'account_name': 'test', 'password': 'test'}:
            return {'response': 200}

        return {'response': 402, 'error': 'wrong password'}


    def handler(self, request: Dict[str, object]):
        print(f'Client sent {request}')
        responce = self.mapping[request['action']](request)
        print(f'Response {request}')
        return responce

    def validate_request(self, data):
        try:
            msg = json.loads(data, encoding='utf-8')
            responce = self.handler(msg)
            return json.dumps(responce).encode('utf-8')
        except json.decoder.JSONDecodeError:
            print('Неверный формат ссообщения')
            return b'Incorrect format'

    def start(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind((self.address, self.port))
            s.listen(1)

            while True:
                client, addr = s.accept()
                with client:
                    data_b = client.recv(1000000)
                    client.send(self.validate_request(data_b))

def main():
    parser = argparse.ArgumentParser(description='Server parser.')
    parser.add_argument('-a', '--address', type=str, required=False, action='store', default='', help='Set address')
    parser.add_argument('-p', '--port', type=int, required=False, action='store', default=7777, help='Set port')
    args = parser.parse_args()

    myserver = Server(args.address, args.port)
    myserver.start()

    
if __name__ == "__main__":    
    main()
  
                
