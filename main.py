import os
import sys 
class gitSnap:
    def __init__(self):
        print("Welcome to gitSnap")
        cmd_args = sys.argv[1:]
        print(cmd_args)
        user_input = input("Resume working on an existing directory? [yes/no]").lower()
        if "yes" in user_input or "y" in user_input:
            ui_path = input("Please enter the path of the directory in the format (folder1/folder2/.../folderN) ")
            #Check if the entered path is valid or not
            if os.path.exists(ui_path):
                print(f"The given path '{ui_path}' does not exist or may not be valid. Please check for the case")
        else:
            #Create a new directory called 
            print("in the no group")

gs = gitSnap()


