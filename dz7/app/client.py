from socket import *
import json
import argparse
import logging
import inspect
from socket import *
import time
try:
    from context import log
except ImportError:
    from .context import log

logger = logging.getLogger('client_log')

enable_log = True

def log(func):
    if enable_log:
        def wrapper(*args, **kwargs):
            try:
                logger.info("Вызов функции %s с аргументами %s, %s\n" % (func.__name__, args, kwargs))
            except:
                parent = inspect.stack()[1][3]
                logger.info("Функция %s с аргументами %s, %s\n вызвана из функции %s" % (func.__name__, args, kwargs, parent))
            return func(*args, **kwargs)
                
        return wrapper
    else:
        return func

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.mapping = {
                'auth': self.authenticate,
                'send': self.send_msg,
                'recieve': self.recieve_msg
                
            }
        

    @log
    def authenticate(self):
        logger.info('Подключение к серверу')
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.address, self.port))
                logger.info('Подключение к серверу выполнено')
                msg = {'action': 'authenticate',
                       'user': {'account_name': 'test', 'password': 'test'}}
                msg_str = json.dumps(msg)
                s.send(msg_str.encode('utf-8'))
                logger.info('Сообщение отправлено')
                data = s.recv(1000000)
                print('Сообщение от сервера: ', data.decode('utf-8'))
                logger.info('Сообщение от сервера принято')
            except ConnectionRefusedError:
                logger.warning('Сервер отключен!')

    @log
    def send_msg(self):
        logger.info('Подключение к серверу')
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.address, self.port))
                logger.info('Подключение к серверу выполнено')
                while True:
                    msg = ""
                    msg = input('Ваше сообщение: ')
                    if msg == 'exit':
                        break
                    s.send(msg.encode('ascii'))
                    data = s.recv(1024).decode('ascii')
                    print(data)
            except ConnectionRefusedError:
                logger.warning('Сервер отключен!')
    @log
    def recieve_msg(self):
        logger.info('Подключение к серверу')
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((self.address, self.port))
                logger.info('Подключение к серверу выполнено')
                while True:
                    data = s.recv(1024).decode('ascii')
                    print(data)
            except ConnectionRefusedError:
                logger.warning('Сервер отключен!')
            


def main():
    logger.info('Старт приложения')

    parser = argparse.ArgumentParser(description='Client parser.')
    parser.add_argument('func', type=str, help='Choose function')
    parser.add_argument('address', type=str, default='localhost',
                        help='Address value')
    parser.add_argument('port', type=int, default=7777, help='Port value')
    args = parser.parse_args()

    root = Client(args.address, args.port)
    root.mapping[args.func]()

if __name__ == "__main__":
    main()
