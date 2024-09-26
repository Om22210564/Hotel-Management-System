from tkinter import*
from PIL import Image,ImageTk
import pyttsx3 as pts
# import matplotlib.pyplot as plt

class Rating:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback")
        self.root.geometry("850x180+300+400")
        
        
        
        text3=Label(self.root,text="How would you like to rate us?",bg='white',fg='black',font=("fantasy",16,"bold"))
        text3.pack()
        img66=Image.open(r"Excellent_emoji.png")
        img66=img66.resize((100,100),Image.ANTIALIAS)
        self.photoimg66=ImageTk.PhotoImage(img66)
        B_Add36=Button(self.root,command=self.close,image=self.photoimg66,borderwidth=0)
        B_Add36.place(x=50,y=50,width=100,height=100)

        img61=Image.open(r"Good_emoji.png")
        img61=img61.resize((100,100),Image.ANTIALIAS)
        self.photoimg61=ImageTk.PhotoImage(img61)
        B_Add31=Button(self.root,command=self.close1,image=self.photoimg61,borderwidth=0)
        B_Add31.place(x=200,y=50,width=100,height=100)

        img62=Image.open(r"Neutral_emoji.png")
        img62=img62.resize((100,100),Image.ANTIALIAS)
        self.photoimg62=ImageTk.PhotoImage(img62)
        B_Add32=Button(self.root,command=self.close2,image=self.photoimg62,borderwidth=0)
        B_Add32.place(x=350,y=50,width=100,height=100)

        img63=Image.open(r"Poor_emoji.png")
        img63=img63.resize((100,100),Image.ANTIALIAS)
        self.photoimg63=ImageTk.PhotoImage(img63)
        B_Add33=Button(self.root,command=self.close3,image=self.photoimg63,borderwidth=0)
        B_Add33.place(x=500,y=50,width=100,height=100)

        img64=Image.open(r"Angry_emoji.png")
        img64=img64.resize((100,100),Image.ANTIALIAS)
        self.photoimg64=ImageTk.PhotoImage(img64)
        B_Add34=Button(self.root,command=self.close4,image=self.photoimg64,borderwidth=0)
        B_Add34.place(x=650,y=50,width=100,height=100)


#Here starts the confusion
    def close(self):
        List1 = open("feed12.txt",'r')
        sum=list()
        sum=List1.readlines()
        sum[0]=str(int(sum[0])+1)
        sum[1]=str(int(sum[1])+0)
        sum[2]=str(int(sum[2])+0)
        sum[3]=str(int(sum[3])+0)
        sum[4]=str(int(sum[4])+0)
        List1.close()
        List1=open("feed12.txt",'w')
        for item in sum:
            List1.write(item+"\n")
        text_speech=pts.init()
        answer="Thanks for the feedback"
        text_speech.say(answer)
        text_speech.runAndWait()
        self.root.destroy()
    def close1(self):
        List1 = open("feed12.txt",'r')
        sum=list()
        sum=List1.readlines()
        sum[0]=str(int(sum[0])+0)
        sum[1]=str(int(sum[1])+1)
        sum[2]=str(int(sum[2])+0)
        sum[3]=str(int(sum[3])+0)
        sum[4]=str(int(sum[4])+0)

        List1.close()
        List1=open("feed12.txt",'w')
        for item in sum:
            List1.write(item+"\n")
        text_speech=pts.init()
        answer="Thanks for the feedback"
        text_speech.say(answer)
        text_speech.runAndWait()
        self.root.destroy()
    def close2(self):
        List1 = open("feed12.txt",'r')
        sum=list()
        sum=List1.readlines()
        sum[0]=str(int(sum[0])+0)
        sum[1]=str(int(sum[1])+0)
        sum[2]=str(int(sum[2])+1)
        sum[3]=str(int(sum[3])+0)
        sum[4]=str(int(sum[4])+0)
        List1.close()
        List1=open("feed12.txt",'w')
        for item in sum:
            List1.write(item+"\n")
        text_speech=pts.init()
        answer="Thanks for the feedback"
        text_speech.say(answer)
        text_speech.runAndWait()
        self.root.destroy()
    def close3(self):
        List1 = open("feed12.txt",'r')
        sum=list()
        sum=List1.readlines()
        sum[0]=str(int(sum[0])+0)
        sum[1]=str(int(sum[1])+0)
        sum[2]=str(int(sum[2])+0)
        sum[3]=str(int(sum[3])+1)
        sum[4]=str(int(sum[4])+0)
        List1.close()
        List1=open("feed12.txt",'w')
        for item in sum:
            List1.write(item+"\n")
        text_speech=pts.init()
        answer="Thanks for the feedback"
        text_speech.say(answer)
        text_speech.runAndWait()
        self.root.destroy()
    def close4(self):
        List1 = open("feed12.txt",'r')
        sum=list()
        sum=List1.readlines()
        sum[0]=str(int(sum[0])+0)
        sum[1]=str(int(sum[1])+0)
        sum[2]=str(int(sum[2])+0)
        sum[3]=str(int(sum[3])+0)
        sum[4]=str(int(sum[4])+1)
        List1.close()
        List1=open("feed12.txt",'w')
        for item in sum:
            List1.write(item+"\n")
        text_speech=pts.init()
        answer="Thanks for the feedback"
        text_speech.say(answer)
        text_speech.runAndWait()
        self.root.destroy()

        

        
    # feed()
if __name__=="__main__":
    root=Tk()
    obj=Rating(root)
    root.mainloop()
    