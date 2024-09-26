from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #--------------------Variables------------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        # self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()


        #=================TITLE=======
        L_T1=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Castellar",18,"bold"),bg='black',fg='lime',bd=6,relief=SUNKEN)
        L_T1.place(x=0,y=0,width=1295,height=50)
        #------------------2nd Image Logo---------------------#
        img2=Image.open(r"Logo1.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        L2=Label(self.root,image=self.photoimg2,bd=0,relief=SUNKEN)
        L2.place(x=5,y=2,width=100,height=40)

        #-------------Label frame----------
        L_fleft=LabelFrame(self.root,bd=2,relief=SUNKEN,text="Customer Details",bg='light grey',padx=2,font=("times new roman",12,"bold"))
        L_fleft.place(x=5,y=50,width=425,height=490)
        # L_fleft.pack(fill=X)
        #-------------labels and entry------
        #custref
        L_C_ref=Label(L_fleft,text="Customer Ref",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_ref.grid(row=0,column=0,sticky=W)

        E_ref=ttk.Entry(L_fleft,textvariable=self.var_ref,font=("times new roman",13,"bold"),width=29,state="readonly")
        E_ref.grid(row=0,column=1)
        
        #cust name
        L_C_name=Label(L_fleft,text="Customer Name",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_name.grid(row=1,column=0,sticky=W)

        E_name=ttk.Entry(L_fleft,textvariable=self.var_cust_name,font=("times new roman",13,"bold"),width=29)
        E_name.grid(row=1,column=1)

        #mother name
        L_C_mname=Label(L_fleft,text="Mother Name",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_mname.grid(row=2,column=0,sticky=W)

        E_mname=ttk.Entry(L_fleft,textvariable=self.var_mother,font=("times new roman",13,"bold"),width=29)
        E_mname.grid(row=2,column=1)
        #gender combobox
        L_C_gender=Label(L_fleft,text="Gender",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_gender.grid(row=3,column=0,sticky=W)

        Com_gender=ttk.Combobox(L_fleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=31,state="readonly")
        Com_gender["value"]=("Male","Female","Other")
        Com_gender.current(0)
        Com_gender.grid(row=3,column=1)
        
        #postcode
        L_C_postcode=Label(L_fleft,text="Postal code",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_postcode.grid(row=4,column=0,sticky=W)

        E_postcode=ttk.Entry(L_fleft,textvariable=self.var_post,font=("times new roman",13,"bold"),width=29)
        E_postcode.grid(row=4,column=1)

        #Mobile no.
        L_C_mobile=Label(L_fleft,text="Mobile No.",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_mobile.grid(row=5,column=0,sticky=W)

        E_mobile=ttk.Entry(L_fleft,textvariable=self.var_mobile,font=("times new roman",13,"bold"),width=29)
        E_mobile.grid(row=5,column=1)

        #Email
        L_C_email=Label(L_fleft,text="Email",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_email.grid(row=6,column=0,sticky=W)

        E_email=ttk.Entry(L_fleft,textvariable=self.var_email,font=("times new roman",13,"bold"),width=29)
        E_email.grid(row=6,column=1)

        #Nationality
        L_C_nation=Label(L_fleft,text="Nationality",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_nation.grid(row=7,column=0,sticky=W)

        Com_nation=ttk.Combobox(L_fleft,textvariable=self.var_nationality,font=("times new roman",12,"bold"),width=31,state="readonly")
        Com_nation["value"]=("Indian","American","Britian")
        Com_nation.current(0)
        Com_nation.grid(row=7,column=1)

        #id proof type combobox
        L_C_idproof=Label(L_fleft,text="ID proof type",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_idproof.grid(row=8,column=0,sticky=W)

        Com_idproof=ttk.Combobox(L_fleft,textvariable=self.var_id_proof,font=("times new roman",12,"bold"),width=31,state="readonly")
        Com_idproof["value"]=("Aadhar card","Driving license","Passport")
        Com_idproof.current(0)
        Com_idproof.grid(row=8,column=1)
       
        #Id Number
        L_C_idnum=Label(L_fleft,text="Id Number",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_idnum.grid(row=9,column=0,sticky=W)

        E_idnum=ttk.Entry(L_fleft,textvariable=self.var_id_number,font=("times new roman",13,"bold"),width=29)
        E_idnum.grid(row=9,column=1)

        #Address
        L_C_address=Label(L_fleft,text="Address",font=("times new roman",12,"bold"),background="light grey",padx=2,pady=6)
        L_C_address.grid(row=10,column=0,sticky=W)

        E_address=ttk.Entry(L_fleft,textvariable=self.var_address,font=("times new roman",13,"bold"),width=29)
        E_address.grid(row=10,column=1)


        #=============Btns=========
        B_F=Frame(L_fleft,bd=2,relief=RIDGE)
        B_F.place(x=0,y=400,width=412,height=40)
        # B_F.pack(fill=X)

        B_Add=Button(B_F,text="Add",command=self.add_data,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Add.grid(row=0,column=0,padx=1)

        B_Update=Button(B_F,text="Update",command=self.update,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Update.grid(row=0,column=1,padx=1)

        B_Delete=Button(B_F,text="Delete",command=self.mDelete,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Delete.grid(row=0,column=2,padx=1)

        B_Reset=Button(B_F,text="Reset",command=self.reset,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Reset.grid(row=0,column=3,padx=1)

        #===========tabel frame and search system======
        Table_Frame=LabelFrame(self.root,bd=2,relief=SUNKEN,text="View Details and Search System",bg='light grey',padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=430,y=50,width=860,height=490)

        L_Searchby=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        L_Searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        Com_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=24,state="readonly")
        Com_search["value"]=("Mobile ",)
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
        Details_table.place(x=0,y=50,width=860,height=350)
        # Details_table.pack(fill=X)

        scroll_x=ttk.Scrollbar(Details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(Details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="E mail")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif "@gmail.com" not in self.var_email.get():
            messagebox.showerror("Error","Enter a valid email",parent=self.root)
        elif len(self.var_mobile.get())!=10:
            messagebox.showerror("Error","Enter a 10 digit valid mobile number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_address.get()#Comma should be at end or not
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()#indentation check
    # the below fuction is used to make rows appear in the box of changes so that we can update the statement
    def get_cursor(self,events=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]),
        # self.var_id_proof.set(row[9]),
        # self.var_id_number.set(row[10]),
    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,IDproof=%s,IDnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                    
                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_ref.get()

                                                                                                                                                             ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
  




if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
