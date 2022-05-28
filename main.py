from pyfileutils import FileHandler
from pathlib import Path


def data_dir():
    return Path("test/data")

def test_files():
    fobj = FileHandler(data_dir())
    for file_ in fobj:
        print(file_)

def test_folders():
    for folder in FileHandler(data_dir()).all_folders():
        print(folder)

def Main():
    print(10*"*")
    print("Files")
    test_files()
    print(10*"*")
    print("Folders")
    test_folders()


if __name__ == '__main__':
    Main()
