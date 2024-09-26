from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from report import Reporth
import pyttsx3 as pts
from feedback import Rating


class HotelManagementSystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Hotel Management System")
                self.root.geometry("1550x800+0+0")
        #------------------1st Image---------------------#
                img1=Image.open(r"hotel2.jpg")
                img1=img1.resize((1550,140),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                L1=Label(self.root,image=self.photoimg1,bd=4,relief=SUNKEN)
                L1.place(x=0,y=0,width=1550,height=140)
                

        #------------------2nd Image Logo---------------------#
                img2=Image.open(r"Logo1.png")
                img2=img2.resize((230,140),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                L2=Label(self.root,image=self.photoimg2,bd=4,relief=SUNKEN)
                L2.place(x=0,y=0,width=230,height=140)

        #----------------TITLE---------
                L_T1=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Algerian",24,"bold"),bg='black',fg='magenta',bd=6,relief=SUNKEN)
                L_T1.place(x=0,y=140,width=1550,height=50)
                # L_T1.pack(fill=X,pady=140)

        #-----------------Frame1 Big below Hotel mange -------
                F1=Frame(self.root,bd=4,bg='light grey',relief=GROOVE)
                F1.place(x=0,y=190,width=1550,height=620)
        #----------------MENU----------
                L_M1=Label(F1,text="MENU",font=("times new roman",18,"bold"),bg='black',fg='magenta',bd=6,relief=SUNKEN)
                L_M1.place(x=0,y=0,width=230)
        #-----------------Frame2 Left palette containing menu-------
                F2=Frame(F1,bd=4,bg='peachpuff',relief=RIDGE)
                F2.place(x=0,y=35,width=228,height=390)    
        #---------#------Below Menu BUTTTON-------
                B1=Button(F2,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",16,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
                B1.grid(row=0,column=0,pady=10)
                B2=Button(F2,text="ROOM",command=self.roombooking,width=22,font=("times new roman",16,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
                B2.grid(row=1,column=0,pady=10)
                B3=Button(F2,text="DETAILS",command=self.details_room,width=22,font=("times new roman",16,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
                B3.grid(row=2,column=0,pady=10)
                B4=Button(F2,text="REPORT",width=22,command=self.report_h,font=("times new roman",16,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
                B4.grid(row=3,column=0,pady=10)
                B6=Button(F2,text="FEEDBACK",command=self.feed1,width=22,font=("times new roman",16,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
                B6.grid(row=4,column=0,pady=10)
                B5=Button(F2,text="LOGOUT",command=self.logout,width=22,font=("times new roman",16,"italic"),bg='black',fg='cyan',bd=0,relief=SUNKEN,cursor="hand1")
                B5.grid(row=5,column=0,pady=10)
        #-------------------RIGHT SIDE IMAGE-----------
                img3=Image.open(r"h2.jpg")
                img3=img3.resize((1310,590),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                L3=Label(F1,image=self.photoimg3,bd=4,relief=SUNKEN)
                L3.place(x=225,y=0,width=1310,height=590)
        #------------------Left side small Images----
                # img4=Image.open(r"food.jpg")
                # img4=img4.resize((230,210),Image.ANTIALIAS)
                # self.photoimg4=ImageTk.PhotoImage(img4)

                # L4=Label(F1,image=self.photoimg4,bd=4,relief=SUNKEN)
                # L4.place(x=0,y=225,width=230,height=210)

                img5=Image.open(r"food.jpg")
                img5=img5.resize((230,190),Image.ANTIALIAS)
                self.photoimg5=ImageTk.PhotoImage(img5)

                L5=Label(F1,image=self.photoimg5,bd=4,relief=SUNKEN)
                L5.place(x=0,y=382,width=225,height=210)
                # img5=Image.open(r"hotel.png")
                # img5=img5.resize((230,190),Image.ANTIALIAS)
                # self.photoimg5=ImageTk.PhotoImage(img5)

                # L5=Label(F1,image=self.photoimg5,bd=4,relief=SUNKEN)
                # L5.place(x=0,y=420,width=230,height=190)

                # Speech
                text_speech=pts.init()
                answer="Welcome to Lemon Tree Hotel"
                text_speech.say(answer)
                text_speech.runAndWait()
                # Speechend
        
        def cust_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Cust_Win(self.new_window)

        def roombooking(self):
                self.new_window=Toplevel(self.root)
                self.app=Roombooking(self.new_window)

        def details_room(self):
                self.new_window=Toplevel(self.root)
                self.app=DetailsRoom(self.new_window)

        def report_h(self):
                self.new_window=Toplevel(self.root)
                self.app=Reporth(self.new_window)

        def feed1(self):
               self.new_window=Toplevel(self.root)
               self.app=Rating(self.new_window)

        def logout(self):
        #        Speech
               text_speech=pts.init()
               answer="Thank You, Visit Again"
               text_speech.say(answer)
               text_speech.runAndWait()
        #        Speechend
               self.root.destroy()
               
        



if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
    
