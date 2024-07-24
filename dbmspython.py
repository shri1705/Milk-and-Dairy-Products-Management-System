from tkinter import * 
import tkinter.font as f
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image    #pip install pillow
import pymysql
###### creating connection to mysql database #####
con=pymysql.connect(host="localhost",
                user="root",
                password="dharshini1109",
                database="MilkManagement")
##### creating cursor object using con object ##### 
cursor=con.cursor()
############################################### Admin login window ######################################################################
def openAdminLogin():
    btn_font=f.Font(family='Helvetica',size=16,weight='normal',slant='roman')
    ##### Admin window after logging in #####
    def openAdminWindow():
        ######checking if admin in database #####
        cursor.execute("SELECT COUNT(*) FROM Admin WHERE admin_username='"+username_entry.get()+"'")
        row=cursor.fetchall()
        cursor.execute("commit")
        if row[0][0]==0:
            messagebox.showinfo("Message","Admin not found !!!")
            return
        ##### checking if the user enters the password for login #####
        if password_entry.get()=="":
            messagebox.showinfo("Message","Enter your password")
        else:
            ##### selecting admin password from database to check the password validity #####
            cursor.execute("SELECT admin_password FROM Admin WHERE Admin_username='"+username_entry.get()+"'")
            rows=cursor.fetchall()
            cursor.execute("commit")
            for i in rows:
                ##### checking password #####
                if(i[0]==password_entry.get()):
                    ##### to clear the entered values in the login page for the next time #####
                    username_entry.delete(0,END)
                    password_entry.delete(0,END)
                    messagebox.showinfo("Message","Login Successful")
                    ##### opening admin window if the password is correct #####
                    adminwindow=Toplevel(adminlogin)
                    adminwindow.title("Admin Window")
                    adminwindow.minsize(1000,900)
                    adminwindow.state('zoomed')
                    adminwindow.config(bg='#9898F5')#CadetBlue1
                    #####Top frame that holds the heading of the admin window #####
                    topFrame=Frame(adminwindow,bd=10,relief=RIDGE,bg='#9898F5')
                    topFrame.pack(side=TOP)
                    ##### adding label to the top frame created #####
                    labelTitle=Label(topFrame,text='MILK AND DAIRY PRODUCTS MANAGEMENT SYSTEM',font=('arial',30,'bold',),bg='lavender',fg='#9898F5',width=51)
                    labelTitle.grid(row=0,column=0)
                    ##### creating a frame to add buttons #####
                    buttonFrame=Frame(adminwindow,bd=10,bg='lavender',width=1500,height=100,relief=RIDGE)
                    buttonFrame.place(x=25,y=90)
                    ##### creating frames for the buttons corespondingly #####
                    ##### frame for add user button #####
                    def AddUserFrame():
                        ##### creating frame #####
                        add_user_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        add_user_Frame.place(x=225,y=200)
                        ##### function to Insert user #####
                        def adduser():
                            ##### getting input from users #####
                            user_id=user_id_entry.get()
                            user_name=user_name_entry.get()
                            phn_num=phn_num_entry.get()
                            password=password_entry.get()
                            address=address_entry.get()
                            ##### checking constraints for password #####
                            checknum=0
                            checkalpha=0
                            checklower=0
                            checkcapital=0
                            for i in password:
                                if i.isnumeric():
                                    checknum=1
                            for i in password:
                                if i.isalpha():
                                    checkalpha=1
                            for i in password:
                                if i.islower():
                                    checklower=1
                            for i in password:
                                if i.isupper():
                                    checkcapital=1
                            checkspl_char=0
                            l=['@','!','#','$','%','^','&','*','_']
                            for i in password:
                                if i in l:
                                    checkspl_char=1
                            ##### checking for the user to input all the fields #####
                            if user_id=="" or user_name=="" or phn_num=="" or password=="":
                                messagebox.showinfo("Insert Status","All fields are required for adding a user")
                            else:
                                ##### checking for valid phone number #####
                                if len(phn_num)!=10:
                                    messagebox.showinfo("Insert Status","Enter valid phone number")
                                ##### checking for valid username #####
                                elif (user_name.isalpha()==False):
                                    messagebox.showinfo("Insert Status","Enter valid username")
                                ##### checking for strong passsword #####
                                elif ((len(password)<8) or(checknum==0)  or (checkspl_char==0) or (checkcapital==0) or (checkalpha==0)or(checklower==0)):
                                    messagebox.showinfo("Insert Status","Passwords must be atleast 8 characters,should contain atleast a special character,capital letter and a number")
                                ##### checking for valid user id #####
                                elif user_id.isnumeric()==False:
                                    messagebox.showinfo("Insert Status","Enter valid user id")
                                ##### Inserting if all values are correct #####
                                else:
                                    cursor.execute("Insert INTO User VALUES("+user_id+",'"+user_name+"','"+password+"',"+phn_num+",'"+address+"')")
                                    cursor.execute("commit")
                                   ##### clearing the value in the entry field for next user entry #####
                                    user_id_entry.delete(0,END)
                                    user_name_entry.delete(0,END)
                                    phn_num_entry.delete(0,END)
                                    password_entry.delete(0,END)
                                    address_entry.delete(0,END)
                                    messagebox.showinfo("Insert Status","User Added !!!") 
                        ##### placing label in the frame for user convience #####
                        txt='Add User'
                        heading=Label(add_user_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry for user id #####
                        user_id_label=Label(add_user_Frame,text='User Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        user_id_label.place(x=50,y=75)               
                        user_id_entry=Entry(add_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        user_id_entry.place(x=200,y=75,width=230,height=35)
                        ##### creating label and entry for user name #####
                        user_name_label=Label(add_user_Frame,text='User Name ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        user_name_label.place(x=50,y=130)               
                        user_name_entry=Entry(add_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        user_name_entry.place(x=200,y=130,width=230,height=35)
                        ##### creating label and entry for phone number #####
                        phn_num_label=Label(add_user_Frame,text='Phone Num  ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        phn_num_label.place(x=50,y=185)               
                        phn_num_entry=Entry(add_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        phn_num_entry.place(x=200,y=185,width=230,height=35)
                        ##### creating label and entry for password #####
                        password_label=Label(add_user_Frame,text='Password ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        password_label.place(x=50,y=240)               
                        password_entry=Entry(add_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        password_entry.place(x=200,y=240,width=230,height=35)
                        ##### creating label and entry for address #####
                        address_label=Label(add_user_Frame,text='Address ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        address_label.place(x=50,y=295)               
                        address_entry=Entry(add_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        address_entry.place(x=200,y=295,width=230,height=35)
                        ##### creating button for add operation #####
                        add_btn=Button(add_user_Frame,text='ADD',bd='5',cursor='hand2',command=adduser,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        add_btn.place(x=300,y=350)
                    ##### frame for delete user button #####
                    def DelUserFrame():
                        ##### creating frame #####
                        del_user_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        del_user_Frame.place(x=225,y=200)
                        ##### function to delete user #####
                        def deluser():
                            ##### input from user #####
                            user_id=user_id_entry.get()
                            if user_id.isnumeric()==False:
                                    messagebox.showinfo("Delete Status","Enter valid user Id!!!")
                                    return
                            ##### to check if the user is present or not in the records #####
                            cursor.execute("SELECT COUNT(*) FROM User WHERE User_id="+user_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")
                            ##### checking if the user id is entered #####
                            if user_id=="":
                                messagebox.showinfo("Delete Status","Enter user Id")
                            ##### deleting valid user id #####
                            elif(user_id):
                                if(rows[0][0]==0):
                                    messagebox.showinfo("Delete Status","User Not Found")
                                else:
                                    cursor.execute("DELETE FROM User WHERE User_id= "+user_id)
                                    cursor.execute("commit")
                                    ##### clearing the value in the entry field for next user entry #####
                                    user_id_entry.delete(0,END)
                                    messagebox.showinfo("Delete Status","User Deleted !!!")                          
                        ##### placing label in the frame for user convience #####
                        txt='Delete User'
                        heading=Label(del_user_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry for user id to be deleted #####
                        user_id_label=Label(del_user_Frame,text='User Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        user_id_label.place(x=50,y=75)               
                        user_id_entry=Entry(del_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        user_id_entry.place(x=200,y=75,width=230,height=35)
                        ##### creating button for delete operation #####
                        del_btn=Button(del_user_Frame,text='DELETE',bd='5',cursor='hand2',command=deluser,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        del_btn.place(x=200,y=200)
                    ##### frame for update user button #####
                    def UpdateUserFrame():
                        ##### creating frame #####
                        update_user_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        update_user_Frame.place(x=225,y=200)
                        ##### function to update user ######
                        def updateuser():
                            ##### getting input from users #####
                            user_id=user_id_entry.get()
                            password=new_password_entry.get()
                            ##### checking for valid user id #####
                            if user_id.isnumeric()==False:
                                messagebox.showinfo("Update Status","Enter valid user id")
                                return
                            ##### check if the users is present in the record #####
                            cursor.execute("SELECT COUNT(*) FROM User WHERE User_id="+user_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")
                            ##### checking constraints for password #####
                            checknum=0
                            checkalpha=0
                            checklower=0
                            checkcapital=0
                            for i in password:
                                if i.isnumeric():
                                    checknum=1
                            for i in password:
                                if i.isalpha():
                                    checkalpha=1
                            for i in password:
                                if i.islower():
                                    checklower=1
                            for i in password:
                                if i.isupper():
                                    checkcapital=1
                            checkspl_char=0
                            l=['@','!','#','$','%','^','&','*','_']
                            for i in password:
                                if i in l:
                                    checkspl_char=1
                            ##### checking for the user to input all the fields #####
                            if user_id=="" or password=="":
                                messagebox.showinfo("Update Status","All fields are required to update a user")
                            else: 
                                if(rows[0][0]==0):
                                    messagebox.showinfo("Update Status","User Not Found")                             
                                ##### checking for strong passsword #####
                                elif ((len(password)<8) or(checknum==0)  or (checkspl_char==0) or (checkcapital==0) or (checkalpha==0)or(checklower==0)):
                                    messagebox.showinfo("Update Status","Passwords must be atleast 8 characters,should contain atleast a special character,capital letter and a number")
                                ##### Updating if all values are correct #####
                                else:
                                    cursor.execute("UPDATE User SET User_Password='"+password+"'WHERE User_id="+user_id)
                                    cursor.execute("commit")
                                   ##### clearing the value in the entry field for next user entry #####
                                    user_id_entry.delete(0,END)
                                    new_password_entry.delete(0,END)
                                    messagebox.showinfo("Update Status","User Updated !!!")
                        ##### placing label in the frame for user convience #####
                        txt='Update User'
                        heading=Label(update_user_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry field for user_id to be updated #####
                        user_id_label=Label(update_user_Frame,text='User Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        user_id_label.place(x=50,y=75)               
                        user_id_entry=Entry(update_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        user_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering new password #####
                        new_password_label=Label(update_user_Frame,text='New Password ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        new_password_label.place(x=50,y=130)               
                        new_password_entry=Entry(update_user_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        new_password_entry.place(x=225,y=130,width=230,height=35)
                        ##### creating button for update operation #####
                        update_btn=Button(update_user_Frame,text='UPDATE',bd='5',cursor='hand2',command=updateuser,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        update_btn.place(x=300,y=300)
                    ##### frame for add worker button #####
                    def AddWorkerFrame():
                        ##### creating frame #####
                        add_worker_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        add_worker_Frame.place(x=225,y=200)
                        ##### function to add worker #####
                        def addworker():
                            ##### user input #####
                            id=worker_id_entry.get()
                            name=worker_name_entry.get()
                            phnnum=phn_num_entry.get()
                            mail_id=mail_id_entry.get()
                            password=password_entry.get()
                            salary=salary_entry.get()
                            worktype=workchoosen.get()
                            address=address_entry.get()
                            ##### checking constraints for password #####
                            checknum=0
                            checkalpha=0
                            checklower=0
                            checkcapital=0
                            for i in password:
                                if i.isnumeric():
                                    checknum=1
                            for i in password:
                                if i.isalpha():
                                    checkalpha=1
                            for i in password:
                                if i.islower():
                                    checklower=1
                            for i in password:
                                if i.isupper():
                                    checkcapital=1
                            checkspl_char=0
                            l=['@','!','#','$','%','^','&','*','_']
                            for i in password:
                                if i in l:
                                    checkspl_char=1
                            ##### checking valid inputs #####
                            if id==""or name=="" or password=="" or worktype=="" or phnnum=="" or mail_id=="" or salary=="" or address=="":
                                messagebox.showinfo("Insert Status","All fields are required for insertion")
                            elif id.isnumeric()==False:
                                messagebox.showinfo("Insert Status","Enter valid user id")
                            elif name.isalpha()==False:
                                messagebox.showinfo("Insert Status","Enter valid user name")
                            elif len(phnnum)!=10:
                                messagebox.showinfo("Insert Status","Enter valid phn number")
                            elif((mail_id.find('.')==-1)or(mail_id.find('@'))==-1):
                                messagebox.showinfo("Insert Status","Enter valid mail id")
                            elif ((len(password)<8) or(checknum==0)  or (checkspl_char==0) or (checkcapital==0) or (checkalpha==0)or(checklower==0)):
                                messagebox.showinfo("Insert Status","Passwords must be atleast 8 characters,should contain atleast a special character,capital letter and a number")                           
                            else:
                                cursor.execute("Insert INTO Worker VALUES("+id+",'"+name+"','"+password+"',"+salary+",'"+mail_id+"','"+worktype+"','"+address+"',"+phnnum+")")
                                cursor.execute("commit")
                                ##### freeing entry field for next entry #####
                                worker_id_entry.delete(0,END)
                                worker_name_entry.delete(0,END)
                                phn_num_entry.delete(0,END)
                                mail_id_entry.delete(0,END)
                                password_entry.delete(0,END)
                                salary_entry.delete(0,END)
                                workchoosen.delete(0,END)
                                address_entry.delete(0,END)
                                messagebox.showinfo("Insert Status","Worker Added!!!")                         
                        ##### placing label in the frame for user convience #####
                        txt='Add Worker'
                        heading=Label(add_worker_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry for worker id #####
                        worker_id_label=Label(add_worker_Frame,text='Worker Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        worker_id_label.place(x=50,y=75)               
                        worker_id_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        worker_id_entry.place(x=200,y=75,width=230,height=35)
                        ##### creating label and entry for worker name #####
                        worker_name_label=Label(add_worker_Frame,text='Worker Name ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        worker_name_label.place(x=50,y=130)               
                        worker_name_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        worker_name_entry.place(x=200,y=130,width=230,height=35)
                        ##### creating label and entry for phone number #####
                        phn_num_label=Label(add_worker_Frame,text='Phone Num  ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        phn_num_label.place(x=50,y=185)               
                        phn_num_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        phn_num_entry.place(x=200,y=185,width=230,height=35)
                        ##### creating label and entry for password #####
                        password_label=Label(add_worker_Frame,text='Password ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        password_label.place(x=50,y=240)               
                        password_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        password_entry.place(x=200,y=240,width=230,height=35)
                        ##### creating label and entry for salary #####
                        salary_label=Label(add_worker_Frame,text='Salary ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        salary_label.place(x=50,y=295)               
                        salary_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        salary_entry.place(x=200,y=295,width=230,height=35)
                        ##### creating label and entry for worker type #####
                        worker_type_label=Label(add_worker_Frame,text='Worker type',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        worker_type_label.place(x=50,y=350)               
                        ##### creating combobox #####
                        n =StringVar()
                        workchoosen = ttk.Combobox(add_worker_Frame, width = 27, textvariable = n)
                        # Adding combobox drop down list
                        workchoosen['values'] = (' FeedMonitor',' CareTaker',)
                        workchoosen.place(x=200,y=350,width=230,height=35)
                        ##### creating label and entry for address #####
                        address_label=Label(add_worker_Frame,text='Address ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        address_label.place(x=50,y=405)               
                        address_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        address_entry.place(x=200,y=405,width=230,height=35)
                        ##### creating label and entry for mail id #####
                        mail_id_label=Label(add_worker_Frame,text='Mail id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        mail_id_label.place(x=50,y=460)               
                        mail_id_entry=Entry(add_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        mail_id_entry.place(x=200,y=460,width=230,height=35)
                        ##### creating add button for add operation #####
                        add_btn=Button(add_worker_Frame,text='ADD',bd='5',cursor='hand2',command=addworker,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        add_btn.place(x=400,y=500)                    
                    ##### frame for delete worker button #####
                    def DelWorkerFrame():
                        ##### creating frame #####
                        del_worker_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        del_worker_Frame.place(x=225,y=200)
                        ##### function to delete worker #####
                        def delworker():
                            ##### input from user #####
                            worker=worker_id_entry.get()
                            if worker.isnumeric()==False:
                                    messagebox.showinfo("Delete Status","Enter valid Worker Id!!!")
                                    return
                            ##### to check if the worker is present or not in the records #####
                            cursor.execute("SELECT COUNT(*) FROM Worker WHERE Worker_id="+worker_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")
                            ##### checking if the worker id is entered #####
                            if worker=="":
                                messagebox.showinfo("Delete Status","Enter Worker Id")
                            ##### deleting valid worker id #####
                            elif(worker):
                                if(rows[0][0]==0):
                                    messagebox.showinfo("Delete Status","Worker Not Found")
                                else:
                                    cursor.execute("DELETE FROM Worker WHERE Worker_id= "+worker)
                                    cursor.execute("commit")
                                    ##### clearing the value in the entry field for next user entry #####
                                    worker_id_entry.delete(0,END)
                                    messagebox.showinfo("Delete Status","Worker Deleted !!!")
                        ##### placing label in the frame for user convience #####
                        txt='Delete Worker'
                        heading=Label(del_worker_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry for worker id to be deleted #####
                        worker_id_label=Label(del_worker_Frame,text='Worker Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        worker_id_label.place(x=50,y=75)               
                        worker_id_entry=Entry(del_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        worker_id_entry.place(x=200,y=75,width=230,height=35)
                        ##### creating delete button for delete operation #####
                        del_btn=Button(del_worker_Frame,text='DELETE',bd='5',cursor='hand2',command=delworker,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        del_btn.place(x=200,y=200)
                    ##### frame for update worker button #####
                    def UpdateWorkerFrame():
                        update_worker_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        update_worker_Frame.place(x=225,y=200) 
                        ##### function to update worker #####
                        def updateworker():
                            ##### getting input from users #####
                            worker_id=worker_id_entry.get()
                            salary=salary_entry.get()
                            ##### checking for valid Worker id #####
                            if worker_id.isnumeric()==False:
                                messagebox.showinfo("Update Status","Enter valid Worker id")
                                return
                            ##### check if the Worker is present in the record #####
                            cursor.execute("SELECT COUNT(*) FROM Worker WHERE Worker_id="+worker_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")                           
                            ##### checking for the user to input all the fields #####
                            if worker_id=="" or salary=="":
                                messagebox.showinfo("Update Status","All fields are required to update a user")
                            else: 
                                if(rows[0][0]==0):
                                    messagebox.showinfo("Update Status","Worker Not Found")                             
                                ##### Updating if all values are correct #####
                                else:
                                    cursor.execute("UPDATE Worker SET salary='"+salary+"'WHERE Worker_id="+worker_id)
                                    cursor.execute("commit")
                                   ##### clearing the value in the entry field for next user entry #####
                                    worker_id_entry.delete(0,END)
                                    salary_entry.delete(0,END)
                                    messagebox.showinfo("Update Status","Worker Updated !!!")
                        ##### placing label in the frame for user convience #####
                        txt='Update Worker'
                        heading=Label(update_worker_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry for worker id to be updated #####
                        worker_id_label=Label(update_worker_Frame,text='Worker Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        worker_id_label.place(x=50,y=75)               
                        worker_id_entry=Entry(update_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        worker_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry for salary #####
                        salary_label=Label(update_worker_Frame,text='Salary ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        salary_label.place(x=50,y=130)               
                        salary_entry=Entry(update_worker_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        salary_entry.place(x=225,y=130,width=230,height=35)
                        ##### creating update button for update operation #####
                        update_btn=Button(update_worker_Frame,text='UPDATE',bd='5',cursor='hand2',command=updateworker,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        update_btn.place(x=300,y=300)
                    ##### frame for edit product button #####
                    def EditProductFrame():
                        ##### creating frame #####
                        edit_product_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        edit_product_Frame.place(x=225,y=200)
                        ##### function to edit product #####
                        def editproduct():
                            ##### input from admin #####
                            p=productchoosen.get()
                            qty=qty_entry.get()
                            price=price_entry.get()
                            ##### updating in database #####
                            cursor.execute("UPDATE Product SET Quantity_avlb='"+qty+"'WHERE Product_id="+p)
                            cursor.execute("UPDATE Product SET Price='"+price+"'WHERE Product_id="+p)
                            cursor.execute("COMMIT")
                            ##### clearing the entry field for next entry #####
                            productchoosen.delete(0,END)
                            qty_entry.delete(0,END)
                            price_entry.delete(0,END)
                            messagebox.showinfo("Update Status","Product Edited !!!")                       
                        ##### function to view product #####
                        def viewproduct():
                            ##### creating frame #####
                            view_product_Frame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                            view_product_Frame.place(x=225,y=200)
                            ##### instance of style widget #####
                            style = ttk.Style()
                            style.theme_use('clam')
                            ##### creating tree frame to display user details #####
                            tree =ttk.Treeview(view_product_Frame, column=("c1", "c2","c3","c4"), show='headings', height=26)
                            ##### aligning columns #####
                            tree.column("# 1", anchor=CENTER)
                            tree.heading("# 1", text="Product ID")
                            tree.column("# 2", anchor=CENTER)
                            tree.heading("# 2", text="Product Name")
                            tree.column("# 3", anchor=CENTER)
                            tree.heading("# 3", text="Quantity avlb")
                            tree.column("# 4", anchor=CENTER)
                            tree.heading("# 4", text="Price ")
                            tree.place(x=100,y=0)
                            ##### fetching values from the database and displaying in the frame #####
                            cursor.execute("SELECT * FROM Product")
                            res=cursor.fetchall()
                            for i in res:
                                tree.insert(parent='',index='end',values=(i[0],i[1],i[2],i[3]))
                            cursor.execute("commit")
                        ##### listing the products available #####
                        Product_id_label=Label(edit_product_Frame,text='Product Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id_label.place(x=550,y=75)
                        Product_name_label=Label(edit_product_Frame,text='Product Name ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name_label.place(x=725,y=75)
                        Product_id1_label=Label(edit_product_Frame,text='1 ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id1_label.place(x=550,y=130)
                        Product_name1_label=Label(edit_product_Frame,text='Milk ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name1_label.place(x=725,y=130)
                        Product_id2_label=Label(edit_product_Frame,text='2 ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id2_label.place(x=550,y=185)
                        Product_name2_label=Label(edit_product_Frame,text='Curd ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name2_label.place(x=725,y=185)
                        Product_id3_label=Label(edit_product_Frame,text='3 ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id3_label.place(x=550,y=240)
                        Product_name3_label=Label(edit_product_Frame,text='Butter ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name3_label.place(x=725,y=240)
                        Product_id4_label=Label(edit_product_Frame,text='4 ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id4_label.place(x=550,y=295)
                        Product_name4_label=Label(edit_product_Frame,text='Cheese ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name4_label.place(x=725,y=295)
                        Product_id5_label=Label(edit_product_Frame,text='5 ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id5_label.place(x=550,y=350)
                        Product_name5_label=Label(edit_product_Frame,text='Paneer ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name5_label.place(x=725,y=350)
                        Product_id6_label=Label(edit_product_Frame,text='6 ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_id6_label.place(x=550,y=405)
                        Product_name6_label=Label(edit_product_Frame,text='Ghee ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        Product_name6_label.place(x=725,y=405)
                        ##### placing label in the frame for user convience #####
                        txt='Edit Product'
                        heading=Label(edit_product_Frame,text=txt,font=('Helvetica',20,'italic'),bg='#9898F5',fg='lavender')
                        heading.place(x=50,y=20,width=200,height=30)
                        ##### creating label and entry field for entering product id to be editted #####
                        edit_product_label=Label(edit_product_Frame,text='Product Id ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        edit_product_label.place(x=50,y=75)             
                        # Combobox creation
                        n = int()
                        productchoosen = ttk.Combobox(edit_product_Frame, width = 27, textvariable = n)
                        # Adding combobox drop down list
                        productchoosen['values'] = ('1','2','3','4','5','6') 
                        productchoosen.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering price ##### 
                        price_label=Label(edit_product_Frame,text='Price ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        price_label.place(x=50,y=130)               
                        price_entry=Entry(edit_product_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        price_entry.place(x=225,y=130,width=230,height=35) 
                        ##### creating label and entry field for entering quantity #####
                        qty_label=Label(edit_product_Frame,text='Quantity ',font=('Helvetica',17,'italic'),bg='#9898F5',fg='lavender')
                        qty_label.place(x=50,y=185)               
                        qty_entry=Entry(edit_product_Frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                        qty_entry.place(x=225,y=185,width=230,height=35)
                        ##### creating edit button for edit operations #####
                        edit_btn=Button(edit_product_Frame,text='EDIT',bd='5',cursor='hand2',command=editproduct,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        edit_btn.place(x=250,y=300)
                        ##### creating edit button for edit operations #####
                        view_btn=Button(edit_product_Frame,text='VIEW',bd='5',cursor='hand2',command=viewproduct,font=btn_font,width=20,bg='lavender',fg='#9898F5')
                        view_btn.place(x=250,y=370)
                    def ViewUserFrame():
                        ##### creating frame #####
                        viewuserFrame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        viewuserFrame.place(x=225,y=200)
                        ##### instance of style widget #####
                        style = ttk.Style()
                        style.theme_use('clam')
                        ##### creating tree frame to display user details #####
                        tree =ttk.Treeview(viewuserFrame, column=("c1", "c2","c3","c4"), show='headings', height=26)
                        ##### aligning columns #####
                        tree.column("# 1", anchor=CENTER)
                        tree.heading("# 1", text="User ID")
                        tree.column("# 2", anchor=CENTER)
                        tree.heading("# 2", text="User Name")
                        tree.column("# 3", anchor=CENTER)
                        tree.heading("# 3", text="Password ")
                        tree.column("# 4", anchor=CENTER)
                        tree.heading("# 4", text="Phone number ")                    
                        tree.place(x=100,y=0)
                        ##### fetching values from the database and displaying in the frame #####
                        cursor.execute("SELECT * FROM User")
                        res=cursor.fetchall()
                        for i in res:
                            tree.insert(parent='',index='end',values=(i[0],i[1],i[2],i[3]))
                        cursor.execute("commit")
                    def ViewWorkerFrame():
                        ##### creating frame #####
                        viewworkerFrame=Frame(adminwindow,width=1030,height=575,bg='#9898F5',bd=10,relief=RIDGE)
                        viewworkerFrame.place(x=225,y=200)
                        ##### instance of style widget #####
                        style = ttk.Style()
                        style.theme_use('clam')
                        ##### creating tree frame to display worker details #####
                        tree =ttk.Treeview(viewworkerFrame, column=("c1", "c2","c3","c4","c5"), show='headings', height=26)
                        ##### aligning columns #####
                        tree.column("# 1", anchor=CENTER)
                        tree.heading("# 1", text="Worker ID")
                        tree.column("# 2", anchor=CENTER)
                        tree.heading("# 2", text="Worker Name")
                        tree.column("# 3", anchor=CENTER)
                        tree.heading("# 3", text="Worker Type")
                        tree.column("# 4", anchor=CENTER)
                        tree.heading("# 4", text="Password ")
                        tree.column("# 5", anchor=CENTER)
                        tree.heading("# 5", text="Salary")                   
                        tree.place(x=0,y=0)
                        ##### fetching values from the database and displaying in the frame #####
                        cursor.execute("SELECT * FROM Worker")
                        res=cursor.fetchall()
                        for i in res:
                            tree.insert(parent='',index='end',values=(i[0],i[1],i[5],i[2],i[3]))
                        cursor.execute("commit")                                     
                    ##### creating and adding buttons to frame #####
                    ##### add button to add user #####
                    add_user_btn=Button(buttonFrame,text='Add User',bd='3',cursor='hand2',command=AddUserFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    add_user_btn.place(x=5,y=20)                   
                    ##### delete button to delete user #####
                    del_user_btn=Button(buttonFrame,text='Delete User',bd='3',cursor='hand2',command=DelUserFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    del_user_btn.place(x=150,y=20)
                    ##### update button to update user #####
                    update_user_btn=Button(buttonFrame,text='Update User',bd='3',cursor='hand2',command=UpdateUserFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    update_user_btn.place(x=295,y=20)
                    ##### add button to add worker #####
                    add_worker_btn=Button(buttonFrame,text='Add Worker',bd='3',cursor='hand2',command=AddWorkerFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    add_worker_btn.place(x=440,y=20)
                    ##### delete button to delete worker #####
                    del_worker_btn=Button(buttonFrame,text='DeleteWorker',bd='3',cursor='hand2',command=DelWorkerFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    del_worker_btn.place(x=585,y=20)
                    ##### update button to update worker #####
                    update_worker_btn=Button(buttonFrame,text='UpdateWorker',bd='3',cursor='hand2',command=UpdateWorkerFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    update_worker_btn.place(x=730,y=20)
                    ##### edit button to edit worker #####
                    edit_product_btn=Button(buttonFrame,text='Edit Product',bd='3',cursor='hand2',command=EditProductFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    edit_product_btn.place(x=875,y=20)
                    ##### button to view user details #####
                    user_details_btn=Button(buttonFrame,text='UserDetails',bd='3',cursor='hand2',command=ViewUserFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    user_details_btn.place(x=1020,y=20)
                    ##### button to view worker details #####
                    worker_details_btn=Button(buttonFrame,text='WorkerDetails',bd='3',cursor='hand2',command=ViewWorkerFrame,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    worker_details_btn.place(x=1165,y=20)
                    ##### button to logout #####
                    logout_btn=Button(buttonFrame,text='Logout',bd='3',cursor='hand2',command=adminwindow.destroy,font=btn_font,width=10,bg='#9898F5',fg='lavender')
                    logout_btn.place(x=1310,y=20)              
                    break
            else:
                ##### showing warning message for invalid password #####
                messagebox.showwarning("Message","Invalid password")
    ##### admin login window #####
    adminlogin = Toplevel(root)
    adminlogin.title("Admin login page")
    adminlogin.minsize(1000,900)
    adminlogin.state('zoomed')
    ##### background image #####
    bg_frame=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\bg5.jpg")
    photo=ImageTk.PhotoImage(bg_frame)
    bg_panel=Label(adminlogin,image=photo)
    bg_panel.image=photo
    bg_panel.pack(fill='both',expand='yes')
    ##### login frame #####
    ##### creating a login frame #####
    login_frame=Frame(adminlogin,width='900',height=600)
    login_frame.place(x=600,y=125)
    ##### giving a heading for a login frame #####
    txt='ADMIN LOGIN'
    txt1='MILK AND DAIRY PRODUCTS MANAGEMENT'
    heading=Label(login_frame,text=txt,font=('Helvetica',22,'italic'),fg='black')
    heading1=Label(login_frame,text=txt1,font=('Helvetica',25,'italic'),fg='black')
    heading1.place(x=5,y=5,width=750,height=30)
    heading.place(x=10,y=50,width=300,height=30)   
    ##### placing a image in the login frame #####
    sign_in_image=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\s1.jpg")
    photo=ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label=Label(login_frame,image=photo)
    sign_in_image_label.image=photo
    sign_in_image_label.place(x=620,y=50)
    #####placing 'sign in 'text #####
    sign_in_label=Label(login_frame,text='Sign In',fg='black',font=('Helvetica',17,'italic'))
    sign_in_label.place(x=635,y=175)
    ##### creating username label #####
    username_label=Label(login_frame,text='Username',font=('Helvetica',17,'italic'),fg='black')
    username_label.place(x=475,y=225)
    ##### creating textfield for username entry #####
    username_entry=Entry(login_frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
    username_entry.place(x=600,y=225,width=230,height=35)
    ##### creating password label #####
    password_label=Label(login_frame,text='Password',font=('Helvetica',17,'italic'),fg='black')
    password_label.place(x=475,y=300)
    ##### creating textfield for password entry #####
    password_entry=Entry(login_frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
    password_entry.place(x=600,y=300,width=230,height=35)
    ##### login button creation #####
    login_btn=Button(login_frame,text='Login',bd='5',cursor='hand2',command=openAdminWindow,font=btn_font,width=20)
    login_btn.place(x=545,y=370)
############################################## User login page #############################################################################################
def openUserLogin():
    btn_font=f.Font(family='Helvetica',size=16,weight='normal',slant='roman')
    ##### creating user window #####
    def openUserWindow():
        ######checking if user in database #####
        cursor.execute("SELECT COUNT(*) FROM User WHERE user_name='"+username_entry.get()+"'")
        row=cursor.fetchall()
        cursor.execute("commit")
        if row[0][0]==0:
            messagebox.showinfo("Message","User not found !!!")
            return
        ##### checking if the user enters the password for login #####
        if password_entry.get()=="":
            messagebox.showinfo("Message","Enter your password")
        else:
            ##### selecting admin password from database to check the password validity #####
            cursor.execute("SELECT User_password FROM User WHERE User_name='"+username_entry.get()+"'")
            rows=cursor.fetchall()
            print(rows[0][0])
            cursor.execute("commit")
            ##### checking password #####
            if(rows[0][0]==password_entry.get()):
                ##### to clear the entered values in the login page for the next time #####              
                messagebox.showinfo("Message","Login Successful")
                username_entry.delete(0,END)
                password_entry.delete(0,END)
                userwindow=Toplevel(userlogin)
                userwindow.title("User Window")
                userwindow.minsize(1000,900)
                userwindow.state('zoomed')
                userwindow.config(bg='#A2A2B5')#LightSteelBlue3
                #####Top frame that holds the heading of the admin window #####
                topFrame=Frame(userwindow,bd=10,relief=RIDGE,bg='#A2A2B5')
                topFrame.pack(side=TOP)
                ##### adding label to the top frame created #####
                labelTitle=Label(topFrame,text='MILK AND DAIRY PRODUCTS MANAGEMENT SYSTEM',font=('arial',30,'bold',),bg='#F5F5FF',fg='#A2A2B5',width=51)#"#F5F5FF"--"mint cream"
                labelTitle.grid(row=0,column=0)
                ##### creating a frame to add buttons #####
                buttonFrame=Frame(userwindow,bd=10,bg='#F5F5FF',width=650,height=100,relief=RIDGE)
                buttonFrame.place(x=375,y=90)
                ##### creating frames correspondingly to the buttons #####
                def ViewProductFrame():
                    ##### creating frame #####
                    viewproductFrame=Frame(userwindow,width=1030,height=575,bg='#A2A2B5',bd=10,relief=RIDGE)
                    viewproductFrame.place(x=225,y=200)
                    ##### giving a heading for user convience #####
                    txt='PRODUCTS AVAILABLE '
                    heading=Label(viewproductFrame,text=txt,font=('Helvetica',25,'italic'),fg='#F5F5FF',bg='#A2A2B5')
                    heading.place(x=80,y=30,width=500,height=30)
                    ##### listing the products available #####
                    Product_id_label=Label(viewproductFrame,text='Product Id ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id_label.place(x=200,y=75)
                    Product_name_label=Label(viewproductFrame,text='Product Name ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name_label.place(x=400,y=75)
                    Product_id1_label=Label(viewproductFrame,text='1 ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id1_label.place(x=200,y=130)
                    Product_name1_label=Label(viewproductFrame,text='Milk ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name1_label.place(x=400,y=130)
                    Product_id2_label=Label(viewproductFrame,text='2 ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id2_label.place(x=200,y=185)
                    Product_name2_label=Label(viewproductFrame,text='Curd ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name2_label.place(x=400,y=185)
                    Product_id3_label=Label(viewproductFrame,text='3 ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id3_label.place(x=200,y=240)
                    Product_name3_label=Label(viewproductFrame,text='Butter ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name3_label.place(x=400,y=240)
                    Product_id4_label=Label(viewproductFrame,text='4 ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id4_label.place(x=200,y=295)
                    Product_name4_label=Label(viewproductFrame,text='Cheese ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name4_label.place(x=400,y=295)
                    Product_id5_label=Label(viewproductFrame,text='5 ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id5_label.place(x=200,y=350)
                    Product_name5_label=Label(viewproductFrame,text='Paneer ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name5_label.place(x=400,y=350)
                    Product_id6_label=Label(viewproductFrame,text='6 ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_id6_label.place(x=200,y=405)
                    Product_name6_label=Label(viewproductFrame,text='Ghee ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    Product_name6_label.place(x=400,y=405)
                def BuyProductFrame():
                    ##### creating frame #####
                    buyproductFrame=Frame(userwindow,width=1030,height=575,bg='#A2A2B5',bd=10,relief=RIDGE)
                    buyproductFrame.place(x=225,y=200)
                    ##### function to buy product #####
                    def buy():
                        qty=qtyentry.get()
                        productid=productchoosen.get()
                        userid=buy_user_entry.get()
                        ##### checking for valid user id #####
                        if userid.isnumeric()==False:
                            messagebox.showinfo("Product Status","Enter valid User id")
                            return
                        ##### check if the user is present in the record #####
                        cursor.execute("SELECT COUNT(*) FROM User WHERE User_id="+buy_user_entry.get())
                        rows=cursor.fetchall()
                        cursor.execute("commit")                          
                        ##### checking for the user to input all the fields #####
                        if userid=="" or productid=="" or qty=="":
                            messagebox.showinfo("Product Status","All fields are required to buy a product ")
                        elif(rows[0][0]==0):
                            messagebox.showinfo("Product Status","User Not Found")
                        else:
                            cursor.execute("SELECT Quantity_avlb FROM Product WHERE Product_id='"+productid+"'")
                            rs=cursor.fetchall()
                            if int(qty)>=rs[0][0]:
                                messagebox.showinfo("Product Status ","Sorry,Product Unavailable !!!")
                            else:
                                updateqty=rs[0][0]-int(qty)
                                r=str(updateqty)
                                cursor.execute("UPDATE Product SET Quantity_avlb='"+r+"'WHERE Product_id='"+productid+"'")
                                cursor.execute("commit")
                                messagebox.showinfo("Product Status ","Thanks for buying !!!")
                                qtyentry.delete(0,END)
                                productchoosen.delete(0,END)
                                buy_user_entry.delete(0,END)
                                cursor.execute("INSERT INTO Bill VALUES("+productid+","+userid+","+qty+",curdate())")
                                cursor.execute("commit")                               
                    ##### giving a heading for user convience #####
                    txt='Choose Product'
                    heading=Label(buyproductFrame,text=txt,font=('Helvetica',25,'italic'),fg='#F5F5FF',bg='#A2A2B5')
                    heading.place(x=80,y=30,width=300,height=30)
                    ##### creating label and entry field for entering product id to be bought #####
                    buy_product_label=Label(buyproductFrame,text='Product Id ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    buy_product_label.place(x=50,y=75)               
                    # Combobox creation
                    n = int()
                    productchoosen = ttk.Combobox(buyproductFrame, width = 27, textvariable = n)
                    # Adding combobox drop down list
                    productchoosen['values'] = ('1','2','3','4','5','6') 
                    productchoosen.place(x=225,y=75,width=230,height=35)
                    ##### creating label and entry field for entering product id  #####
                    buy_user_label=Label(buyproductFrame,text='User Id ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    buy_user_label.place(x=50,y=150)               
                    buy_user_entry=Entry(buyproductFrame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                    buy_user_entry.place(x=225,y=150,width=230,height=35)
                    ##### creating label and entry field for entering product id  #####
                    qtylabel=Label(buyproductFrame,text='Quantity ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    qtylabel.place(x=50,y=225)               
                    qtyentry=Entry(buyproductFrame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                    qtyentry.place(x=225,y=225,width=230,height=35)
                    ##### creating buy button  #####
                    buy_btn=Button(buyproductFrame,text='BUY',bd='5',cursor='hand2',command=buy,font=btn_font,width=20,bg='#F5F5FF',fg='#A2A2B5')
                    buy_btn.place(x=275,y=300)
                def ViewBillFrame():
                    ##### creating frame #####
                    viewbillFrame=Frame(userwindow,width=1030,height=575,bg='#A2A2B5',bd=10,relief=RIDGE)
                    viewbillFrame.place(x=225,y=200)
                    def view():
                        ####input from user#####
                        userid=userentry.get()
                        #### fetching values from the database and displaying in the frame #####
                        cursor.execute("SELECT p.Product_id,p.Price,b.Quantity_saled,b.date_sold FROM Product p INNER JOIN Bill b ON p.Product_id=b.Product_id WHERE b.User_id="+userid)                                       
                        res=cursor.fetchall()
                        cursor.execute("commit")
                        for i in res:
                            tree.insert(parent='',index='end',values=(i[0],i[1],i[2],i[3]))                          
                        ##### calculating total #####
                        total=0
                        for i in res:
                            total=total+(i[1]*i[2])
                        toatlentry.insert(END,total)
                        cursor.execute("SELECT address FROM User WHERE user_id='"+userentry.get()+"'")
                        rs1=cursor.fetchall()
                        cursor.execute("commit")
                        messagebox.showinfo("Product Status ","Product will be shipped to  "+rs1[0][0]+" in 1 hour !! ")
                        userentry.delete(0,END)
                    ##### instance of style widget #####
                    style = ttk.Style()
                    style.theme_use('clam')
                    ##### creating tree frame to display bill #####
                    tree =ttk.Treeview(viewbillFrame, column=("c1", "c2","c3","c4"), show='headings', height=20)
                    ##### aligning columns #####                   
                    tree.column("# 1", anchor=CENTER)
                    tree.heading("# 1", text="Product ID")
                    tree.column("# 2", anchor=CENTER)
                    tree.heading("# 2", text="Price")
                    tree.column("# 3", anchor=CENTER)
                    tree.heading("# 3", text="Quantity")
                    tree.column("# 4", anchor=CENTER)
                    tree.heading("# 4", text="Date")
                    tree.place(x=5,y=0)                 
                    ##### creating label and text field for displaying total #####
                    totallabel=Label(viewbillFrame,text='Total ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    totallabel.place(x=50,y=500)               
                    toatlentry=Entry(viewbillFrame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                    toatlentry.place(x=225,y=500,width=230,height=35)
                    ##### creating label and entry field for user to enter userid #####
                    userlabel=Label(viewbillFrame,text='User id ',font=('Helvetica',17,'italic'),bg='#A2A2B5',fg='#F5F5FF')
                    userlabel.place(x=50,y=450)               
                    userentry=Entry(viewbillFrame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
                    userentry.place(x=225,y=450,width=230,height=35)
                    ##### creating buy button  #####
                    buy_btn=Button(viewbillFrame,text='VIEW',bd='5',cursor='hand2',command=view,font=btn_font,width=20,bg='#F5F5FF',fg='#A2A2B5')
                    buy_btn.place(x=470,y=475)
                ##### button to check products available #####
                check_products_btn=Button(buttonFrame,text='ViewProducts',bd='3',cursor='hand2',command=ViewProductFrame,font=btn_font,width=10,bg='#A2A2B5',fg='#F5F5FF')
                check_products_btn.place(x=25,y=20)
                ##### button to buy products #####
                buy_product_btn=Button(buttonFrame,text='BuyProducts',bd='3',cursor='hand2',command=BuyProductFrame,font=btn_font,width=10,bg='#A2A2B5',fg='#F5F5FF')
                buy_product_btn.place(x=170,y=20)
                ##### button to view bill #####
                view_bill_btn=Button(buttonFrame,text='View Bill',bd='3',cursor='hand2',command=ViewBillFrame,font=btn_font,width=10,bg='#A2A2B5',fg='#F5F5FF')
                view_bill_btn.place(x=310,y=20)
                ##### button to logout #####
                logout_btn=Button(buttonFrame,text='Logout',bd='3',cursor='hand2',command=userwindow.destroy,font=btn_font,width=10,bg='#A2A2B5',fg='#F5F5FF')
                logout_btn.place(x=455,y=20) 
            else:
                ##### showing warning message for invalid password #####
                messagebox.showwarning("Message","Invalid password")           
    ##### creating user login page #####
    userlogin = Toplevel(root)
    userlogin.title("User login page")
    userlogin.minsize(1000,900)
    userlogin.state('zoomed')
    ##### setting a image in background #####
    bg_frame=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\bg3.jpg")
    photo=ImageTk.PhotoImage(bg_frame)
    bg_panel=Label(userlogin,image=photo)
    bg_panel.image=photo
    bg_panel.pack(fill='both',expand='yes')
    ##### login frame #####
    ##### creating a login frame #####
    login_frame=Frame(userlogin,width='900',height=600)
    login_frame.place(x=50,y=125)
    ##### giving a heading for a login frame #####
    txt='USER LOGIN'
    txt1='MILK AND DAIRY PRODUCTS MANAGEMENT'
    heading=Label(login_frame,text=txt,font=('Helvetica',22,'italic'),fg='black')
    heading1=Label(login_frame,text=txt1,font=('Helvetica',25,'italic'),fg='black')
    heading1.place(x=5,y=5,width=750,height=30)
    heading.place(x=10,y=50,width=300,height=30)          
    ##### placing a image in the login frame #####
    sign_in_image=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\usericonlogin.png")
    photo=ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label=Label(login_frame,image=photo)
    sign_in_image_label.image=photo
    sign_in_image_label.place(x=670,y=50)
    #####placing 'sign in 'text #####
    sign_in_label=Label(login_frame,text='Sign In',fg='black',font=('Helvetica',17,'italic'))
    sign_in_label.place(x=635,y=175)
    ##### creating username label #####
    username_label=Label(login_frame,text='Username',font=('Helvetica',17,'italic'),fg='black')
    username_label.place(x=475,y=225)
    ##### creating textfield for username entry #####
    username_entry=Entry(login_frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
    username_entry.place(x=600,y=225,width=230,height=35)
    ##### creating password label #####
    password_label=Label(login_frame,text='Password',font=('Helvetica',17,'italic'),fg='black')
    password_label.place(x=475,y=300)
    ##### creating textfield for password entry #####
    password_entry=Entry(login_frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
    password_entry.place(x=600,y=300,width=230,height=35)
    ##### login button creation #####
    login_btn=Button(login_frame,text='Login',bd='5',cursor='hand2',command=openUserWindow,font=btn_font,width=20)
    login_btn.place(x=545,y=370)
###################################################### Worker login window###################################################################
def openWorkerLogin():
    btn_font=f.Font(family='Helvetica',size=16,weight='normal',slant='roman')
    ###### creating worker window #####
    def openWorkerWindow():
        ######checking if admin in database #####
        cursor.execute("SELECT COUNT(*) FROM Worker WHERE worker_name='"+username_entry.get()+"'")
        row=cursor.fetchall()
        cursor.execute("commit")
        if row[0][0]==0:
            messagebox.showinfo("Message","Worker not found !!!")
            return
        if password_entry.get()=="":
            messagebox.showinfo("Message","Enter your password")
        else:
            ##### selecting admin password from database to check the password validity #####
            cursor.execute("SELECT Worker_password FROM Worker WHERE Worker_name='"+username_entry.get()+"'")
            rows=cursor.fetchall()
            cursor.execute("commit")
            ##### checking password #####
            if(rows[0][0]==password_entry.get()):
                messagebox.showinfo("Message","Login successfull")
                password_entry.delete(0,END)
                username_entry.delete(0,END)
                workerwindow=Toplevel(workerlogin)
                workerwindow.title("Worker Window")
                workerwindow.minsize(1000,900)
                workerwindow.state('zoomed')               
                #####Top frame that holds the heading of the admin window #####
                topFrame=Frame(workerwindow,bd=10,relief=RIDGE,bg='#3B3B3B')#Gray23
                topFrame.pack(side=TOP)
                ##### adding label to the top frame created #####
                labelTitle=Label(topFrame,text='MILK AND DAIRY PRODUCTS MANAGEMENT SYSTEM',font=('arial',30,'bold',),fg='#3B3B3B',width=51)
                labelTitle.grid(row=0,column=0)
                ##### creating a frame to add buttons #####
                buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=650,height=100,relief=RIDGE)
                buttonFrame.place(x=375,y=90)
                ##### creating frames for the button correspondingly #####
                def LiveStock_btnFrame():
                    ##### creating frame #####
                    livestock_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=650,height=100,relief=RIDGE)
                    livestock_buttonFrame.place(x=375,y=200)
                    ##### creating frame for buttons in LiveStock_btnFrame #####
                    ##### frame for adding livestock details #####
                    def AddLiveStock_btnFrame():
                        ##### creating frame #####
                        add_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        add_buttonFrame.place(x=225,y=300)
                        def add():
                            livestock_id=livestock_id_entry.get()
                            livestocktype=livestock_type_entry.get()
                            capacity=capacity_entry.get()
                            if livestock_id=="" or livestocktype=="" or capacity=="":
                                messagebox.showinfo("Insert status","All fields are required for adding !!!!")
                            elif livestock_id.isnumeric()==False:
                                messagebox.showinfo("Insert status","Enter valid id")
                            else:
                                cursor.execute("INSERT INTO LiveStock VALUES("+livestock_id+",'"+livestocktype+"',"+capacity+")")
                                cursor.execute("commit")
                                messagebox.showinfo("Insert status","Livestock added !!!")
                                livestock_id_entry.delete(0,END)
                                livestock_type_entry.delete(0,END)
                                capacity_entry.delete(0,END)
                        ##### creating label for user convience #####
                        txt='Add LiveStock Details'
                        heading=Label(add_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=55,y=20,width=500,height=30)
                        ##### creating label and entry field for entering Livestock id  #####
                        livestock_id_label=Label(add_buttonFrame,text='Livestock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=75)               
                        livestock_id_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering LiveStock type ##### 
                        livestock_type_label=Label(add_buttonFrame,text='LiveStock Type ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_type_label.place(x=50,y=130)               
                        livestock_type_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_type_entry.place(x=225,y=130,width=230,height=35)
                        ##### creating label and entry field for entering capacity of milk #####
                        capacity_label=Label(add_buttonFrame,text='Capacity of milk ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        capacity_label.place(x=50,y=185)               
                        capacity_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        capacity_entry.place(x=225,y=185,width=230,height=35)              
                        ##### creating add button  #####
                        add_btn=Button(add_buttonFrame,text='ADD',bd='5',command=add,cursor='hand2',font=btn_font,width=20,fg='#3B3B3B')
                        add_btn.place(x=300,y=350)
                    ##### creating frame to update livestock  details #####
                    def updateLivestock_buttonFrame():
                        ##### creating frame #####
                        update_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        update_buttonFrame.place(x=225,y=300)
                        def update():
                            livestock_id=livestock_id_entry.get()
                            capacity=capacity_entry.get()
                            if livestock_id.isnumeric()==False:
                                messagebox.showinfo("Update status","Enter valid id")
                                return
                            cursor.execute("SELECT COUNT(*) FROM LiveStock WHERE LiveStock_id="+livestock_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")                     
                            if livestock_id==""  or capacity=="":
                                messagebox.showinfo("Update status","All fields are required for Updating !!!!")
                            elif(rows[0][0]==0):
                                messagebox.showinfo("Update Status","Livestock id Not Found")
                            else:
                                cursor.execute("UPDATE LiveStock SET Capacity_of_Milk='"+capacity+"'WHERE LiveStock_id='"+livestock_id+"'")
                                cursor.execute("commit")
                                messagebox.showinfo("Update status","Livestock Updated !!!")
                                livestock_id_entry.delete(0,END)
                                capacity_entry.delete(0,END)
                        ##### creating label for user convience #####
                        txt='Update LiveStock  Details'
                        heading=Label(update_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=75,y=20,width=500,height=30)
                        ##### creating label and entry field for entering LiveStock Id to be updated  ##### 
                        livestock_id_label=Label(update_buttonFrame,text='LiveStock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=75)               
                        livestock_id_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering capacity #####
                        capacity_label=Label(update_buttonFrame,text='Capacity of milk ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        capacity_label.place(x=50,y=130)               
                        capacity_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        capacity_entry.place(x=225,y=130,width=230,height=35)                       
                        ##### creating UPDATE button  #####
                        update_btn=Button(update_buttonFrame,text='UPDATE',bd='5',command=update,cursor='hand2',font=btn_font,width=20,fg='#3B3B3B')
                        update_btn.place(x=305,y=350)
                        ##### creating frame to delete livestock  details #####
                    def deleteLivestock_buttonFrame():
                        ##### creating frame #####
                        del_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        del_buttonFrame.place(x=225,y=300)
                        def delete():
                            livestock_id=livestock_id_entry.get()
                            if livestock_id.isnumeric()==False:
                                messagebox.showinfo("Delete status","Enter valid id")
                                return
                            cursor.execute("SELECT COUNT(*) FROM LiveStock WHERE LiveStock_id="+livestock_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")                     
                            if livestock_id=="" :
                                messagebox.showinfo("Delete status","All fields are required for Deleting !!!!")
                            elif(rows[0][0]==0):
                                messagebox.showinfo("Delete Status","Livestock id Not Found")
                            else:
                                cursor.execute("DELETE FROM LiveStock WHERE LiveStock_id='"+livestock_id+"'")
                                cursor.execute("commit")
                                messagebox.showinfo("Delete status","Livestock Deleted !!!")
                                livestock_id_entry.delete(0,END)                               
                        ##### creating label for user convience #####
                        txt='Delete LiveStock  Details'
                        heading=Label(del_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=75,y=20,width=500,height=30)
                        ##### creating label and entry field for entering LiveStock Id to be deleted  ##### 
                        livestock_id_label=Label(del_buttonFrame,text='LiveStock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=75)               
                        livestock_id_entry=Entry(del_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating DELETE button  #####
                        del_btn=Button(del_buttonFrame,text='DELETE',bd='5',cursor='hand2',command=delete,font=btn_font,width=20,fg='#3B3B3B')
                        del_btn.place(x=225,y=350)
                    ##### creating frame to display livestock  details #####
                    def ViewLivestockDetailsFrame():
                        ##### creating frame #####
                        ViewLivestock=Frame(workerwindow,width=1030,height=475,bg='#3B3B3B',bd=10,relief=RIDGE)
                        ViewLivestock.place(x=225,y=300)
                        ##### instance of style widget #####
                        style = ttk.Style()
                        style.theme_use('clam')
                        ##### creating tree frame to display livestock details #####
                        tree =ttk.Treeview(ViewLivestock, column=("c1", "c2","c3"), show='headings', height=20)
                        ##### aligning columns #####                   
                        tree.column("# 1", anchor=CENTER)
                        tree.heading("# 1", text="Livestock ID")
                        tree.column("# 2", anchor=CENTER)
                        tree.heading("# 2", text="Livestock type")
                        tree.column("# 3", anchor=CENTER)
                        tree.heading("# 3", text="Capacity of milk")
                        tree.place(x=200,y=0)
                         ##### fetching values from the database and displaying in the frame #####
                        cursor.execute("SELECT * FROM LiveStock")
                        res=cursor.fetchall()
                        for i in res:
                            tree.insert(parent='',index='end',values=(i[0],i[1],i[2]))
                        cursor.execute("commit")
                    ##### button for adding livestock #####
                    add_btn=Button(livestock_buttonFrame,text='ADD',bd='3',cursor='hand2',command=AddLiveStock_btnFrame,font=btn_font,width=10,fg='#3B3B3B')
                    add_btn.place(x=5,y=20)
                    ##### button for updating livestock #####
                    update_btn=Button(livestock_buttonFrame,text='UPDATE',bd='3',cursor='hand2',command=updateLivestock_buttonFrame,font=btn_font,width=10,fg='#3B3B3B')
                    update_btn.place(x=145,y=20)
                    ##### button for deleting livestock #####
                    del_btn=Button(livestock_buttonFrame,text='DELETE',bd='3',cursor='hand2',command=deleteLivestock_buttonFrame,font=btn_font,width=10,fg='#3B3B3B')
                    del_btn.place(x=290,y=20)
                    ##### button for viewing livestock details #####
                    view_btn=Button(livestock_buttonFrame,text='VIEW',bd='3',cursor='hand2',command=ViewLivestockDetailsFrame,font=btn_font,width=10,fg='#3B3B3B')
                    view_btn.place(x=435,y=20)
                def FeedMonitor_btnFrame():
                    ##### creating frame #####
                    FeedMonitor_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=650,height=100,relief=RIDGE)
                    FeedMonitor_buttonFrame.place(x=375,y=200)                   
                    ##### creating frame for buttons in LiveStockDiagonsis_btnFrame #####
                    ##### frame for adding livestock feedmonitor details #####
                    def AddLiveStock_btnFrame():
                        ##### creating frame #####
                        add_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        add_buttonFrame.place(x=225,y=300)
                        def add():
                            livestock_id=livestock_id_entry.get()
                            worker_id=Worker_id_entry.get()
                            feedtype=feedtype_entry.get()
                            if livestock_id=="" or worker_id=="" or feedtype=="":
                                messagebox.showinfo("Insert status","All fields are required for adding !!!!")
                            elif livestock_id.isnumeric()==False:
                                messagebox.showinfo("Insert status","Enter valid livestock id")
                            elif worker_id.isnumeric()==False:
                                messagebox.showinfo("Insert status","Enter valid worker id")
                            cursor.execute("SELECT COUNT(*) FROM LiveStock WHERE LiveStock_id="+livestock_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")
                            cursor.execute("SELECT COUNT(*) FROM Worker WHERE Worker_id="+Worker_id_entry.get())
                            row=cursor.fetchall()
                            cursor.execute("commit")                     
                            if(rows[0][0]==0):
                                messagebox.showinfo("Insert Status","Livestock id Not Found")
                            elif(row[0][0]==0):
                                messagebox.showinfo("Insert Status","Worker id Not Found")
                            else:
                                cursor.execute("INSERT INTO Feed_monitoring VALUES('"+worker_id+"',"+livestock_id+",'"+feedtype+"')")
                                cursor.execute("commit")
                                messagebox.showinfo("Insert status","Feedtype added !!!")
                                livestock_id_entry.delete(0,END)
                                Worker_id_entry.delete(0,END)
                                feedtype_entry.delete(0,END)
                        ##### creating label for user convience #####
                        txt='Add LiveStock FeedMonitoring Details'
                        heading=Label(add_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=55,y=20,width=500,height=30)
                        ##### creating label and entry field for entering Livestock id  #####
                        livestock_id_label=Label(add_buttonFrame,text='Livestock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=75)               
                        livestock_id_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering Worker ID ##### 
                        Worker_id_label=Label(add_buttonFrame,text='Worker ID ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Worker_id_label.place(x=50,y=130)               
                        Worker_id_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Worker_id_entry.place(x=225,y=130,width=230,height=35)
                        ##### creating label and entry field for entering feed type #####
                        feedtype_label=Label(add_buttonFrame,text='Feedtype ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        feedtype_label.place(x=50,y=185)               
                        feedtype_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        feedtype_entry.place(x=225,y=185,width=230,height=35)              
                        ##### creating add button  #####
                        add_btn=Button(add_buttonFrame,text='ADD',bd='5',command=add,cursor='hand2',font=btn_font,width=20,fg='#3B3B3B')
                        add_btn.place(x=300,y=350)
                    ##### creating frame to update livestock feed monitor details #####
                    def updateLivestock_buttonFrame():
                        ##### creating frame #####
                        update_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        update_buttonFrame.place(x=225,y=300)
                        def update():
                            livestock_id=livestock_id_entry.get()
                            feedtype=feedtype_entry.get()
                            if livestock_id==""  or feedtype=="":
                                messagebox.showinfo("Update status","All fields are required for Updating !!!!")
                            if livestock_id.isnumeric()==False:
                                messagebox.showinfo("Update status","Enter valid id")
                                return
                            cursor.execute("SELECT COUNT(*) FROM Feed_monitoring WHERE LiveStock_id="+livestock_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")                     
                            if(rows[0][0]==0):
                                messagebox.showinfo("Update Status","Livestock id Not Found")
                            else:
                                cursor.execute("UPDATE Feed_monitoring SET Feed_type='"+feedtype+"'WHERE LiveStock_id='"+livestock_id+"'")
                                cursor.execute("commit")
                                messagebox.showinfo("Update status","Feedtype Updated !!!")
                                livestock_id_entry.delete(0,END)
                                feedtype_entry.delete(0,END)
                        ##### creating label for user convience #####
                        txt='Update LiveStock FeedMonitoring Details'
                        heading=Label(update_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=75,y=20,width=500,height=30)
                        ##### creating label and entry field for entering LiveStock Id to be updated  ##### 
                        livestock_id_label=Label(update_buttonFrame,text='LiveStock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=75)               
                        livestock_id_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering feedtype  #####
                        feedtype_label=Label(update_buttonFrame,text='Feedtype ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        feedtype_label.place(x=50,y=130)               
                        feedtype_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        feedtype_entry.place(x=225,y=130,width=230,height=35)                       
                        ##### creating UPDATE button  #####
                        update_btn=Button(update_buttonFrame,text='UPDATE',bd='5',command=update,cursor='hand2',font=btn_font,width=20,fg='#3B3B3B')
                        update_btn.place(x=305,y=350)
                    ##### creating frame to display livestock feedmonitor details #####
                    def ViewLivestockFeedMonitorDetailsFrame():
                        ##### creating frame #####
                        ViewLivestock=Frame(workerwindow,width=1030,height=475,bg='#3B3B3B',bd=10,relief=RIDGE)
                        ViewLivestock.place(x=225,y=300)
                        ##### instance of style widget #####
                        style = ttk.Style()
                        style.theme_use('clam')
                        ##### creating tree frame to display livestock diagonsis #####
                        tree =ttk.Treeview(ViewLivestock, column=("c1", "c2","c3"), show='headings', height=20)
                        ##### aligning columns #####                  
                        tree.column("# 1", anchor=CENTER)
                        tree.heading("# 1", text="Worker ID")
                        tree.column("# 2", anchor=CENTER)
                        tree.heading("# 2", text="Livestock ID")
                        tree.column("# 3", anchor=CENTER)
                        tree.heading("# 3", text="Feedtype")
                        tree.place(x=200,y=0)
                         ##### fetching values from the database and displaying in the frame #####
                        cursor.execute("SELECT * FROM Feed_monitoring")
                        res=cursor.fetchall()
                        for i in res:
                            tree.insert(parent='',index='end',values=(i[0],i[1],i[2]))
                        cursor.execute("commit")                   
                    ##### button for adding new livestock feed monitoring #####
                    add_btn=Button(FeedMonitor_buttonFrame,text='ADD',bd='3',cursor='hand2',command=AddLiveStock_btnFrame,font=btn_font,width=10,fg='#3B3B3B')
                    add_btn.place(x=100,y=20)
                    ##### button for updating livestock feedtype #####
                    update_btn=Button(FeedMonitor_buttonFrame,text='UPDATE',bd='3',cursor='hand2',command=updateLivestock_buttonFrame,font=btn_font,width=10,fg='#3B3B3B')
                    update_btn.place(x=250,y=20)
                    ##### button for viewing livestock feedtype details #####
                    view_btn=Button(FeedMonitor_buttonFrame,text='VIEW',bd='3',cursor='hand2',command=ViewLivestockFeedMonitorDetailsFrame,font=btn_font,width=10,fg='#3B3B3B')
                    view_btn.place(x=400,y=20)
                def LiveStockDiagonisis_btnFrame():
                    ##### creating frame #####
                    LiveStockDiagonisis_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=650,height=100,relief=RIDGE)
                    LiveStockDiagonisis_buttonFrame.place(x=375,y=200)
                    ##### creating frame for buttons in LiveStockDiagonsis_btnFrame #####
                    ##### frame for adding livestock diagonsis details #####
                    def AddLiveStock_btnFrame():
                        ##### creating frame #####
                        add_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        add_buttonFrame.place(x=225,y=300)
                        def add():
                            livestock_id=livestock_id_entry.get()
                            worker_id=worker_id_entry.get()
                            disease=disease_entry.get()
                            dstatus=Disease_status_entry.get()
                            vstatus=Vaccine_status_entry.get()
                            expenses=Expenses_entry.get()
                            if livestock_id=="" or worker_id=="" or disease=="" or dstatus=="" or vstatus=="" or expenses=="":
                                messagebox.showinfo("Insert status","All fields are required for adding !!!!")
                            elif livestock_id.isnumeric()==False:
                                messagebox.showinfo("Insert status","Enter valid livestock id")
                            else:
                                cursor.execute("INSERT INTO LiveStockDiagonsis VALUES('"+worker_id+"',"+livestock_id+",'"+disease+"','"+dstatus+"','"+expenses+"','"+vstatus+"')")
                                cursor.execute("commit")
                                messagebox.showinfo("Insert status","LiveStock details added !!!")
                                livestock_id_entry.delete(0,END)
                                worker_id_entry.delete(0,END)
                                disease_entry.delete(0,END)
                                Disease_status_entry.delete(0,END)
                                Vaccine_status_entry.delete(0,END)
                                Expenses_entry.delete(0,END)
                        ##### creating label for user convience #####
                        txt='Add LiveStock Diagnosis Details'
                        heading=Label(add_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=50,y=20,width=400,height=30)
                        ##### creating label and entry field for entering Worker id  #####
                        worker_id_label=Label(add_buttonFrame,text='Worker Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        worker_id_label.place(x=50,y=75)               
                        worker_id_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        worker_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering LiveStock Id ##### 
                        livestock_id_label=Label(add_buttonFrame,text='LiveStock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=130)               
                        livestock_id_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=130,width=230,height=35)
                        ##### creating label and entry field for entering Disease #####
                        disease_label=Label(add_buttonFrame,text='Disease ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        disease_label.place(x=50,y=185)               
                        disease_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        disease_entry.place(x=225,y=185,width=230,height=35)
                        ##### creating label and entry field for entering Disease Status  #####
                        Disease_status_label=Label(add_buttonFrame,text='Disease Status ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Disease_status_label.place(x=50,y=240)               
                        Disease_status_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Disease_status_entry.place(x=225,y=240,width=230,height=35)
                        ##### creating label and entry field for entering Vaccine Status ##### 
                        Vaccine_status_label=Label(add_buttonFrame,text='Vaccine Status ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Vaccine_status_label.place(x=50,y=295)               
                        Vaccine_status_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Vaccine_status_entry.place(x=225,y=295,width=230,height=35)
                        ##### creating label and entry field for entering Expenses #####
                        Expenses_label=Label(add_buttonFrame,text='Expense ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Expenses_label.place(x=50,y=350)               
                        Expenses_entry=Entry(add_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Expenses_entry.place(x=225,y=350,width=230,height=35)
                        ##### creating add button  #####
                        add_btn=Button(add_buttonFrame,text='ADD',bd='5',command=add,cursor='hand2',font=btn_font,width=20,fg='#3B3B3B')
                        add_btn.place(x=375,y=400)
                    ##### creating frame to update livestock details #####
                    def updateLivestock_buttonFrame():
                        ##### creating frame #####
                        update_buttonFrame=Frame(workerwindow,bd=10,bg='#3B3B3B',width=1030,height=475,relief=RIDGE)
                        update_buttonFrame.place(x=225,y=300)
                        ##### function to update livestock details #####
                        def update():
                            livestock_id=livestock_id_entry.get()
                            dstatus=Disease_status_entry.get()
                            vstatus=Vaccine_status_entry.get()
                            Expenses=Expenses_entry.get()
                            if livestock_id==""  or dstatus=="" or vstatus=="" or Expenses=="":
                                messagebox.showinfo("Update status","All fields are required for Updating !!!!")
                            if livestock_id.isdigit()==False:
                                messagebox.showinfo("Update status","Enter valid id")
                                return
                            cursor.execute("SELECT COUNT(*) FROM LivestockDiagonsis WHERE LiveStock_id="+livestock_id_entry.get())
                            rows=cursor.fetchall()
                            cursor.execute("commit")                     
                            if(rows[0][0]==0):
                                messagebox.showinfo("Update Status","Livestock id Not Found")
                            else:
                                cursor.execute("UPDATE LivestockDiagonsis SET disease_status='"+dstatus+"'WHERE LiveStock_id='"+livestock_id+"'")
                                cursor.execute("UPDATE LivestockDiagonsis SET expenses='"+Expenses+"'WHERE LiveStock_id='"+livestock_id+"'")
                                cursor.execute("UPDATE LivestockDiagonsis SET vaccine_status='"+vstatus+"'WHERE LiveStock_id='"+livestock_id+"'")
                                cursor.execute("commit")
                                messagebox.showinfo("Update status","Livestock Updated !!!")
                                if dstatus=="Death":
                                    cursor.execute("DELETE FROM Livestock WHERE LiveStock_id='"+livestock_id+"'")
                                    cursor.execute("commit")
                                livestock_id_entry.delete(0,END)
                                Disease_status_entry.delete(0,END)
                                Vaccine_status_entry.delete(0,END)
                                Expenses_entry.delete(0,END)
                        ##### creating label for user convience #####
                        txt='Update LiveStock Diagnosis Details'
                        heading=Label(update_buttonFrame,text=txt,font=('Helvetica',20,'italic'),bg='#3B3B3B',fg='white')
                        heading.place(x=75,y=20,width=500,height=30)
                        ##### creating label and entry field for entering LiveStock Id to be updated  ##### 
                        livestock_id_label=Label(update_buttonFrame,text='LiveStock Id ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        livestock_id_label.place(x=50,y=75)               
                        livestock_id_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        livestock_id_entry.place(x=225,y=75,width=230,height=35)
                        ##### creating label and entry field for entering Disease Status  #####
                        Disease_status_label=Label(update_buttonFrame,text='Disease Status ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Disease_status_label.place(x=50,y=130)               
                        Disease_status_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Disease_status_entry.place(x=225,y=130,width=230,height=35)
                        ##### creating label and entry field for entering Vaccine Status ##### 
                        Vaccine_status_label=Label(update_buttonFrame,text='Vaccine Status ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Vaccine_status_label.place(x=50,y=185)               
                        Vaccine_status_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Vaccine_status_entry.place(x=225,y=185,width=230,height=35)
                        ##### creating label and entry field for entering Expenses #####
                        Expenses_label=Label(update_buttonFrame,text='Expense ',font=('Helvetica',17,'italic'),bg='#3B3B3B',fg='white')
                        Expenses_label.place(x=50,y=240)               
                        Expenses_entry=Entry(update_buttonFrame,highlightthickness=0,relief=FLAT,font=('Helvetica',12,'italic'))
                        Expenses_entry.place(x=225,y=240,width=230,height=35)
                        ##### creating UPDATE button  #####
                        update_btn=Button(update_buttonFrame,text='UPDATE',bd='5',command=update,cursor='hand2',font=btn_font,width=20,fg='#3B3B3B')
                        update_btn.place(x=375,y=350)
                    ##### creating frame to display livestock diagonsis details #####
                    def ViewLivestockDiagonsisDetailsFrame():
                        ##### creating frame #####
                        ViewLivestock=Frame(workerwindow,width=1030,height=475,bg='#3B3B3B',bd=10,relief=RIDGE)
                        ViewLivestock.place(x=225,y=300)
                        ##### instance of style widget #####
                        style = ttk.Style()
                        style.theme_use('default')
                        ##### creating tree frame to display livestock diagonsis #####
                        tree =ttk.Treeview(ViewLivestock, column=("c1", "c2","c3","c4","c5"), show='headings', height=20)
                        ##### aligning columns #####                  
                        tree.column("# 1", anchor=CENTER)
                        tree.heading("# 1", text="Livestock ID")
                        tree.column("# 2", anchor=CENTER)
                        tree.heading("# 2", text="Disease")
                        tree.column("# 3", anchor=CENTER)
                        tree.heading("# 3", text="DiseaseStatus")
                        tree.column("# 4", anchor=CENTER)
                        tree.heading("# 4", text="VaccineStatus")
                        tree.column("# 5", anchor=CENTER)
                        tree.heading("# 5", text="Expenses")
                        tree.place(x=5,y=0)
                        cursor.execute("SELECT * FROM LiveStockDiagonsis")
                        res=cursor.fetchall()
                        for i in res:
                            tree.insert(parent='',index='end',values=(i[1],i[2],i[3],i[5],i[4]))
                        cursor.execute("commit")
                    ##### button for adding new livestock diagonsis #####
                    add_btn=Button(LiveStockDiagonisis_buttonFrame,text='ADD',bd='3',cursor='hand2',command=AddLiveStock_btnFrame,font=btn_font,width=10,fg='#3B3B3B')
                    add_btn.place(x=100,y=20)
                    ##### button for updating livestock diagonsis #####
                    update_btn=Button(LiveStockDiagonisis_buttonFrame,text='UPDATE',bd='3',cursor='hand2',command=updateLivestock_buttonFrame,font=btn_font,width=10,fg='#3B3B3B')
                    update_btn.place(x=250,y=20)
                    ##### button for viewing livestock diagonsis details #####
                    view_btn=Button(LiveStockDiagonisis_buttonFrame,text='VIEW',bd='3',cursor='hand2',command=ViewLivestockDiagonsisDetailsFrame,font=btn_font,width=10,fg='#3B3B3B')
                    view_btn.place(x=400,y=20)
                ##### button for livestock #####
                livestock_btn=Button(buttonFrame,text='Livestock',bd='3',cursor='hand2',command=LiveStock_btnFrame,font=btn_font,width=10,fg='#3B3B3B')
                livestock_btn.place(x=25,y=20)
                ##### button for feedmonitor #####
                feed_monitor_btn=Button(buttonFrame,text='FeedMonitor',bd='3',cursor='hand2',command=FeedMonitor_btnFrame,font=btn_font,width=10,fg='#3B3B3B')
                feed_monitor_btn.place(x=170,y=20)
                ##### button to livestock diagonis check #####
                diagonsis_btn=Button(buttonFrame,text='Diagnois',bd='3',cursor='hand2',command=LiveStockDiagonisis_btnFrame,font=btn_font,width=10,fg='#3B3B3B')
                diagonsis_btn.place(x=310,y=20)
                ##### button to logout #####
                logout_btn=Button(buttonFrame,text='Logout',bd='3',cursor='hand2',command=workerwindow.destroy,font=btn_font,width=10,fg='#3B3B3B')
                logout_btn.place(x=455,y=20) 
            else:
                ##### showing warning message for invalid password #####
                messagebox.showwarning("Message","Invalid password")        
    ##### creating worker login page #####
    workerlogin = Toplevel(root)
    workerlogin.title("Worker login page")
    workerlogin.minsize(1000,900)
    workerlogin.state('zoomed')   
    ##### setting background image ##### 
    bg_frame=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\bg4.jpg")
    photo=ImageTk.PhotoImage(bg_frame)
    bg_panel=Label(workerlogin,image=photo)
    bg_panel.image=photo
    bg_panel.pack(fill='both',expand='yes')
    ##### login frame #####
    ##### creating a login frame #####
    login_frame=Frame(workerlogin,width='900',height=600)
    login_frame.place(x=600,y=100)
    ##### giving a heading for a login frame #####
    txt='WORKER LOGIN'
    txt1='MILK AND DAIRY PRODUCTS MANAGEMENT'
    heading=Label(login_frame,text=txt,font=('Helvetica',22,'italic'),fg='black')
    heading1=Label(login_frame,text=txt1,font=('Helvetica',25,'italic'),fg='black')
    heading1.place(x=5,y=5,width=750,height=30)
    heading.place(x=10,y=50,width=300,height=30) 
    ##### placing a image in the login frame #####
    sign_in_image=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\workericon.jpeg")
    photo=ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label=Label(login_frame,image=photo)
    sign_in_image_label.image=photo
    sign_in_image_label.place(x=620,y=50)
    #####placing 'sign in 'text #####
    sign_in_label=Label(login_frame,text='Sign In',fg='black',font=('Helvetica',17,'italic'))
    sign_in_label.place(x=635,y=175)
    ##### creating username label #####
    username_label=Label(login_frame,text='Username',font=('Helvetica',17,'italic'),fg='black')
    username_label.place(x=475,y=225)
    ##### creating textfield for username entry #####
    username_entry=Entry(login_frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
    username_entry.place(x=600,y=225,width=230,height=35)
    ##### creating password label #####
    password_label=Label(login_frame,text='Password',font=('Helvetica',17,'italic'),fg='black')
    password_label.place(x=475,y=300)
    ##### creating textfield for password entry #####
    password_entry=Entry(login_frame,highlightthickness=0,relief=FLAT,fg="black",font=('Helvetica',12,'italic'))
    password_entry.place(x=600,y=300,width=230,height=35)
    ##### login button creation #####
    login_btn=Button(login_frame,text='Login',bd='5',cursor='hand2',command=openWorkerWindow,font=btn_font,width=20)
    login_btn.place(x=545,y=370)
####################################################login options#######################################################################
##### main window #####
root=Tk()
root.title("Login Page")
root.minsize(640,400)
##### setting background image #####
bg_frame=Image.open("C:\\Users\\maha9\\OneDrive\\Documents\\II_semester\\Dbms&py_miniproj\\bg1.jpg")
photo=ImageTk.PhotoImage(bg_frame)
bg_panel=Label(root,image=photo)
bg_panel.image=photo
bg_panel.pack(fill='both',expand='yes')
##### giving a heading for a login frame #####
txt=' DAIRY PRODUCTS MANAGEMENT SYSTEM'
heading=Label(bg_panel,text=txt,font=('Helvetica',20,'italic'))
heading.place(x=0,y=10,width=650,height=30)
##### creating admin login button #####
btn_font=f.Font(family='Helvetica',size=16,weight='normal',slant='roman')
btn1=Button(root,text='Admin Login',bd='5',command=openAdminLogin,font=btn_font)
btn1.place(x=250,y=75)
##### creating user login button #####
btn2=Button(root,text='User Login  ',bd='5',command=openUserLogin,font=btn_font)
btn2.place(x=250,y=175)
##### creating worker login button #####
btn3=Button(root,text='Worker Login',bd='5',command=openWorkerLogin,font=btn_font)
btn3.place(x=250,y=275)
########################################################################################################################################
root.mainloop()
##### closing the connection to the database #####
con.close()
