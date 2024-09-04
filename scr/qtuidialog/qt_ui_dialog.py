from pathlib import Path

from PySide6 import QtWidgets, QtGui, QtUiTools, QtCore
from PySide6.QtCore import Qt, QSize
from maya import OpenMayaUI as OpenMayaUI
from shiboken6 import wrapInstance

import maya.cmds as cmd


class AssetData:
    """
    class used to hold data for assets added to the tree
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type


class QtUiDialog(QtWidgets.QMainWindow):

    def __init__(self):
        maya_main = self.get_maya_main_window()
        super(QtUiDialog, self).__init__(maya_main)
        # path directly to .ui file
        ui_path = Path('C:\\GitHub\\sample_python_work\\scr\\qtuidialog\\qt_ui_dialog.ui')
        self.ui = self.load_ui(ui_path, maya_main)
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        # connect ui elements to python functions
        self.ui.btn_cube.clicked.connect(self.btn_cube_clicked)
        self.ui.btn_camera.clicked.connect(self.btn_camera_clicked)
        
        # rt click menus 
        self.ui.tre_tree.customContextMenuRequested.connect(self.rt_click_tree)
        self.ui.tre_tree.itemClicked.connect(self.add_tree_action)
        
        # container for created assets
        self.assets = []

    def eventFilter(self, obj, event):
        """
        catches close event override for QObject

        :param obj: event filter
        :param event: event filter
        :return:
        """

        if obj is self.ui and event.type() == QtCore.QEvent.Close:
            self.close_event()
            return True
        return False

    def close_event(self):
        """
        called from the eventFilter on close
        """

        self.ui.close()

    def run(self):
        """
        opens ui
        """

        self.ui.show()

    @staticmethod
    def get_maya_main_window():
        """
        gets the pointer to the window to use as ui

        :return: maya_main
        :rtype: python wrapper for a C++ object instantiated at a given memory address
        """
        
        main_window_pointer = OpenMayaUI.MQtUtil.mainWindow()
        maya_main = wrapInstance(int(main_window_pointer), QtWidgets.QWidget)
        
        return maya_main

    @staticmethod
    def load_ui(ui_path, parent=None):
        """
        loads the .ui file from a path

        :param ui_path: path to .ui file
        :type ui_path: str
        :param parent: this is a top level ui element with no parent
        :type parent: None
        :return: ui
        :rtype: QUiLoader
        """
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        ui = loader.load(ui_file, parent)
        ui_file.close()
        return ui

    def rt_click_tree(self, pos):
        """
        event for right click action. calls for creation of specific rt click menu
        creation depending on type of item at pos

        @param pos: where the cursor is located
        @type pos: QPoint
        """
        
        item = self.ui.tre_tree.itemAt(pos)
        if item is not None:
            if item.whatsThis(0) == 'cube':
                self.populate_cube_menu()
            elif item.whatsThis(0) == 'camera':
                self.populate_camera_menu()
        elif item is None:
            self.populate_tree_menu()

    def populate_tree_menu(self):
        """
        creates right click option for the anim tree
        """

        rt_click_menu = QtWidgets.QMenu()

        set_action = rt_click_menu.addAction('Tree')
        set_action.triggered.connect(lambda: self.add_tree_action())
        rt_click_menu.addAction(set_action)

        rt_click_menu.exec(QtGui.QCursor.pos())

    def populate_cube_menu(self):
        """
        creates right click option for the cube items
        """

        rt_click_menu = QtWidgets.QMenu()

        set_action = rt_click_menu.addAction('Cube')
        set_action.triggered.connect(lambda: self.add_cube_action())
        rt_click_menu.addAction(set_action)

        rt_click_menu.exec(QtGui.QCursor.pos())

    def populate_camera_menu(self):
        """
        creates right click option for the anim tree
        """

        rt_click_menu = QtWidgets.QMenu()

        set_action = rt_click_menu.addAction('Camera')
        set_action.triggered.connect(lambda: self.add_camera_action())
        rt_click_menu.addAction(set_action)

        rt_click_menu.exec(QtGui.QCursor.pos())

    def btn_cube_clicked(self):
        """
        event called on cube button pressed
        """

        self.add_assets(cmd.polyCube()[0], 'cube')

    def btn_camera_clicked(self):
        """
        event called on camera button pressed
        """

        self.add_assets(cmd.camera()[0], 'camera')

    @staticmethod
    def add_tree_action():
        """
        add specific action for the tree here
        """
        print('add specific action for the tree here')

    @staticmethod
    def add_cube_action():
        """
        add specific action for cubes here
        """
        print('add specific action for cubes here')

    @staticmethod
    def add_camera_action():
        """
        add specific action for cameras here
        """
        print('add specific action for cameras here')

    def refresh_tree_ui(self):
        """
        populates tree with cube and cameras items
        """

        self.ui.tre_tree.clear()

        for asset in self.assets:
            asset_item = QtWidgets.QTreeWidgetItem()
            asset_item.setSizeHint(0, QSize(-1, 20))
            asset_item.setText(0, asset.name)
            asset_item.setWhatsThis(0, asset.type)
            
            self.ui.tre_tree.addTopLevelItem(asset_item) 
        
    def add_assets(self, name, type):
        """
        adds recently created assets to class list and calls to refresh tree
        """
        
        self.assets.append(AssetData(name, type))
        self.refresh_tree_ui()


qt_UI_Dialog = QtUiDialog()
qt_UI_Dialog.run()

        