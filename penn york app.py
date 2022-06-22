# Imports
from tkinter import *
import random
import os
import csv


#variables
app_name = "Administration App "
Version_num = "0.02a"


#root definition
root = Tk()
root.title(app_name + " Version: " + Version_num)
root.geometry("960x540")


#Create_file definition
def Create_file():
    print("1")


#Create_first_run_files creates idlist and staff files on first startup
def Create_first_run_files():
    if os.path.exists("datasheets") != True:
        os.mkdir("datasheets")``
        with open("datasheets/file.csv", "x") as stafflist:
            stafflist.write("type,age,first_name,last_name,id,\n")


#id number generation
def generate_id(filename):
    id = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    with open(filename, "r") as file:
        stafflist_id = []
        stafflist_reader = csv.DictReader(stafflist)
        for line in stafflist_reader:
            stafflist_id.append(stafflist_reader['id'])
        while id in stafflist_id:
            id = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        return id
print(generate_id())


#selection button definition / pushing to screen
Create_new_file = Button(root, text="Create New File", padx=15, pady=15, command=Create_file)
Create_new_file.grid(row=1, column=0)


root.mainloop()
