import random
import string


class GenerateFile:

    def __init__(self):
        self.length = 10
        self.number_lines = 100000
        self.file_path = "data_source/file.txt"

    def generate_random_string(self):
        """Generate a random string of fixed length."""
        return ''.join(random.choice(string.ascii_letters) for _ in range(self.length))

    def generate_file(self):
        """Generate a file with the specified number of lines containing random strings."""

        with open(self.file_path, 'w') as file:
            for _ in range(self.number_lines):
                file.write(self.generate_random_string() + '\n')

        # Add a specific string for testing
        test_string = "test_string"
        with open(self.file_path, 'a') as file:
            file.write(test_string + '\n')


if __name__ == '__main__':
    gen = GenerateFile()
    gen.generate_file()

    print(f"File generated at {gen.file_path} with 100,001 lines.")
