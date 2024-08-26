from PySide6 import QtWidgets
from shiboken6 import wrapInstance
# local to maya
import maya.OpenMayaUI as OpenMaya

"""
to use evaluate in maya 2025 script editor
"""

main_window = None
main_menu_bar = None


class LevelMap:
    """

    """
    def __init__(self, name, level, action):
        self.name = name
        self.level = level
        self.action = action

    def __str__(self):
        return 'name :: {}\nlevel :: {}\naction :: {}'.format(self.name, self.level, self.action)


class ManageToolBar(object):
    def __init__(self):
        self.long = int
        self.current_selection = 30

        # contains LogMap classes that are used in the level menu
        self.actions = []
        # class level menu actions to be used by a class level function
        self.item1_option1 = None
        self.item1_option2 = None
        self.item1_option3 = None
        self.item1_option4 = None
        self.item1_option5 = None

        # start process
        self.initialize_bar_widgets()

    def initialize_action(self, name, level, action):
        """
        initializes a LevelMap class and adds it to a class level list

        @param name: name of the asset
        @type name: string
        @param level: level number
        @type level: int
        @param action: menu action
        @type action: menu action
        """

        action.setCheckable(True)
        if self.current_selection == level:
            action.setChecked(True)
        else:
            action.setChecked(False)
        self.actions.append(LevelMap(name, level, action))

    def initialize_bar_widgets(self):
        """
        initializes menu items and actions and adds them to maya main menu bar
        """

        # get maya's menu bar
        menu_bar = self.get_main_menu_bar()
        # main menu dropdown menu
        file_menu = QtWidgets.QMenu('New Drop Down')

        # first menu item
        # first menu item in dropdown
        file_menu_item1 = QtWidgets.QMenu('Menu Item 1')
        # create and add actions to menu items...these just fire a function which is passed as an argument
        file_menu_item1.addAction('Item 1 Option 1', self.item1_action)
        # create the level menu for first menu item
        level_menu = QtWidgets.QMenu('Level Menu')
        # create all level menu actions which all call the function with predefined arguments
        # the function initialize_action automate redundant steps
        self.item1_option1 = level_menu.addAction('10', lambda: self.update_log_level(10))
        self.initialize_action('item1_option1', 10, self.item1_option1)
        self.item1_option2 = level_menu.addAction('20', lambda: self.update_log_level(20))
        self.initialize_action('item1_option2', 20, self.item1_option2)
        self.item1_option3 = level_menu.addAction('30', lambda: self.update_log_level(30))
        self.initialize_action('item1_option3', 30, self.item1_option3)
        self.item1_option4 = level_menu.addAction('40', lambda: self.update_log_level(40))
        self.initialize_action('item1_option4', 40, self.item1_option4)
        self.item1_option5 = level_menu.addAction('50', lambda: self.update_log_level(50))
        self.initialize_action('item1_option5', 50, self.item1_option5)
        # add level menu to menu item 1
        file_menu_item1.addMenu(level_menu)
        # add first menu item to main dropdown
        file_menu.addMenu(file_menu_item1)
        # first menu item

        # second menu item
        # second menu item in dropdown
        file_menu_item2 = QtWidgets.QMenu('Menu Item 2')
        # create and add actions to menu items...these just fire a function which is passed as an argument
        file_menu_item2.addAction('Item 2 Option 1', self.item2_action)
        # add second menu item to main dropdown
        file_menu.addMenu(file_menu_item2)
        # second menu item

        # add the menu we just created to the maya menu bar
        menu_bar.addMenu(file_menu)

    @staticmethod
    def item1_action():
        """
        placeholder function
        """
        print('item1 action triggered')

    @staticmethod
    def item2_action():
        """
        placeholder function
        """
        print('item2 action triggered')

    def invert_selection(self):
        """
        functions like radio buttons, sets the checked value for chosen item and unchecks the rest
        """

        for action in self.actions:
            if action.level != self.current_selection:
                action.action.setChecked(False)
            else:
                action.action.setChecked(True)

    def update_log_level(self, new_level=0):
        """
        case statement that find correct level and switches others to off

        @param new_level:
        @type new_level: int
        """

        match new_level:
            case 10:
                self.item1_option1.checked = True
                self.current_selection = 10
                self.invert_selection()
            case 20:
                self.item1_option2.checked = True
                self.current_selection = 20
                self.invert_selection()
            case 30:
                self.item1_option3.checked = True
                self.current_selection = 30
                self.invert_selection()
            case 40:
                self.item1_option4.checked = True
                self.current_selection = 40
                self.invert_selection()
            case 50:
                self.item1_option5.checked = True
                self.current_selection = 50
                self.invert_selection()

    def get_main_window(self):
        """
        gets the maya main menu

        @return: main_window to add our menu to
        @rtype: wrapped instance of maya main window
        """
        global main_window

        if main_window:
            return main_window

        main_window_ptr = OpenMaya.MQtUtil.mainWindow()
        main_window = wrapInstance(self.long(main_window_ptr), QtWidgets.QWidget)
        return main_window

    def get_main_menu_bar(self):
        """
        gets maya menu bar from maya's main window

        @return: maya's menu bar
        @rtype: QMenuBar
        """
        global main_menu_bar

        if main_menu_bar:
            return main_menu_bar

        main_menu_bar = self.get_main_window().findChild(QtWidgets.QMenuBar, '')
        return main_menu_bar


tool_bar = ManageToolBar()
