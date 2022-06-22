from tkinter import *

Version_num = "0.02a"


root = Tk()
root.title("Administration App Version: " + Version_num)

answer = Entry(root)
answer.pack()

def My_click():
    user_input = answer.get()
    print(user_input)

my_button = Button(root, text="Enter First Name", command=My_click)
my_button.pack()



root.mainloop()
