# sample_python_work
Sample python code...some in DCC and some not
 
3 samples:
 
_GitHub\sample_python_work\scr\update_maya_menubar.py_

_GitHub\sample_python_work\scr\draw_folder_structure.py_

_GitHub\sample_python_work\tests_

<br/>

## update_maya_menubar.py


**Description:**
Creates a new dropdown menu and adds it to maya's main window 

<br/>

**To Use:**
1. Open maya 2025 (or a version that is compatible with python3 and pyside6)

2. Open _GitHub\sample_python_work\scr\update_maya_menubar.py_ in the maya script editor

3. Evaluate whole script and a new menu bar drop down will be added and populated with menu options

_python from script that runs script_
```
tool_bar = ManageToolBar() 
```
<br/>

## draw_folder_structure.py


**Description:**
Viualizes given folder structure and the files within it. 

<br/>

**To Use:**
1. at the bottom of draw_folder_structure.py update the path var to the folder path you want to visualize

_path var from script to update_
```
path = 'C:\\temp\\folder_deep'
```

2. evaluate script.
(I use pycharm but it works in the command line as well)

_cmd line to path to python file_
```
cd C:\GitHub\sample_python_work\scr
```

_cmd line to call python file_
```
draw_folder_structure.py
```

_cmd line final cmd_
```
c:\GitHub\sample_python_work\scr>draw_folder_structure.py
```

3. a printed version will be written to (tempfile.gettempdir() + folder_structure.txt) ..."C:\Users\jpato\AppData\Local\Temp\folder_structure.txt"

<br/>

## unit tests


**Description:**
Tests math functions and logs to file. This uses pytest (not in the standard library) for testing and logging for...logging 

**Files used:**

scr/basic_math_utilities.py ...as the test case 

\GitHub\sample_python_work\pytest.ini ...for initializing pytest

\GitHub\sample_python_work\requirements.txt ...for the virtual env

\GitHub\sample_python_work\tests which contains the tests
<br/>

**To use:**
1. _cmd line input...path to root_
```
cd C:\GitHub\sample_python_work
```

2. _cmd line input...add pytest command_
```
pytest
```

3. _cmd line input...to run simple test_
```
C:\GitHub\sample_python_work>pytest
```

4. output will be written to the cmd line 

_cmd line for more verbose tests and to write to disk ...\GitHub\sample_python_work\tests.log_
```
C:\GitHub\sample_python_work>pytest -v > tests.logs
```
