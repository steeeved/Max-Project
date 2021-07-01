from tkinter import *
import os

def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, 'w')
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    Label(screen1, text = "Registration Successful", bg = "green", width = "30").pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("350x250")
    screen1.title("Register")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="please enter the given information", height = "2", width = "30")
    Label(screen1, text="", height = "2", width="30").pack()
    Label(screen1, text="Username * ", height='2', width='30').pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password * ", height='2', width='30').pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text='', height = "2", width="30").pack()
    Button(screen1, text="Submit", height="2", width='30', command = register_user).pack()

def login_verify():
    login = False
    username1 = username_verify.get()
    password1 = password_verify.get()
    list_of_dir = os.listdir()
    if username1 in list_of_dir:
        file = open (username1, "r")
        verify  = file.read().splitlines()
        if password1 in verify:
            print("Success")
        else:
            print("Wrong password")
    
    else:
        print("User not found ")


def login():
    global screen2
    global username_verify
    global password_verify   
    username_verify = StringVar()
    password_verify = StringVar()

    screen2 = Toplevel(screen)
    screen2.geometry("500x300")
    screen2.title("login")
    Label(screen2, text="Please enter the information to login ", height = "2", width="30").pack()
    Label(screen2, text="", height = "2", width="30").pack()
    Label(screen2, text="Username : ", height = "2", width = "30").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="Password : ", height = "2", width="30").pack()
    password_entry1 = Entry (screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text="", height="2", width="30").pack()
    Button(screen2, text="Login", height = "2", width="30", command = login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    Label(text="Tkinter Login").pack()
    Label(text="", height='2', width="30")
    Button(text="Login", height="2", width="30", bg="blue", command = login).pack()
    Label(text="", height='2', width="30").pack()
    Button(text="Register", height = "2", width = "30", bg="green", command = register).pack()
    screen.mainloop()

main_screen()