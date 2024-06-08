import socket
import threading
import time
import configparser
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='DEBUG: %(message)s')


class AppServer:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080
        self.config_file_path = "app_configuration.ini"

    @staticmethod
    def load_configuration(file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        return config['MAIN'].get('linuxpath'), config['MAIN'].getboolean('REREAD_ON_QUERY')

    @staticmethod
    def log_debug(search_query, client_address, execution_time):
        logging.debug(f"DEBUG: Query: {search_query}, IP: {client_address[0]}, Execution Time: {execution_time:.4f} "
                      f"seconds")

    @staticmethod
    def search_string(file_path, search_string, reread_on_query):
        if reread_on_query:
            with open(file_path, 'r') as file:
                for line in file:
                    if line.strip() == search_string:
                        return "STRING EXISTS"
            return "STRING NOT FOUND"
        else:
            if search_string in cached_lines:
                return "STRING EXISTS"
            return "STRING NOT FOUND"

    def handling_client_connection(self, client_socket, file_path, reread_on_query):
        try:
            while True:
                data = client_socket.recv(1024).decode().strip()
                if data:
                    start_time = time.time()
                    response = self.search_string(file_path, data, reread_on_query)
                    end_time = time.time()
                    self.log_debug(data, client_socket.getpeername(), end_time - start_time)
                    client_socket.send(response.encode() + b'\n')
                else:
                    break
        finally:
            client_socket.close()

    def start(self):
        file_path, reread_on_query = self.load_configuration(self.config_file_path)
        global cached_lines
        cached_lines = set()

        if not reread_on_query:
            with open(file_path, 'r') as file:
                for line in file:
                    cached_lines.add(line.strip())

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Server listening on port {self.port}")

        while True:
            client_socket, addr = server.accept()
            client_handler = threading.Thread(
                target=self.handling_client_connection,
                args=(client_socket, file_path, reread_on_query)
            )
            client_handler.start()


if __name__ == "__main__":
    app_server = AppServer()
    app_server.start()
