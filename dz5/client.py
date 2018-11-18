from socket import *
import json
import argparse
import logging
from log import client_log_config

logger = logging.getLogger('client_log')

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def start(self):
        logger.info('Подключение к серверу')
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.address, self.port))
                logger.info('Подключение к серверу выполнено')
                msg = {'action': 'authenticate', 'user': {'account_name': 'test', 'password': 'test'}}
                msg_str = json.dumps(msg)
                s.send(msg_str.encode('utf-8')) 
                logger.info('Сообщение отправлено')
                data = s.recv(1000000)
                print('Сообщение от сервера: ', data.decode('utf-8'))
                logger.info('Сообщение от сервера принято')
            except ConnectionRefusedError:
                logger.warning('Сервер отключен!')


def main():
    logger.info('Старт приложения')
    
    parser = argparse.ArgumentParser(description='Client parser.')
    parser.add_argument('address', type=str, default='localhost', help='Address value')
    parser.add_argument('port', type=int, default=7777, help='Port value')
    args = parser.parse_args()

    root = Client(args.address, args.port)
    root.start()
    
if __name__ == "__main__":    
    main()
