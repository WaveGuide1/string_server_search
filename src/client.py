import socket


class Client:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080

    def sending_info(self, message: str) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
            sk.connect((self.host, self.port))

            # Sending a message to the server
            sk.sendall(message.encode())

            info = sk.recv(1111)
            print(info.decode())


if __name__ == "__main__":
    client = Client()
    client.sending_info("From a Client")
