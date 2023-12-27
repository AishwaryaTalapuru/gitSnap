import os
import shutil
#Class that handles folder operations like create and delete folders and sub folders according to the path
class folder_actions:
    def __init__(self, ui_path):
        #Initializing the user input path and the result of the subsequent functions
        self.ui_path = ui_path
        self.res = False
    #Helper function to create a folder/directory
    def make_directory(self):
        self.res = False
        # directly creating a folder if such a folder in that path does not exist
        try:
            os.makedirs(self.ui_path)
            print(f"Folder '{self.ui_path}' created successfully.")
            self.res = True
        #Handling the case where the folder already exists
        except FileExistsError:
            print(f"The folder '{self.ui_path}' already exists.")
            self.res = "MayBe"
        except OSError as e:
            self.res = False 
            print(f"Error creating folder '{self.ui_path}': {e}")
        return self.res

#Helper function to delete the folder if the folder does not exist
    def delete_directory(self):
        self.res = False
        try:
            os.rmdir(self.ui_path)
            print(f"Directory '{self.ui_path}' deleted successfully.")
            self.res = True
        except FileNotFoundError:
            print(f"The directory '{self.ui_path}' does not exist.")
        except OSError as e:
            print(f"Need more info to delete the folder'{self.ui_path}': {e}")
            ui = input("The folder is not empty. Do you still want to delete it : [yes/no] ")
            if "yes" in ui or "y" in ui:
                try:
                    shutil.rmtree(self.ui_path)
                    print(f"Directory '{self.ui_path}' deleted successfully.")
                    self.res = True
                except OSError as er:
                    print(f"Error deleting directory '{self.ui_path}': {er}")
            else:
                self.res = True
        return self.res
    
    def change_directory(self, dest_dir):
        if dest_dir == "..":
            folder_arr = self.ui_path.split("/")
            new_path = "/"
            for folder in range(0, len(folder_arr)-2):
                new_path += folder_arr[folder] + "/"
            #Go back one folder
            self.ui_path = new_path
        else:                
            check_dir = self.ui_path + dest_dir + "/"
            if os.path.exists(check_dir):
                self.ui_path = check_dir
            else:
                print(f"Cannot change the director to {check_dir} because the path does not exist")
        return self.ui_path



"""
fol_actns_obj = folder_actions("/Users/aishwmkaryatalapuru/Documents/gS_wrksp")
fol_actns_obj.make_directory()
"""
        