import tkinter.messagebox
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import db
import os

def _MainFunc():
    root = Tk()
    root.configure(bg = "navy blue")
    root.title("Rent Management")
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width,height))

    # Fuctions
    def _ClearData():
        _Customerid.delete(0, END)
        _Firstname.delete(0, END)
        _Surname.delete(0, END)
        _Address.delete(0, END)
        _Postalcode.delete(0, END)
        _Town.delete(0, END)
        _DownPayment.delete(0, END)
        _Deposit.delete(0, END)
        _Flat.delete(0, END)
        _House.delete(0, END)
        _Cost.delete(0, END)
        _Location.delete(0, END) 
        _Electricity.delete(0, END)
        _Water.delete(0, END)
        _Garbage.delete(0, END)
        _Tt.delete(0, END)
        _secentry.delete(0, END)

    def TenantRec(event):
        global sd
        searchStd = _secentry.curselection()[0]
        sd = _secentry.get(searchStd)

        _Customerid.delete(0, END)
        _Customerid.insert(END,sd[1])

        _Firstname.delete(0, END)
        _Firstname.insert(END,sd[2])

        _Surname.delete(0, END)
        _Surname.insert(END,sd[3])

        _Address.delete(0, END)
        _Address.insert(END,sd[4])

        _Postalcode.delete(0, END)
        _Postalcode.insert(END,sd[5])

        _Town.delete(0, END)
        _Town.insert(END,sd[6])

        _DownPayment.delete(0, END)
        _DownPayment.insert(END,sd[7])

        _Deposit.delete(0, END)
        _Deposit.insert(END,sd[8])

    def _exit():
        iExit = tkinter.messagebox.askyesno("Rent Management System", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

    def _ViewData():
        _secentry.delete(0, END)
        for row in db.viewData():
            _secentry.insert(END,row, str("")) 

    def _deleteRec():
        global sd
        if(len(_Customerid.get())!=0):
            db._deleteRec(sd[0])
            _ClearData()
            _ViewData()

    def _searchData():
        _secentry.delete(0, END)
        for row in db._searchData(_Customerid.get(), _Firstname.get(),_Surname.get(),_Address.get(),_Postalcode.get(),_Town.get(),_DownPayment.get(),_Deposit.get()):
            _secentry.insert(END, row, str(""))

    def _addtenantRecord():
        if(len(_Customerid.get())==0) or (len( _Firstname.get())==0) or (len(_Surname.get())==0) or (len(_Address.get())==0) or (len(_Postalcode.get())==0) or (len(_Town.get())==0) or (len(_DownPayment.get())==0) or (len(_Deposit.get())==0):
            messagebox.showinfo("Incomplete Data", "Please fill in all the fields")
        elif(len(_Customerid.get())!=0):
            db._addtenantRecord(_Customerid.get(), _Firstname.get(),_Surname.get(),_Address.get(),_Postalcode.get(),_Town.get(),_DownPayment.get(),_Deposit.get())
            _secentry.delete(0, END)
            _secentry.insert(END, (_Customerid.get(), _Firstname.get(),_Surname.get(),_Address.get(),_Postalcode.get(),_Town.get(),_DownPayment.get(),_Deposit.get()))

    def _dataUpdate():
        global sd
        if(len(_Customerid.get())!=0):
            db._deleteRec(sd[0])
        if(len(_Customerid.get())!=0):
            db._addtenantRecord((_Customerid.get(), _Firstname.get(),_Surname.get(),_Address.get(),_Postalcode.get(),_Town.get(),_DownPayment.get(),_Deposit.get()))
            _secentry.delete(0, END)
            _secentry.insert(END, (_Customerid.get(), _Firstname.get(),_Surname.get(),_Address.get(),_Postalcode.get(),_Town.get(),_DownPayment.get(),_Deposit.get()))

    # Frame Work
    _MainFrame = Frame(root,  bg="cadet blue")
    _MainFrame.grid()
    _titleframe = Frame(_MainFrame, bd=2, padx=54, pady=8, bg="navy blue", relief=RIDGE)
    _titleframe.pack(side=TOP)
    _buttons = Frame(_MainFrame, bd=2, padx=54, pady=8, bg="purple", relief=RIDGE)
    _buttons.pack(side=BOTTOM)
    _dataframe = Frame(_MainFrame, bd=2, padx=54, pady=8, bg="navy blue", relief=RIDGE)
    _dataframe.pack(side=BOTTOM)
    _primaryframe = Frame(_dataframe, bd=2, padx=54, pady=8, bg="navy blue", relief=RIDGE)
    _primaryframe.pack(side=LEFT)
    _secondaryframe = Frame(_dataframe, bd=2, padx=54, pady=8, bg="navy blue", relief=RIDGE)
    _secondaryframe.pack(side=RIGHT)
    _customerdetails = Frame(_primaryframe, bd=2, padx=54, pady=8, bg="purple", relief=RIDGE)
    _customerdetails.pack(side=TOP)
    _rentaldetails = Frame(_primaryframe, bd=2, padx=54, pady=8, bg="purple", relief=RIDGE)
    _rentaldetails.pack(side=LEFT)
    _utilitybills = Frame(_primaryframe, bd=2, padx=54, pady=8, bg="purple", relief=RIDGE)
    _utilitybills.pack(side=RIGHT)


    # Labels
    _title = Label(_titleframe, bg="navy blue", text="Rent Management System", font=("aerial", 25 ,"bold"))
    _title.grid(row=0, column=0)
    _costomerlabel = Label(_customerdetails, text="Customer Details", padx=2, pady=2, bg="purple",font=("aerial", 15 ,"bold"))
    _costomerlabel.grid(row=0, column=0, columnspan=5)
    _customerid = Label(_customerdetails, text="Customer Id", padx=2, pady=2, bg="purple")
    _customerid.grid(row=1, column=0)
    _firstname = Label(_customerdetails, text="First Name",padx=2, pady=2, bg="purple")
    _firstname.grid(row=2, column=0)
    _surname = Label(_customerdetails, text="Surname", padx=2, pady=2, bg="purple")
    _surname.grid(row=3, column=0)
    _address = Label(_customerdetails, text="Address", padx=2, pady=2, bg="purple")
    _address.grid(row=4, column=0)
    _postalcode = Label(_customerdetails, text="Postal Code", padx=2, pady=2, bg="purple")
    _postalcode.grid(row=1, column=2)
    _town = Label(_customerdetails, text="Town", padx=2, pady=2, bg="purple")
    _town.grid(row=2, column=2)
    _downpayment = Label(_customerdetails, text="DownPayment", padx=2, pady=2, bg="purple")
    _downpayment.grid(row=3, column=2)
    _deposit = Label(_customerdetails, text="Deposit", padx=2, pady=2, bg="purple")
    _deposit.grid(row=4, column=2)

    _rentallabel = Label(_rentaldetails, text="Rental Details", padx=2, pady=2, bg="purple",font=("aerial", 15 ,"bold"))
    _rentallabel.grid(row=0, column=0)
    _flat = Label(_rentaldetails, text="Flat", padx=2, pady=2, bg="purple")
    _flat.grid(row=1, column=0)
    _house = Label(_rentaldetails, text="House Number", padx=2, pady=2, bg="purple")
    _house.grid(row=2, column=0)
    _cost = Label(_rentaldetails, text="Cost", padx=2, pady=2, bg="purple")
    _cost.grid(row=3, column=0)
    _location = Label(_rentaldetails, text="Location", padx=2, pady=2, bg="purple")
    _location.grid(row=4, column=0)

    _utilitylabel = Label(_utilitybills, text="Utility Bills", padx=2, pady=2, bg="purple",font=("aerial", 15 ,"bold"))
    _utilitylabel.grid(row=0, column=0)
    _electricity = Label(_utilitybills, text="Electricity", padx=2, pady=2, bg="purple")
    _electricity.grid(row=1, column=0)
    _garbage = Label(_utilitybills, text="Garbage Bill", padx=2, pady=2, bg="purple")
    _garbage.grid(row=2, column=0)
    _water = Label(_utilitybills, text="Water Bill", padx=2, pady=2, bg="purple")
    _water.grid(row=3, column=0)
    _total = Label(_utilitybills, text="TOTALS:", padx=2, pady=2, bg="purple")
    _total.grid(row=4, column=0)

    # Entry Widgets
    _Customerid = Entry(_customerdetails, width=20)
    _Customerid.grid(row=1, column=1)
    _Firstname = Entry(_customerdetails, width=20)
    _Firstname.grid(row=2, column=1)
    _Surname = Entry(_customerdetails, width=20)
    _Surname.grid(row=3, column=1)
    _Address = Entry(_customerdetails, width=20)
    _Address.grid(row=4, column=1)
    _Postalcode = Entry(_customerdetails, width=20)
    _Postalcode.grid(row=1, column=3)
    _Town = Entry(_customerdetails, width=20)
    _Town.grid(row=2, column=3)
    _DownPayment = Entry(_customerdetails, width=20)
    _DownPayment.grid(row=3, column=3)
    _Deposit = Entry(_customerdetails, width=20)
    _Deposit.grid(row=4, column=3)

    _Flat = Entry(_rentaldetails, width=20)
    _Flat.grid(row=1, column=1)
    _House = Entry(_rentaldetails, width=20)
    _House.grid(row=2, column=1)
    _Cost = Entry(_rentaldetails, width=20)
    _Cost.grid(row=3, column=1)
    _Location = Entry(_rentaldetails, width=20)
    _Location.grid(row=4, column=1)

    _Electricity = Entry(_utilitybills, width=20)
    _Electricity.grid(row=1, column=1)
    _Garbage = Entry(_utilitybills, width=20)
    _Garbage.grid(row=2, column=1)
    _Water = Entry(_utilitybills, width=20)
    _Water.grid(row=3, column=1)
    _Tt = Entry(_utilitybills, width=10)
    _Tt.grid(row=4, column=1)

    scrollbar = Scrollbar(_secondaryframe)
    _secentry = Listbox(_secondaryframe, width=40, height=8, font=("Comfortaa Light", 15 ,"bold"),yscrollcommand=scrollbar.set) 
    _secentry.bind("<<ListboxSelect>>", TenantRec)
    _secentry.grid(row=0, column=0, padx=8)
    scrollbar.config(command = _secentry.yview)

    # Buttons
    _con = Button(_buttons, text="Confirm", font=("aerial", 10 ,"bold"), width=10, height=1, bd=4,command=_ViewData)
    _con.grid(row=0, column=0)
    _reset = Button(_buttons, text="Reset", font=("aerial", 10 ,"bold"), width=10, height=1, bd=4, command=_ClearData)
    _reset.grid(row=0, column=1)
    _exit = Button(_buttons, text="Exit", font=("aerial", 10 ,"bold"), width=10, height=1, bd=4,command=_exit)
    _exit.grid(row=0, column=2)

    _delete = Button(_buttons, text="Delete", font=("aerial", 10 ,"bold"), width=10, height=1, bd=4, command=_deleteRec)
    _delete.grid(row=0, column=3)
    _add = Button(_buttons, text="Add Records", font=("aerial", 10 ,"bold"), width=10, height=1, bd=4, command=_addtenantRecord)
    _add.grid(row=0, column=4)
    _search = Button(_buttons, text="Search", font=("aerial", 10 ,"bold"), width=10, height=1, bd=4, command=_searchData)
    _search.grid(row=0, column=5)
    _update = Button(_buttons, text="Update Records", font=("aerial", 10 ,"bold"), width=12, height=1, bd=4, command=_dataUpdate)
    _update.grid(row=0, column=6)


    root.mainloop()

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
            print("Success!!")
            login = True
        else:
            print("Wrong password")
    
    else:
        print("User not found ")

    if login == True:
        _MainFunc()

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