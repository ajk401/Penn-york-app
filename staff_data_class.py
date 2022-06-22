from tkinter import *
import sqlite3
import sys


root = Tk()
root.title('test')
root.iconbitmap('images/app logo.ico')
root.geometry("400x400")

# Databases

#create a Database or connect to one
connection = sqlite3.connect('datasheets/PennYorkCamp.db')

# create cursor
c = connection.cursor()

#create table
def make_table():
    c.execute("""CREATE TABLE staff (first_name text,last_name text,age integer,job text)""")

#create delete function
def delete():
    #connect to database
    connection = sqlite3.connect('datasheets/PennYorkCamp.db')
    c = connection.cursor()

    #delete entry
    c.execute("DELETE from staff WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)



    #end connection
    connection.commit()
    connection.close()

#Create submit function
def submit():
    connection = sqlite3.connect('datasheets/PennYorkCamp.db')
    c = connection.cursor()

    #insert into table
    c.execute("INSERT INTO staff VALUES (:f_name, :l_name, :age, :job)",
        {
            "f_name" : f_name.get(),
            "l_name" : l_name.get(),
            "age" : age.get(),
            "job" : job.get()
        })

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    #end connection
    connection.commit()
    connection.close()

def delete():
    #connect to database
    connection = sqlite3.connect('datasheets/PennYorkCamp.db')
    c = connection.cursor()

    #delete entry
    c.execute("DELETE from staff WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)



    #end connection
    connection.commit()
    connection.close()



#Create quit function
def quit():
    connection = sqlite3.connect('datasheets/PennYorkCamp.db')
    c = connection.cursor()

    exit()

    #end connection
    connection.commit()
    connection.close()



#create query function
def query():
    #establish connection
    connection = sqlite3.connect('datasheets/addressbook.db')
    c = connection.cursor()

    #query the Database
    c.execute("SELECT *, oid FROM staff")
    records = c.fetchall()
    #print(records)

    #Loop through all results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + str(record[6]) + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)


    #end connection
    connection.commit()
    connection.close()



def create_input_boxes():
    #create text boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(20, 0))
    l_name = Entry(root, width=30)
    l_name.grid(row=1, column=1)
    address = Entry(root, width=30)
    address.grid(row=2, column=1)
    city = Entry(root, width=30)
    city.grid(row=3, column=1)
    state = Entry(root, width=30)
    state.grid(row=4, column=1)
    zipcode = Entry(root, width=30)
    zipcode.grid(row=5, column=1)

    delete_box = Entry(root, width=30)
    delete_box.grid(row=9, column=1)

    #create text box labels
    f_name_label = Label(root, text="first_name")
    f_name_label.grid(row=0, column=0, pady=(20, 0))
    l_name_label = Label(root, text="last name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(root, text="address")
    address_label.grid(row=2, column=0)
    city_label = Label(root, text="city")
    city_label.grid(row=3, column=0)
    state_label = Label(root, text="state")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(root, text="zipcode")
    zipcode_label.grid(row=5, column=0)

    delete_box_label = Label(root, text="id number")
    delete_box_label.grid(row=9, column=0)

def create_buttons():
    #create submit button
    submit_btn = Button(root, text="add record to database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

    #create a query button
    query_btn = Button(root, text="show records", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    #create delete button
    query_btn = Button(root, text="delete record", command=delete)
    query_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    quit_btn = Button(root, text='quit', command=quit)
    quit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
