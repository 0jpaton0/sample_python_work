import os
import glob
import tempfile

"""
to use run in pycharm
"""


class TreeCharacters:
    def __init__(self):
        """
        initializes parts to be used for drawing folder structure
        """

        # cast for utf-8 encoding for non-standard characters
        # │
        self.vertical = u'\u2502'
        # ─
        self.hoizontal = u'\u2500'
        # └
        self.corner = u'\u2514'
        # ├
        self.tee = u'\u251C'

        # standard characters
        self.directory = '\\'
        self.space = ' '
        self.empty_space = ''
        self.tab = '\t'

    # the below functions build parts that maybe needed while draw the folder structure
    # the argument sent is used to customize the specific character lengths
    def create_space(self, count):
        return self.space * count

    def create_bend(self, hor_amount=1):
        return self.corner + (self.hoizontal * hor_amount)

    def create_line(self, line_length=1):
        return self.hoizontal * line_length

    def create_tab(self, tab_lengths=1):
        return self.tab * tab_lengths


class DrawFolderStructure:

    def __init__(self, start_path):
        self.TC = TreeCharacters()
        # parent folder to draw contents of
        self.start_path = start_path

        # write file setup
        temp_directory = tempfile.gettempdir()
        file_name = 'folder_structure.txt'
        file_path = os.path.join(temp_directory, file_name)
        self.write_file = open(file_path, 'w', encoding='utf-8')

        # class vars
        self.all_folders = []
        self.root_children = []
        self.more_folders = True

        # grab folders based on start_path and start
        self.all_folders = [path_item[0] for path_item in os.walk(self.start_path)]
        self.iterate_folders(self.start_path, self.TC.empty_space, True)

    def __str__(self):
        return('start path :: {}\nall folders :: {}\nmore folders :: {}'.
               format(self.start_path, self.all_folders, self.more_folders))

    def close_file_stream(self):
        self.write_file.close()

    @staticmethod
    def return_direct_child_folders(path, child_folders):
        """
        returns a list of folders that are direct decadents children of the given path

        @param path: path to draw children from
        @type path: string
        @param child_folders: list to be populated but it may contain a initial path depending on needs
        @type child_folders: list
        @return: list of children folders
        @rtype: list
        """
        for item in glob.glob(os.path.join(path, '*')):
            if os.path.isdir(item):
                child_folders.append(item)

        return child_folders

    def print_folder_files(self, folder, space, first):
        """
        print folders and file to disk and console

        :param folder: folder path to use
        :type folder: string
        :param space: amount of space to use...probably before prepended
        :type space: string
        :param first: is this being called form __init__
        :type first: bool
        """

        # get all files in folder path
        files = []
        for item in os.listdir(folder):
            test_item = os.path.join(folder, item)
            if os.path.isfile(test_item):
                files.append(item)

        # print folders first
        folder_name = folder.split('\\')[-1]
        # called from __init__ ...just prints the folders name
        if first:
            print_string = '{}'.format(folder_name)
            print(print_string)
            self.write_file.write(print_string + '\n')
        # creates a longer horizontal line after the corner
        elif folder in self.root_children:
            print_string = '{}{}{}{}'.format(space, self.TC.corner + self.TC.create_line(2), self.TC.directory, folder_name)
            print(print_string)
            self.write_file.write(print_string + '\n')
        else:
            print_string = '{}{}{}{}{}'.format(space, self.TC.corner, self.TC.create_line(), self.TC.directory, folder_name)
            print(print_string)
            self.write_file.write(print_string + '\n')

        # print files
        file_index = 0
        file_count = len(files)
        while file_index < file_count:
            file = files.pop(0)
            # use a tee shape because more will be printed
            if self.more_folders or len(files) > 0:
                print_string = '{}{}{}{}{}'.format(space + self.TC.tab, self.TC.tee, self.TC.create_line(), space, file)
                print(print_string)
                self.write_file.write(print_string + '\n')
            # end of the folder print a corner
            else:
                print_string = '{}{}{}{}{}'.format(space + self.TC.tab, self.TC.corner, self.TC.create_line(), space, file)
                print(print_string)
                self.write_file.write(print_string + '\n')

            file_index += 1

    def iterate_folders(self, path, space, first=False):
        """
        gets a path and setups the printing based on arguments and class vars

        @param path: path to draw contents of
        @type path: string
        @param space: space to add relative to file pointer
        @type space: string
        @param first: is this called from __init__
        @type first: bool
        """
        current_folders = self.return_direct_child_folders(path, [path])

        folder_index = 0
        folder_count = len(current_folders)
        while folder_index < folder_count:
            # grab the first folder from current path
            current_folder = current_folders.pop(0)
            sub_folders = self.return_direct_child_folders(current_folder, [])

            # this adjusts folders length if more need to be added
            # if there are sub-folders they need to be printed after the current folder
            if sub_folders and not first:
                # reduce the index to adjust for the change in current_folders length
                folder_index -= len(sub_folders)
                # combine sub_folders and current_folders
                # add current_folders to the end of sub_folders and assign it to current_folders
                sub_folders.extend(current_folders)
                current_folders = sub_folders
                # there are more folders to print
                self.more_folders = True
            else:
                self.more_folders = False

            if current_folder in self.root_children:
                # set space to ''
                space = self.TC.empty_space
            else:
                # add tab to space
                space = space + self.TC.tab

            # after adjusting for space send to print
            self.print_folder_files(current_folder, space, first)

            if first:
                first = False
                # need to keep the original folders as they will need to be printed differently
                self.root_children = current_folders.copy()

            folder_index += 1

# update to local folder
path = 'C:\\temp\\folder_deep'
DrawFolderStructure(path)
