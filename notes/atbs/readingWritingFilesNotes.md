# Reading and Writing Files Notes
## Paths
Notes on reading and writing files taken from the book 'Automate the Boring Stuff' by Al Sweigart.
Chapter 9, page 202
<br>
* On Windows, paths separate directories using a backslash **(\\)** while linux and macOS use forward slashes **(\/)**
* Use **from pathlib import Path** to return a path with the correct path separators.
```python
from pathlib import Path
Path('..', 'User', 'UserName') #returns WindowsPath(../User/UserName) appears as forward slashes in shell
```
* A forward slash can be used to join more Path objects and strings together
* One of the first two values must be a Path value in order for the forward slash to work
```python
Path('journal') / 'notes' / 'dictionaries' # returns journal/notes/dictionaries
```
* **Absolute paths** begin with the root folder C:\
* **Relative paths** are relative to the current working directory and use 'this directory' (.) or 'parent folder' (..)
*  Create multiple directories/subdirectories using **os.makedirs(filepath)**
```python
import os
os.makedirs('C:\\diet\\coke\zero') # Will create any directories that do not exist
```
* Use **mkdir()** method to create a directory from a Path object
```python
from pathlib import Path
Path(r'C:\sodas\brands\flavors').mkdir() #This will only create the 'flavors' directory
```
* **os.path.getsize(path)** will return the byte size of a file in the path argument
*  **os.listdir(path)** will return a list of filenames as strings
* See page 213 for an explanation on glob patterns.
* Check path validity using pathObj.exists(), pathObj.is_file(), or pathObj.is_dir(), where pathObj is a path object.
## Opening, reading, and writing files
* To open a file, provide the **open()** function with a File object or a path as a string. A file is opened in read mode by default. You can explicitly state this by providing 'r' as a second argument. Returns a File object.
* You can provide open() with an 'a' or 'w' to open a file in append or write mode, respectively. If a file does not exist when opening in either mode, it will be created.
```python
helloFile = open(Path.home() / 'hello.txt', 'r')
```
* To read a file, use either the **read()** or **readlines()** method, which will return the contents of the file as a single string or list of strings, respectively.
