""" 
Testing the File handler script
"""
from pathlib import Path
import pytest
from ..pyfileutils import FileHandler 


def current_folder() -> Path:
    """Get the parent folder so we can point to the 
    subfolders for testing """
    return Path(__file__).parent.absolute()

def top_folder():
    """Define the top folder for the test data. This 
    means that we cannot move the top folder unless we 
    break the tests"""
    return current_folder() / "data"


def test_top_folder():
    """Ensure the top data folder exists"""
    topdir = top_folder()
    if not topdir.is_dir():
        raise FileNotFoundError(f"No test data folder found {topdir}")


def test_empty():
    """Ensure that an empty find returns an empty array"""
    assert list(FileHandler("kdkso,wmxidal;ag").all_files()) == [], \
                            "Empty folder does not return empty arrary"


def test_exits():
    """Make sure that existsing folder as topdir works"""
    topdir = top_folder()
    assert topdir.is_dir(), "Existing directory should return true"


def test_does_not_exits():
    """Make sure that non existing folder as topdir returns false"""
    topdir = FileHandler("I_do_not_exist")
    assert not topdir.is_dir(), "Existing directory should return true"


def test_iter():
    """Ensure that iterating over the files works"""
    for files in FileHandler(top_folder()):
        pass


def test_all_files():
    topdir = top_folder()
    fobj = FileHandler(topdir)
    all_files = fobj.all_files()
    # Create a base set of all files that we need to ensure are found
    json_files = []
    txt_files = []
    for i in range(1,4):
        json_files.append(f"json{i}.json")
        txt_files.append(f"txt{i}.txt")
    json_files.append("jsonA.json")
    txt_files.append("txtA.txt")



    




