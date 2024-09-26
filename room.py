from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #========Variable=====
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        #=================TITLE=======
        L_T1=Label(self.root,text="ROOM-BOOKING DETAILS",font=("Castellar",18,"bold"),bg='black',fg='lime',bd=6,relief=SUNKEN)
        L_T1.place(x=0,y=0,width=1295,height=50)
        #------------------2nd Image Logo---------------------#
        img2=Image.open(r"Logo1.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        L2=Label(self.root,image=self.photoimg2,bd=0,relief=SUNKEN)
        L2.place(x=5,y=2,width=100,height=40)

        #-------------Label frame----------
        L_fleft=LabelFrame(self.root,bd=2,relief=SUNKEN,text="Room Details",padx=2,font=("times new roman",12,"bold"))
        L_fleft.place(x=5,y=50,width=425,height=490)

        #-------------labels and entry------
        #custcontact
        L_C_contact=Label(L_fleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_contact.grid(row=0,column=0,sticky=W)

        E_contact=ttk.Entry(L_fleft,textvariable=self.var_contact,font=("times new roman",13,"bold"),width=20)
        E_contact.grid(row=0,column=1,sticky=W)

        # Fetch data button
        B_fetchdata=Button(L_fleft,command=self.Fetch_contact,text="Fetch Data",font=("times new roman",10,"italic"),bg="black",fg="gold",width=10)
        B_fetchdata.place(x=330,y=4)

        #Check_in Date
        L_C_name=Label(L_fleft,text="Check_in Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_name.grid(row=1,column=0,sticky=W)

        E_name=ttk.Entry(L_fleft,textvariable=self.var_checkin,font=("times new roman",13,"bold"),width=29)
        E_name.grid(row=1,column=1)

        #Check_out Date
        L_C_mname=Label(L_fleft,text="Check_out Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_mname.grid(row=2,column=0,sticky=W)

        E_mname=ttk.Entry(L_fleft,textvariable=self.var_checkout,font=("times new roman",13,"bold"),width=29)
        E_mname.grid(row=2,column=1)

        
        #Room Type
        L_C_gender=Label(L_fleft,text="Room Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_gender.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(L_fleft,textvariable=self.var_roomtype,font=("times new roman",12,"bold"),width=31,state="readonly")
        combo_RoomType["value"]=("Single","Double","Elite")#ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        #Available room 
        lblRoomAvailable=Label(L_fleft,text="Available Room:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        # E_postcode=ttk.Entry(L_fleft,textvariable=self.var_roomavailable,font=("times new roman",13,"bold"),width=29)
        # E_postcode.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(L_fleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=31,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        #Meal
        lblMeal=Label(L_fleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        E_mobile=ttk.Entry(L_fleft,textvariable=self.var_meal,font=("times new roman",13,"bold"),width=29)
        E_mobile.grid(row=5,column=1)

        #No. of Days:
        L_C_email=Label(L_fleft,text="No. of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_email.grid(row=6,column=0,sticky=W)

        E_email=ttk.Entry(L_fleft,textvariable=self.var_noOfdays,font=("times new roman",13,"bold"),width=29)
        E_email.grid(row=6,column=1)

        #Paid Tax
        L_C_nation=Label(L_fleft,text="Paid Tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_nation.grid(row=7,column=0,sticky=W)

        Com_nation=ttk.Entry(L_fleft,textvariable=self.var_paidtax,font=("times new roman",12,"bold"),width=29)
        Com_nation.grid(row=7,column=1)

        #Sub Total
        L_C_nation=Label(L_fleft,text="Sub Total:",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_nation.grid(row=8,column=0,sticky=W)

        Com_nation=ttk.Entry(L_fleft,textvariable=self.var_actualtotal,font=("times new roman",12,"bold"),width=29)
        Com_nation.grid(row=8,column=1)

        #Total Cost
        L_C_nation=Label(L_fleft,text="Total Cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        L_C_nation.grid(row=9,column=0,sticky=W)

        Com_nation=ttk.Entry(L_fleft,textvariable=self.var_total,font=("times new roman",12,"bold"),width=29)
        Com_nation.grid(row=9,column=1)

#----------Buttons------------
#bill button
        B_Bill=Button(L_fleft,text="Bill",command=self.total,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Bill.grid(row=10,column=0,padx=1,sticky=W)        
        #=============Btns=========
        B_F=Frame(L_fleft,bd=2,relief=RIDGE)
        B_F.place(x=0,y=400,width=412,height=40)


        B_Add=Button(B_F,text="Add",command=self.add_data,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Add.grid(row=0,column=0,padx=1)

        B_Update=Button(B_F,text="Update",command=self.update,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Update.grid(row=0,column=1,padx=1)

        B_Delete=Button(B_F,text="Delete",command=self.mDelete,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Delete.grid(row=0,column=2,padx=1)

        B_Reset=Button(B_F,text="Reset",command=self.reset,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Reset.grid(row=0,column=3,padx=1)

        #---------Right side image
        L_T1=Label(self.root,text="ROOM-BOOKING DETAILS",font=("Castellar",18,"bold"),bg='black',fg='lime',bd=6,relief=SUNKEN)
        L_T1.place(x=0,y=0,width=1295,height=50)
        #------------------2nd Image Logo---------------------#
        img3=Image.open(r"hotel.png")
        img3=img3.resize((500,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        L2=Label(self.root,image=self.photoimg3,bd=0,relief=SUNKEN)
        L2.place(x=790,y=55,width=500,height=300)


        #===========tabel frame and search system======
        Table_Frame=LabelFrame(self.root,bd=2,relief=SUNKEN,text="View Details and Search System",bg='light grey',padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=430,y=280,width=860,height=260)

        L_Searchby=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        L_Searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        Com_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=24,state="readonly")
        Com_search["value"]=("Contact ","Room",)
        Com_search.current(0)
        Com_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        E_search=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=24)
        E_search.grid(row=0,column=2,padx=2) 

        B_Search=Button(Table_Frame,text="Search",command=self.search,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Search.grid(row=0,column=3,padx=1)

        B_Showall=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Showall.grid(row=0,column=4,padx=1)

        #==========Show Data Table============

        Details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        Details_table.place(x=0,y=50,width=860,height=180)
        # Details_table.pack(fill=X)

        scroll_x=ttk.Scrollbar(Details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(Details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")

        

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        #The below function is used to make the apperance of the data in the boxes
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
#-----ADD DATA-----------
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noOfdays.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)
    #To fetch data from the database.            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])

#Update function 
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                                                 
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noOfdays.get(), 
                                                                                                                                            self.var_contact.get()

                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        

#=========All Data Fetch======
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=160)#Height cross check

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                #Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                #Email
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
                #Nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)
                #Address
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
#Search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Elite"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Elite"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Elite"):
            q1=float(400)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Doublee"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(400)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(400)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(400)
            q2=float(400)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs"+str("%.2f"%((q5)*0.18))
            ST="Rs"+str("%.2f"%((q5)))
            TT="Rs"+str("%.2f"%((q5)+((q5)*0.18)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
