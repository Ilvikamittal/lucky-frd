from tkinter import*
import random
root=Tk()

root.title("friend names")
root.geometry("400x600")
root.configure(background="blue")

nameInput=Entry(root)
nameInput.place(relx=0.5,rely=0.2,anchor=CENTER)

friendList=Label(root)
friendList.place(relx=0.5,rely=0.4,anchor=CENTER)

lucky_friend=Label(root)
lucky_friend.place(relx=0.5,rely=0.6,anchor=CENTER)    

frd_list=[]

def addFriend():
    print("adding friend")
    name=nameInput.get()
    frd_list.append(name)  
    friendList["text"]="Your friend's list: "+str(frd_list)
    

btn_1=Button(root,text="Add friends to the list",command=addFriend)
btn_1.place(relx=0.5,rely=0.3,anchor=CENTER)



def luckyFrd():
    print("lucky friend")
    length=len(frd_list)
    randomNumber=random.randint(0,length-1)
    friend=frd_list[randomNumber]
    lucky_friend["text"]="Your lucky friend is: "+str(friend)
    
btn_2=Button(root,text="who's my lucky friend",command=luckyFrd)
btn_2.place(relx=0.5,rely=0.5,anchor=CENTER)






root.mainloop()


