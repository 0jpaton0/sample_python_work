# sample_python_work
 sample python code...some in DCC and some not
 
 there are 
 3 samples here:
 
 
GitHub\sample_python_work\scr\update_maya_menubar.py

GitHub\sample_python_work\scr\draw_folder_structure.py

GitHub\sample_python_work\tests which uses pytest and logging to test GitHub\sample_python_work\scr\basic_math_utilities.py


######################update_maya_menubar##############################


Description:
Creates a new dropdown menu and adds it to maya's main window 

To Use : 
open maya 2025 (or a version that is compatible with python3 and pyside6)
open GitHub\sample_python_work\scr\update_maya_menubar.py in the maya script editor
evaluate whole script and a new menu bar drop down will appear and be populated with menu options

<python from script that runs script>
>>>tool_bar = ManageToolBar() 

 
######################draw_folder_structure##############################


Description:
Viualizes given folder structure and the files within it. 

To Use:
at the bottom of draw_folder_structure.py update the path var to the folder path you want to visualize

<python from script to update path>
>>>path = 'C:\\temp\\folder_deep'

evaluate script.
(I use pycharm but it works in the command line as well)

<cmd line to path to python file>
>>>cd C:\GitHub\sample_python_work\scr
<cmd line to call python file>
draw_folder_structure.py

<cmd line final cmd>
>>>c:\GitHub\sample_python_work\scr>draw_folder_structure.py

a printed version will be written to (tempfile.gettempdir() + folder_structure.txt) ..."C:\Users\jpato\AppData\Local\Temp\folder_structure.txt"


######################unit tests##############################


Description:
Tests math functions and logs to file. This uses pytest (not in the standard library) for testing and logging for...logging 

Files: 
scr/basic_math_utilities.py ...as the test case 
pytest.ini ...for initializing pytest
requirements.txt ...for the virtual env
and the contents of the folder ...\GitHub\sample_python_work\tests for the tests 

<cmd line input...path to root>
>>>cd C:\GitHub\sample_python_work

<cmd line input...add pytest command>
>>>pytest

<cmd line input...to run simple test>
>>>C:\GitHub\sample_python_work>pytest

output will be written to the cmd line 

<cmd line for more verbose tests and to write to disk ...\GitHub\sample_python_work\tests.log>
'''
	C:\GitHub\sample_python_work>pytest -v > tests.logs
'''