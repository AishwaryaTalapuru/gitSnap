import os
import sys 
import re
from folder_actions import folder_actions
from file_actions import file_actions

class gitSnap:
    def __init__(self):
        #Initialising the ui_path, re_execute, no_trials
        self.ui_path = ""
        self.re_execute = True
        self.no_trials = 0
        self.home = ""
        #Re- running the program until the user enters the right path for 5 times
        while self.re_execute and self.no_trials <= 5:
            if len(sys.argv[1:]) > 0 and os.path.exists(sys.argv[1:][0]):
                #Reading the command line argument
                self.ui_path = sys.argv[1:][0]
            else:
                #Reading the path as user input
                self.ui_path = input(f"Please enter a valid, non- empty and existing path. Attempts remaining :  {5-self.no_trials} : ")
            #Decrementing the no of attempts after every failed attempt
            self.no_trials += 1
            #Re-calling the basic_preprocessing()
            self.re_execute = not self.basic_preprocessing()

    #Helper function for basic prerocessing like checking if the path entered is empty, invalid/non-existant
    def basic_preprocessing(self):
        self.res = False
        if len(self.ui_path) > 0:
            #prepending "/" if the user entered path does not have one
            if self.ui_path[0] != "/":
                self.ui_path = "/"+self.ui_path
            #appending "/" if the user entered path does not have one
            if self.ui_path[-1] != "/":
                self.ui_path +=  "/"
            #check for the path exists or not
            if os.path.exists(self.ui_path):
                print(f"The path is {self.ui_path}")
                self.res = self.intermediatory_preprocessing()
            else:
                #Error msg that gets printed if the path is invalid or non-existing
                print(f"The path {self.ui_path} is not valid or does not exist. Please check the correctness of the path")
        else:
            #Error msg that gets printed if the path is empty
            print("The entered path is empty. Please follow the format python main.py <actual path to the directory>")
        return self.res
    
    #Helper function for intermediatory prerocessing like checking if the path entered is empty, invalid/non-existant
    def intermediatory_preprocessing(self):
        self.res = False
        #Creating a default workspace called "gS_wrksp" 
        foldr_player_obj = folder_actions(self.ui_path + "gS_wrksp" + "/")
        self.res = foldr_player_obj.make_directory()
        if self.res:
            self.ui_path += "gS_wrksp" + "/"
            if self.home == "":
                self.home = self.ui_path
            cmd = input("CMD: ")
            while cmd != "Esc":
                cmd_arr = cmd.split(" ")
                operation = cmd_arr[0]
                if len(cmd_arr) > 1:
                    entity_name = cmd_arr[1]
                else:
                    entity_name = ""
                pattern = r'"(.*?)"'
                matches = re.findall(pattern, cmd)
                if len(matches)>0:
                    data = matches[0]
                else:
                    data = ""
                if operation == "mkdir":
                    foldr_player_obj = folder_actions(self.ui_path + entity_name + "/")
                    foldr_player_obj.make_directory()
                elif operation == "rmdir":
                    foldr_player_obj = folder_actions(self.ui_path + entity_name + "/")
                    foldr_player_obj.delete_directory()
                elif operation == "touch":
                    file_player_obj = file_actions(self.ui_path + entity_name, data)
                    file_player_obj.make_file()
                elif operation == "delete":
                    file_player_obj = file_actions(self.ui_path + entity_name, data)
                    file_player_obj.delete_file()
                elif operation == "cd":
                    if len(entity_name) == 0:
                        self.ui_path = self.home
                    else:
                        foldr_player_obj = folder_actions(self.ui_path)
                        self.ui_path = foldr_player_obj.change_directory(entity_name)
                    print(f"Present working directory is : {self.ui_path}")
                elif operation == "pwd":
                    print(f"Present working directory is : {self.ui_path}")
                else:
                    print("Invalid command. Please use --help option to know more")

                cmd = input("CMD: ")
            
            
        return self.res

        
          

gs = gitSnap()



