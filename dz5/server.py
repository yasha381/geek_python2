import json
from typing import Any, Dict
from socket import *
import argparse
import logging
from log import server_log_config

logger = logging.getLogger('server_log')


class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.mapping = {
            'authenticate': self.handle_authenticate
        }

    def handle_authenticate(self, request):
        logger.info('Проверка аутентификации')
        if request['user'] == {'account_name': 'test', 'password': 'test'}:
            return {'response': 200}

        return {'response': 402, 'error': 'wrong password'}

    def handler(self, request: Dict[str, object]):
        logger.info('Производится обработка сообщения')
        print(f'Client sent {request}')
        responce = self.mapping[request['action']](request)
        print(f'Response {request}')
        logger.info('Обработка завершена')
        return responce

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

    def start(self):
        logger.info('Запуск сервера')

        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind((self.address, self.port))
            s.listen(1)
            logger.info('Сервер запущен')
            while True:
                client, addr = s.accept()
                with client:
                    data_b = client.recv(1000000)
                    logger.info('Принято сообщение от клиента')

                    client.send(self.validate_request(data_b))
                    logger.info('Клиенту отправлено сообщение')


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
