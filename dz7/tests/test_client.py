from context import app
import pytest


class TestClient:
    def test_init(self):
        test_client = app.Client('localhost', 7777)
        assert test_client

    def test_start_serv_off(self):
        test_client = app.Client('localhost', 7776)
        test_client.start()

    def test_start_serv_on(self):
        test_client = app.Client('localhost', 7777)
        test_client.start()


if __name__ == "__main__":
    test_client = TestClient()

    test_client.test_init()
    test_client.test_start_serv_off()
    test_client.test_start_serv_on()
    main()
