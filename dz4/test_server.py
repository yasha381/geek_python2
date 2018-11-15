from server import Server

class TestServer:
    def test_init(self):
        test_server = Server('', 7777)
        assert test_server
        
    def test_start(self):
        test_server = Server('', 7777)
        test_server.start()      


if __name__ == "__main__": 
    test_server = TestServer()
    
    test_server.test_init()
    test_server.test_start()
