import json
from typing import Any, Dict
from socket import *
import argparse
import logging
import inspect
import select
import time

try:
    from context import log
except ImportError:
    from .context import log
    
logger = logging.getLogger('server_log')

enable_log = True

def log(func):
    if enable_log:
        def wrapper(*args, **kwargs):
            try:
                parent = inspect.stack()[1][3]
                logger.info("Функция %s с аргументами %s, %s\n вызвана из функции %s" % (func.__name__, args, kwargs, parent))
            except:
                logger.info("Вызов функции %s с аргументами %s, %s\n" % (func.__name__, args, kwargs))
           
            return func(*args, **kwargs)
                
        return wrapper
    else:
        return func

class Server:
    @log
    def __init__(self, address, port):
        self.address = address
        self.port = port
        
        self.full_address = [address, port]
        self.mapping = {
            'authenticate': self.handle_authenticate,
        }

    @log
    def handle_authenticate(self, request):
        logger.info('Проверка аутентификации')
        if request['user'] == {'account_name': 'test', 'password': 'test'}:
            return {'response': 200}

        return {'response': 402, 'error': 'wrong password'}

    @log
    def handler(self, request: Dict[str, object]):
        logger.info('Производится обработка сообщения')
        print(f'Client sent {request}')
        responce = self.mapping[request['action']](request)
        print(f'Response {request}')
        logger.info('Обработка завершена')
        return responce

    @log
    def validate_request(self, data):
        logger.info('Производится проверка сообщения')
        try:
            msg = json.loads(data, encoding='utf-8')
            responce = self.handler(msg)
            logger.info('Проверка успешно завершена')
            return json.dumps(responce).encode('utf-8')
        except json.decoder.JSONDecodeError:
            logger.error('Неверный формат ссообщения')
            return b'Incorrect format'
    @log
    def read_requests(self, clients):
        for s_client in clients:
            logger.info('Принято сообщение от клиента')
            data = s_client.recv(1024).decode('ascii')
            chat = chat + data + "\n"
    @log    
    def write_responses(self, clients):
        for s_client in clients:
            resp = chat.encode('ascii')
            s_client.send(resp.upper())
            logger.info('Клиенту отправлено сообщение')

    @log
    def new_listen_socket(self, address):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(address)
        sock.listen(5)
        logger.info('Сервер запущен')
        sock.settimeout(0.2)

        return sock

    @log
    def start(self):
        logger.info('Запуск сервера')
        full_address = (self.address, self.port)
        clients = []
        chat = ""
        while True:
            with self.new_listen_socket(full_address) as sock:
                try:
                    conn, addr = sock.accept()
                except OSError as e:
                    pass
                else:
                    logger.info("Получен запрос на соединение с %s" % str(addr))
                    clients.append(conn)
                finally:
                    
                    r = [] 
                    w = []
                    try:
                        r, w, e = select.select(clients, clients, [], 0)
                    except Exception as e:
                        pass
                            
                    self.read_requests(r)
                    self.write_responses(w)


def main():
    logger.info('Старт приложения')

    parser = argparse.ArgumentParser(description='Server parser.')
    parser.add_argument('-a', '--address', type=str, required=False,
                        action='store', default='', help='Set address')
    parser.add_argument('-p', '--port', type=int, required=False,
                        action='store', default=7777, help='Set port')
    args = parser.parse_args()

    myserver = Server(args.address, args.port)
    myserver.start()


if __name__ == "__main__":
    main()
