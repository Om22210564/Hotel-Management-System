import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import matplotlib.image as mpimg

# if __name__=="__main__":
def fetch_data():
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        
        rows=my_cursor.fetchall()
        Room_type_Elite = 0
        Room_type_Double = 0
        Room_type_Single = 0

        for i in rows:
            # print(i)
            if i==('Elite',):
                Room_type_Elite=Room_type_Elite+1
            elif i==('Double',):
                Room_type_Double=Room_type_Double+1
            elif i==('Single',):
                Room_type_Single=Room_type_Single+1
                
        # print("Hello world",Room_type_Elite)
        # print("Hello world",Room_type_Double)
        # print("Hello world",Room_type_Single)
        fig = plt.figure(figsize = (5, 5))
        plt.xlabel("RoomType",fontdict= {'family':'arial','color':'blue','size':16})
        plt.ylabel("No. of Rooms Available",fontdict= {'family':'arial','color':'blue','size':16})
        plt.title("No. of different rooms Available",fontdict= {'family':'fantasy','color':'black','size':20},weight='bold')
        plt.bar('Single', color ='yellowgreen',edgecolor ='grey', label ='Single',height=Room_type_Single,width=0.5)
        plt.bar('Double', color ='lightyellow',edgecolor ='grey', label ='Double',height=Room_type_Double,width=0.5)
        plt.bar('Elite', color ='darkorange',edgecolor ='grey', label ='Elite',height=Room_type_Elite,width=0.5)
        plt.legend()
        plt.show()

def fetch_data2():
        conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from room")
        
        rows=my_cursor.fetchall()
        Room_type_Elite = 0
        Room_type_Double = 0
        Room_type_Single = 0

        for i in rows:
            # print(i)
            if i==('Elite',):
                Room_type_Elite=Room_type_Elite+1
            elif i==('Double',):
                Room_type_Double=Room_type_Double+1
            elif i==('Single',):
                Room_type_Single=Room_type_Single+1
                
        # print("Hello world",Room_type_Elite)
        # print("Hello world",Room_type_Double)
        # print("Hello world",Room_type_Single)
        fig = plt.figure(figsize = (5, 5))
        plt.xlabel("RoomType",fontdict= {'family':'arial','color':'blue','size':16})
        plt.ylabel("No. of Rooms Booked",fontdict= {'family':'arial','color':'blue','size':16})
        plt.title("No. of different rooms booked",fontdict= {'family':'fantasy','color':'black','size':20},weight='bold')
        plt.bar('Single', color ='yellowgreen',edgecolor ='grey', label ='Single',height=Room_type_Single,width=0.5)
        plt.bar('Double', color ='lightyellow',edgecolor ='grey', label ='Double',height=Room_type_Double,width=0.5)
        plt.bar('Elite', color ='darkorange',edgecolor ='grey', label ='Elite',height=Room_type_Elite,width=0.5)
        plt.legend()
        plt.show()

# fetch_data()
    # fetch_data()

def fetch_data3():
    conn=mysql.connector.connect(host="localhost",username="root",password="Your_Password",database="management")
    my_cursor=conn.cursor()
    my_cursor.execute("select noOfdays from room")
    
    rows=my_cursor.fetchall()
    # print(rows)
    # print(type(rows))
    list1,list2=list(),list()
    for i in rows:
         for j in i:
            list12=int(j)
            list1.append(list12)
    # print(list1)
    # print(len(list1))
    for i in range(1,len(list1)+1):
        list2.append(i)
    # print(list2)
         
    x=list2
    y=list1
    fig = plt.figure(figsize = (6, 6))
    mngr= plt.get_current_fig_manager()
    mngr.window.geometry("+0+0")
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
            marker='o', markerfacecolor='blue', markersize=7)

    # setting x and y axis range
    plt.ylim(1,80)
    plt.xlim(1,8)

    # naming the x axis
    plt.xlabel('Customer',fontdict= {'family':'arial','color':'red','size':16})
    # naming the y axis
    plt.ylabel('No. of Days stayed',fontdict= {'family':'arial','color':'red','size':16})

    # giving a title to my graph
    plt.title('No. of Days Customer Stayed',fontdict= {'family':'fantasy','color':'black','size':20},weight='bold')

    # function to show the plot
    plt.show()



# fetch_data3()



