# pyfileutils
Utility set for handling files through python. 

During some years of doing research code and software development I have repeatedly 
had to write the small snippets to fetch files by a specific extension or in a
specific folder through python. Although in theory it's really simple to do so through
the standard library the fact is you end up having to write some boiler plate code
to re-do the same thing over and over again. 


This library introduces some really simple - human readable functionality that uses
the python standard library as a backend - to achieve simple things like

```

FileHandler("top/directory").all_files()
FileHandler("top/directory").by_extension(".json")
```

You should be able to read from the context what the return object will give you.

## Install
Currently this is installed using the pip install in the top directory.
- Clone repository
- Go into repository
- Call pip install . 
Work is under way to get this into the git repository so it can be build using pip install pyfileutils but it might take a while. [A while because I don't like sharing or spreading code that is inefficient and bad!]

## Philosophy
As stated, the functionality behind the process is really simple it's basically a 
wrapper around the pathlib library. As such I don't claim any novelty  with this project.
The real objective for me is just to abstract a really common set of call functions that
require 3-5 lines, but come up for me really often.

## Development Guide
KISS is the word of the day 
- Keep It Simple Stupid
Human readable, simple expatiations in the code base and minimum documentation because the function calls should be self-evident. If they are not self evident they should not be in this library but a fork which can include this library.

