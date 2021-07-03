import sqlite3

# Customer Details Table
def TenantDetails():
    con=sqlite3.connect("RMS.db")
    cur =con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tenanttb(id INTEGER PRIMARY KEY, 
    	CustomerID integer,
        F_Name text,
        Surname text, 
        T_Address text, 
        P_Code text,
        Town text,
        D_Payment text,
        Deposit text
        )""")
    con.commit()
    con.close()

def _ViewData():
    con=sqlite3.connect("RMS.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM tenanttb")
    rows =cur.fetchall()
    con.close
    return rows

def _addtenantRecord(CustomerID, F_Name, Surname, T_Address, P_Code, Town, D_Payment, Deposit):
    con=sqlite3.connect("RMS.db")
    cur =con.cursor()
    cur.execute("INSERT INTO tenanttb VALUES (NULL, ?,?,?,?,?,?,?,?)",\
        (CustomerID, F_Name, Surname, T_Address, P_Code, Town, D_Payment, Deposit))
    con.commit()
    con.close()

def _deleteRec(id):
    con=sqlite3.connect("RMS.db")
    cur =con.cursor()
    cur.execute("DELETE FROM tenanttb WHERE id=?", (id,))
    con.commit()
    con.clos

def _searchData(CustomerID="", F_Name="",  Surname="", T_Address="", P_Code="", Town="", D_Payment="", Deposit=""):
    con=sqlite3.connect("RMS.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM tenanttb WHERE CustomerID=? OR F_Name=? OR  Surname=? OR T_Address=? OR P_Code=? OR Town=? OR  D_Payment=? OR \
            Deposit=? ", \
            (CustomerID, F_Name, Surname, T_Address, P_Code, Town, D_Payment, Deposit))
    rows = cur.fetchall()
    con.close()
    return rows

def _dataUpdate(id,CustomerID="", F_Name="",  Surname="", T_Address="", P_Code="", Town="", D_Payment="", Deposit=""):
    con=sqlite3.connect("RMS.db")
    cur =con.cursor()
    cur.execute("UPDATE tenanttb SET CustomerID=?, F_Name=?, Surname=?, T_Address=?, P_Code=?, Town=?, D_Payment=?, Deposit=?, WHERE id=?", \
        (CustomerID, F_Name, Surname, T_Address, P_Code, Town, D_Payment, Deposit, id))
    con.commit()
    con.close()






TenantDetails()