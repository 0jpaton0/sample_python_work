# sample_python_work
 sample python code...some in DCC and some not
 
 there are 
 3 samples here:
 
 
GitHub\sample_python_work\scr\update_maya_menubar.py

GitHub\sample_python_work\scr\draw_folder_structure.py

GitHub\sample_python_work\test which uses pytest and logging to test GitHub\sample_python_work\scr\basic_math_utilities.py


######################update_maya_menubar##############################


Description:
Creates a new dropdown menu and adds it to maya main window 

To Use : 
open maya 2025 or a version that is compatible with python3 and pyside6
open GitHub\sample_python_work\scr\update_maya_menubar.py in the maya script editor
evaluate whole script and a new menu bar drop down will appear and be populated with menu options

this line initializes the class and runs the script

tool_bar = ManageToolBar() 

 
######################draw_folder_structure##############################

Description:
Viualizes given folder structure and the files within it. 

To Use:
at the bottom of draw_folder_structure.py update the path var to the folder path you want to visualize

# update to local folder
path = 'C:\\temp\\folder_deep'

evaluate script.
(I use pycharm but it works in the command line as well)
to run in the command line cd into the the project scr folder

cd C:\GitHub\sample_python_work\scr
and add the name of the module 
draw_folder_structure.py
so
c:\GitHub\sample_python_work\scr>draw_folder_structure.py


a printed version will be written to (tempfile.gettempdir() + folder_structure.txt) ..."C:\Users\jpato\AppData\Local\Temp\folder_structure.txt"


######################unit tests##############################

Description:
Tests math functions and logs to file. This uses pytest (not in the standard library) and logging packages

This uses: 
scr/basic_math_utilities.py as the test case 
pytest.ini for initializing pytest
requirements.txt for the virtual env
and the contents of the folder scr for 