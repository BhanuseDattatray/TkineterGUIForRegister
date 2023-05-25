from tkinter import *
import os 
import mysql.connector

def clear_data():
    box1.delete(0,END)
    box2.delete(0,END)
    box3.delete(0,END)
    box1.focus()

def load_data():
    if (os.path.exists("DepartmentData.txt")):
        with open("DepartmentData.txt","r") as dta:
            for line in dta:
                lstbx.insert(END,line)

def Add_Emp():
    depid = box1.get()
    name = box2.get()
    salary = box3.get()
    fnloutput = depid+","+name+","+salary
    lstbx.insert(END,fnloutput)
    with open("DepartmentData.txt","a") as dta:
        dta.write(fnloutput)
        dta.write("\n")
    
    clear_data()
        
def Select_Record():
    clear_data()
    global index 
    index = lstbx.curselection()[0]
    activerecord = lstbx.get(ACTIVE)
    r = activerecord.split(",")
    id = box1.insert(0,r[0])
    name = box2.insert(0,r[1])
    salary = box3.insert(0,r[2])
    
def Delete_Record():
    lstbx.delete(ACTIVE)
    allitem = lstbx.get(0,END)
    print(allitem)
    with open("DepartmentData.txt","w") as dta:
        for item in allitem:
            dta.write(item)

def Update_Record():
    global index 
    rec = lstbx.delete(index)
    id = box1.get()
    name = box2.get()
    sal = box3.get()
    fnl = id+","+name+","+sal
    lst = lstbx.insert(index,fnl)
    allitems = lstbx.get(0,END)
    with open("DepartmentData.txt","w") as dta:
        for item in allitems:
            dta.write(item)
    clear_data()
            
if (__name__ == "__main__"):
    window = Tk()
    window.title("Employee Register")
    window.geometry("350x350")

    #------------------------
    frm1 = Frame(window)
    frm2 = Frame(window)
    frm3 = Frame(window)

    lbl1 = Label(frm1,text="Department Id")
    lbl2 = Label(frm1,text = "Employee Name")
    lbl3 = Label(frm1,text="Salary")

    box1 = Entry(frm1,width=30)
    box2 = Entry(frm1,width=30)
    box3 = Entry(frm1,width=30)

    #-----------------------------
    btn1 = Button(frm2,text="Add",command=Add_Emp,width=10)
    btn2 = Button(frm2,text="Select", command=Select_Record,width=10)
    btn3 = Button(frm2,text="Delete",command=Delete_Record,width=10)
    btn4 = Button(frm2,text="Update",command=Update_Record,width=10)

    lstbx = Listbox(frm3,width=53,height=15)
    #--------------------------------------
    frm1.pack()
    frm2.pack()
    frm3.pack()
    #---------------
    lbl1.grid(row=1,column=1)
    lbl2.grid(row=2,column=1)
    lbl3.grid(row=3,column=1)

    box1.grid(row=1,column=2)
    box2.grid(row=2,column=2)
    box3.grid(row=3,column=2)

    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=LEFT)

    lstbx.pack()
    load_data()
    window.mainloop()
