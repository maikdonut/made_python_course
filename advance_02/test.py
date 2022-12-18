import socket
import time
import threading
import unittest
from server import server_listen


class TestURLs(unittest.TestCase):
    def test_server(self):
        server = socket.socket()
        server_listen(server, socket.SOL_SOCKET, socket.SO_REUSEADDR)
        server_thread = threading.Thread(
            target=server_listen,
            args=(server, socket.SOL_SOCKET, socket.SO_REUSEADDR, True),
        )
        server_thread.start()
        time.sleep(0.0001)
        fake_client = socket.socket()
        fake_client.settimeout(1)
        fake_client.connect(("localhost", 5000))
        fake_client.close()
        server_thread.join()

    def fake_server(self):
        sock = socket.socket()
        sock.bind(("localhost", 5000))
        sock.listen(0)
        sock.accept()
        sock.close()

    def test_client(self):
        server_thread = threading.Thread(target=self.fake_server)
        server_thread.start()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 5000))
        client.close()
        server_thread.join()


if __name__ == "__main__":
    unittest.main()
