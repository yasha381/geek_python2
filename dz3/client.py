from socket import *
import json
import argparse

parser = argparse.ArgumentParser(description='Client parser.')

parser.add_argument('address', type=str, help='Address value')
parser.add_argument('port', type=int, help='Port value')

args = parser.parse_args()

if args.address:
    address = args.address
else:
    address = 'localhost'
    
if args.port:
    port = args.port
else:
    port = 7777

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((address, port))
    msg = {'action': 'authenticate', 'user': {'account_name': 'test', 'password': 'test'}}
    msg_str = json.dumps(msg)
    s.send(msg_str.encode('utf-8'))
    data = s.recv(1000000)
    print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной', len(data))
