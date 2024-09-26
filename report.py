from tkinter import*
from PIL import Image,ImageTk
# from graph import Graphy
import graph2 as g
import pyttsx3
import matplotlib.pyplot as plt
class Reporth:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        f1=Frame(root,bg='peachpuff',borderwidth=50)
        f1.pack(side=RIGHT,fill=Y,pady=6)
        l=Label(f1,text="Welcome !!!",bg='red',fg='white',font=("Comic Sans MS",22,"italic"))
        l.pack(anchor=N,side=TOP,fill=Y,)

        B_Add=Button(f1,text="RoomType",command=self.add,font=("times new roman",16,"italic"),bg="black",fg="gold",width=10)
        B_Add.place(x=10,y=180,width=170,height=50)

        B_Add2=Button(f1,text="RoomBooked",command=self.add2,font=("times new roman",16,"italic"),bg="black",fg="gold",width=10)
        B_Add2.place(x=10,y=280,width=170,height=50)

        B_Add3=Button(f1,text="Customer anaylsis",command=self.add3,font=("times new roman",16,"italic"),bg="black",fg="gold",width=10)
        B_Add3.place(x=10,y=380,width=170,height=50)

        B_Add5=Button(f1,text="Feedback anaylsis",command=self.add5,font=("times new roman",16,"italic"),bg="black",fg="gold",width=10)
        B_Add5.place(x=10,y=480,width=170,height=50)

        img6=Image.open(r"sound.png")
        img6=img6.resize((150,70),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        B_Add3=Button(root,image=self.photoimg6,command=self.add4,borderwidth=0)
        B_Add3.place(x=1100,y=140,width=150,height=70)
        
        
        Head=Label(self.root,text="Hotel Report",font=("Algerian",28,"bold"),bg='black',fg='magenta',bd=6,relief=SUNKEN)
        Head.pack(fill=X,padx=4,pady=6)
        text1=Label(self.root,text="Lemon Tree, India's Strongest Brand across industries and sectors, is an iconic hospitality brand from the Indian Hotels Company Limited.",bg='white',fg='black',font=("Comic Sans MS",12,"italic"))
        text2=Label(self.root,text="The brand continues to be one of the most revered and loved hospitality brands with a legacy of over 116 years of impeccable service",bg='white',fg='black',font=("Comic Sans MS",12,"italic"))
        text3=Label(self.root,text="The brand has more than 700+ branches across 60+ countries in the world",bg='white',fg='black',font=("Comic Sans MS",12,"italic"))
        text1.pack()
        text2.pack()
        text3.pack()

        img5=Image.open(r"hotel.png")
        img5=img5.resize((850,570),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        L5=Label(self.root,image=self.photoimg5,bd=4,relief=SUNKEN)
        L5.place(x=220,y=180,width=850,height=570)

    def add(self):
        g.fetch_data()
    def add2(self):
        g.fetch_data2()
    def add3(self):
        g.fetch_data3()
    def add4(self):
        text_speech=pyttsx3.init()
        answer="""Lemon Tree, India's Strongest Brand across industries and sectors, is an iconic hospitality brand from the Indian Hotels Company Limited.
        The brand continues to be one of the most revered and loved hospitality brands with a legacy of over 116 years of impeccable service.
        The brand has more than 700+ branches across 60+ countries in the world"""
        text_speech.say(answer)
        text_speech.runAndWait()
    def add5(self):
        List1 = open("feed12.txt",'r')
        sum=list()
        sum2=list()
        sum=List1.readlines()
        sum[0]=(int(sum[0]))
        sum[1]=(int(sum[1]))
        sum[2]=(int(sum[2]))
        sum[3]=(int(sum[3]))
        sum[4]=(int(sum[4]))
        for i in range(0,5):
            sum2.append(sum[i])
        List1.close()
        # print(sum2) 
        fig = plt.figure(figsize = (6, 6))
        plt.xlabel("Rating",fontdict= {'family':'arial','color':'blue','size':16})
        plt.ylabel("No. of customers",fontdict= {'family':'arial','color':'blue','size':16})
        plt.title("Customer Feedback",fontdict= {'family':'fantasy','color':'black','size':20},weight='bold')
        plt.bar('Excellent', color ='limegreen',edgecolor ='grey', label ='Excellent',height=sum2[0],width=0.5)
        plt.bar('Happy', color ='yellowgreen',edgecolor ='grey', label ='Happy',height=sum2[1],width=0.5)
        plt.bar('Neutral', color ='lightyellow',edgecolor ='grey', label ='Neutral',height=sum2[2],width=0.5)
        plt.bar('Unhappy', color ='darkorange',edgecolor ='grey', label ='Unhappy',height=sum2[3],width=0.5)
        plt.bar('Poor', color ='red',edgecolor ='grey', label ='Poor',height=sum2[4],width=0.5)
        plt.legend()
        plt.show()

if __name__=="__main__":
    root=Tk()
    obj=Reporth(root)
    root.mainloop()
