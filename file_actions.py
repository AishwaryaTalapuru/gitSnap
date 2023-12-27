import os
import shutil
#Class that handles folder operations like create and delete folders and sub folders according to the path
class file_actions:
    def __init__(self, ui_path, data):
        #Initializing the user input path and the result of the subsequent functions
        self.ui_path = ui_path
        self.res = False
        self.data = data

    def make_file(self):
        self.res = False
        try:
            with open(self.ui_path, 'w') as file:
                file.write(self.data)
            print(f"File '{self.ui_path}' created successfully.")
            self.res = True
        except OSError as e:
            print(f"Error creating file '{self.ui_path}': {e}")
        return self.res

    def delete_file(self):
        self.res = False
        try:
            os.remove(self.ui_path)
            print(f"File '{self.ui_path}' deleted successfully.")
            self.res = True
        except OSError as e:
            print(f"Error deleting file '{self.ui_path}': {e}")
        return self.res



"""    
file_acts_obj = file_actions("/Users/aishwaryatalapuru/Documents/gS_wrksp/file1.txt", "")
file_acts_obj.delete_file()
"""









        