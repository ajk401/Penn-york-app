import os

#creates idlist and staff files
def Create_first_run_files():
    if os.path.exists("datasheets") != True:
        os.mkdir("datasheets")
        with open("datasheets/idlist.csv", "x") as idlist:
            idlist.write("")
        with open("datasheets/stafflist.csv", "x") as stafflist:
            stafflist.write("type,age,first_name,last_name,\n")
    #else:
        #debug print statement, enable for output
        #print("datasheets already exists")


Create_first_run_files()
