import json
from typing import Any, Dict
from socket import *
import argparse

parser = argparse.ArgumentParser(description='Server parser.')


parser.add_argument('-a', '--address', type=str, required=False, action='store', help='Set address')
parser.add_argument('-p', '--port', type=int, required=False, action='store', help='Set port')

args = parser.parse_args()

if args.address:
    address = args.address
else:
    address = ''
    
if args.port:
    port = args.port
else:
    port = 7777
    
def handle_authenticate(request):
    if request['user'] == {'account_name': 'test', 'password': 'test'}:
        return {'response': 200}

    return {'response': 402, 'error': 'wrong password'}

mapping = {
    'authenticate': handle_authenticate
}

def handler(request: Dict[str, object]):
    print(f'Client sent {request}')
    responce = mapping[request['action']](request)
    print(f'Response {request}')
    return responce

def check(data):
    try:
        json.loads(data, encoding='utf-8')
        return True
    except json.decoder.JSONDecodeError:
        print('Неверный формат ссообщения')
        return False

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((address, port))
    s.listen(1)

    while True:
        client, addr = s.accept()
        with client:
            data_b = client.recv(1000000)
            if check(data_b):
                data = json.loads(data_b, encoding='utf-8')
                responce = handler(data)
                client.send(json.dumps(responce).encode('utf-8'))
