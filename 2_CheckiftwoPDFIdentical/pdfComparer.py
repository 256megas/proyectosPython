import hashlib
from difflib import SequenceMatcher


class PdfComparer:
    def __init__(self, file1, file2):
        self.__file1 = file1
        print("Archivo1: ", self.__file1)
        self.__file2 = file2
        print("Archivo2: ", self.__file2)

    def comparer(self):
        hash1 = hashlib.sha1()
        hash2 = hashlib.sha1()
        print("Hash1:    ", hash1)
        print("Hash2:    ", hash1)

        with open(self.__file1, 'rb') as file1:
            chunk = 0
            while chunk != b'':
                chunk = file1.read(1024)
                hash1.update(chunk)
        with open(self.__file2, 'rb') as file2:
            chunk = 0
            while chunk != b'':
                chunk = file2.read(1024)
                hash2.update(chunk)

        if (hash1.hexdigest() == hash2.hexdigest()):
            return True
        return False
