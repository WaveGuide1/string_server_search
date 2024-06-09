import unittest
from src.app_server import AppServer


class TestAppServer(unittest.TestCase):

    # Test case
    def test_search_in_file(self):
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write("test_string\nanother_string\n")

        self.assertEqual(AppServer.search_string(file_path, "test_string", True), "STRING EXISTS")
        self.assertEqual(AppServer.search_string(file_path, "not_found_string", True), "STRING NOT FOUND")


if __name__ == '__main__':
    unittest.main()
