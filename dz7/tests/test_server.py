from context import app
import json
import pytest


class TestServer:
    def test_init(self):
        test_server = app.Server('', 7777)
        assert test_server

    def test_validate_request_correct(self):
        test_server = app.Server('', 7777)
        msg = {'action': 'authenticate', 'user': {'account_name': 'test',
               'password': 'test'}}
        msg_str = json.dumps(msg)
        result = test_server.validate_request(msg_str)
        assert result == b'{"response": 200}'

    def test_validate_request_incorrect(self):
        test_server = app.Server('', 7777)
        result = test_server.validate_request(b'abcd')
        assert result == b'Incorrect format'

    def test_handler(self):
        test_server = app.Server('', 7777)
        hand_dict = {'action': 'authenticate', 'user': {'account_name': 'test','password': 'test'}} 
        result = test_server.handler(hand_dict)
        assert result == {'response': 200}

    def test_handle_authenticate_right(self):
        test_server = app.Server('', 7777)
        result = test_server.handle_authenticate({'action': 'authenticate',
                                                  'user': {
                                                      'account_name': 'test',
                                                      'password': 'test'}})
        assert result == {'response': 200}

    def test_handle_authenticate_wrong(self):
        test_server = app.Server('', 7777)
        result = test_server.handle_authenticate({'action': 'authenticate',
                                                  'user': {
                                                     'account_name': 'not_test',
                                                     'password': 'not_test'}})
        assert result == {'response': 402, 'error': 'wrong password'}


if __name__ == "__main__":
    test_server = TestServer()

    test_server.test_init()
    test_server.test_validate_request_incorrect()
    test_server.test_validate_request_correct()
    test_server.test_handler()
    test_server.test_handle_authenticate_right()
    test_server.test_handle_authenticate_wrong()
