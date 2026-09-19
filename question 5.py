from abc import ABC, abstractmethod


class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class TextFileHandler(FileHandler):

    def read(self):
        print("Reading text file.")

    def write(self):
        print("Writing to text file.")


class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading binary file.")

    def write(self):
        print("Writing to binary file.")


text_file = TextFileHandler()
binary_file = BinaryFileHandler()

text_file.read()
text_file.write()

binary_file.read()
binary_file.write()