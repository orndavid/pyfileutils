""" 
File Handler 

Introducing an OO approach to a simple repeated process. 

I find myself very often iterating over a lot of files by extension, be it 
csv, json, bin. The python standard library allows for multiple ways of solving
this and I have tested them multiple times both using the os module and the 
pathlib module. 

This object is meant to solve this specific issue once and for all, so I can stop
re-writing this simple search every time I examine a new project.

The idea is simple, you can either use the OO approach and point at a specific dir
and iterate through all the files directly

```
from fileutils import FileHandler
fobj = FileHandler("some/dir/name")
for file_ in fobj:
    print(file_)
```
All the files are returned as pathlib.Path objects.

Alternatively you can fetch the subset using "by_extension". Both create the same
FileHandler class object but the list here only contains files with the selected
extension

```
from fileutils import FileHandler
fob = FileHandler("some/dir/name").by_extension(".json") for file_ in fob:
    print(file_)
```
The library is built on pathlib [developed using python 3.10] so theoretically
it should be stable for a long time. 

The algorithm stores all the files in memory. It is still fine for up to many thousand
files. Once you get above that we need to introduce a lazy evaluation of the process. 
For now [V 0.1] we won't do that. If enough requests come in we might examine it
""" 
from pathlib import Path
from typing import List

class FileHandler:
    def __init__(self, topdir: str):
        self.topdir = Path(topdir)
        self._iter = FileHandler._get_all_files(self.topdir)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iter)

    def all_files(self) -> List[Path]:
        """Return a list of all the files in the folder"""
        return FileHandler._get_all_files(self.topdir)

    def all_folders(self) -> List[Path]:
        """Return a list of all the folders that are within the top directory"""
        return FileHandler._get_all_folders(self.topdir)

    def by_extension(self, extension: str) -> List[Path]:
        """Fetch a list of with the correct extension"""
        return FileHandler._get_all_by_extension(self.topdir, extension)

    @staticmethod
    def _get_all_by_extension(path: Path, ext: str) -> List[Path]:
        if ext[0] != ".":
            raise ValueError(f"Extension format incorrect {ext} should be e.g. '.json'")
        if not ext:
            raise ValueError("Function should be called with extension")
        return path.rglob("*" + ext)

    @staticmethod
    def _get_all_files(path: Path) -> List[Path]:
        """Create a list of all the files in the directory"""
        return path.rglob("*")

    @staticmethod
    def _get_all_folders(path: Path) -> List[Path]:
        """List all the folders in the directory returns
        empty if there are no folders in the directory 
        """
        return path.iterdir()
