import tkinter as tk                # ---tkinter=python ki gul library // GUL = window,butter, label,entry box     
from tkinter import ttk   # as tk = short name (easy use) // ttk Themed Tkinter widgets
from tkinter import messagebox                       # INTERVIEW LINE := Tkinter is used to create GUL apllication in python.
import pymysql
#pymyaql , mysql.connector, sqlite3


 
win = tk.Tk()                     # ye main /root window banata hai. # saare widgets isi window ke ander aate hain..
win.geometry("1350x700+0+0")      # 1350 = window width  , 700 = window height , 0+0 = screen ke top-left se start
win.title("student management system")    # Title bar me app ka naam show hota hai 

title_label = tk.Label(win,text="student management system",font =("Arial",25),border = 12,relief = tk.GROOVE)  #label= text dikhane ke liya ,  win = parent window , font = font style & size , border = border thickness , relief-groove = border style
title_label.pack(side=tk.TOP,fill=tk.X)       # pack()= widget place karne ke liye  ,  top = upar side ,  fill=x =  left se right full width

detail_fram = tk.LabelFrame(win,text = "Enter Details", font=("Arial",20),bd=12,relief=tk.GROOVE)  #label frame -frame with heading  # student form ke field rakhne ke liye
detail_fram.place(x=20,y=90,width=420,height=575) # place() = exact position  * screen distance * width /height - frame size

data_frame =tk.Frame(win,bd=12,relief=tk.GROOVE)   # simple frame * future me table / records dekhane ke liye
data_frame.place(x=475,y=90,width=810,height=575)  # right side ka data  section 

#=======variables=======#

rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
fathersnm = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()

 
#==========ENTRY======#

rollno_lbl =tk.Label(detail_fram,text="rollno",font=('Arial',15)) # label= "roll no "text    
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)   # grid() - table- like layout , row =0, column=0 - position  * padx/pady - spacing 

rollno_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=rollno) # entry - user input field 
rollno_ent.grid(row=0,column=1,padx=2,pady=2)  # roll number type karne ke liye 


name_lbl =tk.Label(detail_fram,text="Name",font=('Arial',15))   # student ka naam input karne ke liye
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

class_lbl =tk.Label(detail_fram,text="Class",font=('Arial',15))  # studebt ki class ke liye 
class_lbl.grid(row=2,column=0,padx=2,pady=2)

class_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=2)

section_lbl =tk.Label(detail_fram,text="Section",font=('Arial',15))     
section_lbl.grid(row=3,column=0,padx=2,pady=2) 

section_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=section)
section_ent.grid(row=3,column=1,padx=2,pady=2) 

contact_lbl =tk.Label(detail_fram,text="Contact",font=('Arial',15))
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=2)


fathersnm_lbl =tk.Label(detail_fram,text="Father's Name",font=('Arial',15))
fathersnm_lbl.grid(row=5,column=0,padx=2,pady=2)

fathersnm_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=fathersnm)
fathersnm_ent.grid(row=5,column=1,padx=2,pady=2)

address_lbl =tk.Label(detail_fram,text="Address",font=('Arial',15))
address_lbl.grid(row=6,column=0,padx=2,pady=2)

address_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=2)

gender_lbl =tk.Label(detail_fram,text="Gender",font=('Arial',15))
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent = ttk.Combobox(detail_fram,font=('Arial',15),state="readonly",textvariable=gender)
gender_ent['value'] = ("Male","Female", "Other")
gender_ent.grid(row=7,column=1,padx=2,pady=2)


dob_lbl =tk.Label(detail_fram,text="D.O.B",font=('Arial',15))
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent =tk.Entry(detail_fram,bd=7,font=("Arial",15),textvariable=dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)

#+===============================================#

#========================================#
#========== function==================#

def fetch_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1",port=3308)
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows :
            student_table.insert('', tk.END ,values=row)
        conn.commit()
    conn.close()


def add_func():
    if rollno.get()=="" or name.get() == "" or class_var.get() =="":
       messagebox.showerror("Error!","Please fill all fields!")
    else:
         conn = pymysql.connect(host="localhost",user="root",password="",database="sms1",port=3308)
         curr = conn.cursor()
         curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),section.get(),contact.get(),fathersnm.get(),address.get(),gender.get(),dob.get()))
         conn.commit()
         conn.close()

         fetch_data()  #  This will fetch the data after adding (MEANS UPDATE)



def get_cursor(event):
    '''This fuction will fetch data of the selection row'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    contact.set(row[4])
    fathersnm.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])


def clear():
    '''This is function will update data accprding to user'''
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    fathersnm.set("")
    address.set("")
    gender.set("")
    dob.set("")







def UPDATE_func():
     ''' This fuction will updata data according to user '''
     conn = pymysql.connect(host="localhost",user="root",password="",database="sms1",port=3308) 
     curr = conn.cursor()
     curr.execute("UPDATE data set name=%s,class=%s,section=%s,contact=%s,fathersnm=%s,address=%s,gender=%s,dob=%s where rollno=%s",name.get(),class_var.get(),section.get(),contact.get(),fathersnm.get(),address.get(),gender.get(),dob.get(),rollno.get()) 
     conn.commit() 
     conn.close() 
     fetch_data() 
     clear()

 #delete_function 

def delete_func():
    if rollno.get()=="":
        messagebox.showerror("Error","Select record to delete")
    else:
        conn = pymysql.connect(host="localhost",user="root",password="",database="sms1",port=3308)
        curr = conn.cursor()
        curr.execute("DELETE FROM data WHERE rollno=%s",(rollno.get),)
        conn.commit()
        conn.close()
        fetch_data()
        clear()




#===========butters====================#


btn_frame = tk.Frame(detail_fram,bd=10,relief=tk.GROOVE)
btn_frame.place(x=20,y=390, width= 341 ,height= 130 )

add_btn = tk.Button(btn_frame,text="Add",bd=7,font=("Arial",13),width=15,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

UPDATE_btn = tk.Button(btn_frame,text="UPDATE",bd=7,font=("Arial",13),width=15,command=UPDATE_func)
UPDATE_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,text="Delete",bd=7,font=("Arial",13),width=15,command=delete_func)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,text="Clear",bd=7,font=("Arial",13),width=15,command=clear)
clear_btn.grid(row=1,column=1,padx=3,pady=2)



#=================================

#================Search===============#


search_frame = tk.Frame(data_frame,bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame,text="search",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=2,pady=2)

search_in = ttk.Combobox(search_frame,font=("Arial",14 ),state="readonly", textvariable=search_by)
search_in['values'] = ("Name","Roll No","Contact","Father's Name","Class","Section","D.O.B")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_lbl = tk.Button(search_frame,text="search",font=("Arial",13),bd=9,width=14)
search_lbl.grid(row=0,column=2,padx=12,pady=2)

showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=14)
showall_btn.grid(row=0,column=3,padx=12,pady=2)

#==============

#======== Database freame======

main_frame = tk.Frame(data_frame,bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

''' Name , Class , Section , Father's Name ,Address , Gender , dob '''

student_table = ttk.Treeview(main_frame, columns=("rollno","name","class","section","contact","father","address","gender","dob"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)


y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("rollno",text="rollno")
student_table.heading("name",text="Name")
student_table.heading("class",text="Class")
student_table.heading("section",text="Section")
student_table.heading("contact",text="Contact")
student_table.heading("father",text="Father")
student_table.heading("address",text="Address")
student_table.heading("gender",text="Gender")
student_table.heading("dob",text="D.O.B")

student_table['show']  = 'headings'

student_table.column("rollno",width=100)
student_table.column("name",width=100)
student_table.column("class",width=100)
student_table.column("section",width=100)
student_table.column("contact",width=100)
student_table.column("father",width=100)
student_table.column("address",width=100)
student_table.column("gender",width=100)
student_table.column("dob",width=150)

student_table.pack(fill=tk.BOTH,expand=True) 

fetch_data()

student_table.bind("<ButtonRelease-1>" ,get_cursor)




win.mainloop()   #  window ko continuous run karte hai   * button click , typing sab handle karta hai  * iske bina window close ho jaayegi