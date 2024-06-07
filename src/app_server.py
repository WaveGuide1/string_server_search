import socket


class AppServer:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080

    def starting_server(self) -> None:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:

            sk.bind((self.host, self.port))
            # Listening for incoming connection
            sk.listen()
            print(f"Server is listening at: {self.host}: {self.port}")

            connection, address = sk.accept()
            with connection:
                print(f"{address} is connected")
                while True:
                    info = connection.recv(1111)
                    if not info:
                        break
                    connection.sendall(info)


if __name__ == "__main__":
    app_server = AppServer()
    app_server.starting_server()
