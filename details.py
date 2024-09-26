from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

         #=================TITLE=======
        L_T1=Label(self.root,text="ROOM-DETAILS",font=("Castellar",18,"bold"),bg='black',fg='lime',bd=6,relief=SUNKEN)
        L_T1.place(x=0,y=0,width=1295,height=50)
        #------------------2nd Image Logo---------------------#
        img2=Image.open(r"Logo1.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        L2=Label(self.root,image=self.photoimg2,bd=0,relief=SUNKEN)
        L2.place(x=5,y=2,width=100,height=40)

        #-------------Label frame----------
        L_fleft=LabelFrame(self.root,bd=2,relief=SUNKEN,text="New Room Add",padx=2,font=("times new roman",12,"bold"))
        L_fleft.place(x=5,y=50,width=440,height=350)

        #-------------labels and entry------
        #Floor
        lbl_floor=Label(L_fleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        E_floor=ttk.Entry(L_fleft,textvariable=self.var_floor,font=("times new roman",13,"bold"),width=20)
        E_floor.grid(row=0,column=1,sticky=W)
        #Room No.
        lbl_RoomNo=Label(L_fleft,text="Room No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        E_RoomNo=ttk.Entry(L_fleft,textvariable=self.var_roomNo,font=("times new roman",13,"bold"),width=20)
        E_RoomNo.grid(row=1,column=1,sticky=W)
        #Room Type
        lbl_RoomType=Label(L_fleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        E_RoomType=ttk.Entry(L_fleft,textvariable=self.var_RoomType,font=("times new roman",13,"bold"),width=20)
        E_RoomType.grid(row=2,column=1,sticky=W)

        #=============Btns=========
        B_F=Frame(L_fleft,bd=2,relief=RIDGE)
        B_F.place(x=0,y=200,width=412,height=40)


        B_Add=Button(B_F,text="Add",command=self.add_data,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Add.grid(row=0,column=0,padx=1)

        B_Update=Button(B_F,text="Update",command=self.update,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Update.grid(row=0,column=1,padx=1)

        B_Delete=Button(B_F,text="Delete",command=self.mDelete,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Delete.grid(row=0,column=2,padx=1)

        B_Reset=Button(B_F,text="Reset",command=self.reset,font=("times new roman",12,"italic"),bg="black",fg="gold",width=10)
        B_Reset.grid(row=0,column=3,padx=1)

        #===========tabel frame======
        Table_Frame=LabelFrame(self.root,bd=2,relief=SUNKEN,text="Show Room Details",bg='light grey',padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
       

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
      
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Your_password",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_roomNo.get(),
                                                                                self.var_RoomType.get(),
                                                                                
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Succesfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)
    
    #To fetch data from the database.            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])

#Update function 
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                                                 
                                                                                                                                            self.var_floor.get(),
                                                                                                                                            self.var_RoomType.get(),
                                                                                                                                            self.var_roomNo.get(),
                                                                                                                                    
                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_RoomType.set(""),
        self.var_roomNo.set("")


        


if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()


