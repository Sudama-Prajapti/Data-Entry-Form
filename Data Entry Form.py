from tkinter import*
from tkinter import messagebox
root = Tk() 
root.title("Data Entry Software Author :- Sudama Prajapti")
root.geometry("1920x1080")

def savedata(): #Define Function
    fp = open("D:/sudama.xls","a+") #a+ Append Text Input
    tt = txtt.get() # Title
    fn = txtf.get() #first name 
    ln = txtl.get() # last Name
    d = txtd.get() # Designation
    C = txtc.get() # Company Name
    
    fp.write(tt)
    fp.write(" ")
    fp.write(fn)
    fp.write(" ") 
    fp.write(ln)
    fp.write(" ")
    fp.write(d)
    fp.write(" ")
    fp.write(C)
    fp.write(" \n") #\n When you save Data to Insert to Next Rows
    
    fp.close()
    messagebox.showinfo("Save", "Data entry successfully")
    txtf.delete(0,END)
    txtl.delete(0,END)
    txtd.delete(0,END)
    txtt.delete(0,END)
    txtc.delete(0,END)


lblh = Label(root,text ="Customer Data entry Form",font="TimesNewRoman 30 bold") # Heading
lblh.grid(row = 0,column = 0,padx = 10,pady = 10,ipady = 10,ipadx = 10)

# Lable Boxes
Iblt = Label(root,text = "Title :",font="TimesNewRoman 15 bold")
Iblf = Label(root,text = "Enter First Name : ",font = "TimesNewRoman 15 bold")
Ibll = Label(root,text = "Enter Last Name : ",font = "TimesNewRoman 15 bold")
Ibld = Label(root,text = "Enter Designation :  ",font = "TimesNewRoman 15 bold") 
Iblc = Label(root,text = "Enter Company Name :  ",font = "TimesNewRoman 15 bold")

# Txt Boxes
txtt = Entry(root,font = "TimesNewRoman 15 bold")
txtf = Entry(root,font = "TimesNewRoman 15 bold")
txtl = Entry(root,font = "TimesNewRoman 15 bold")
txtd = Entry(root,font = "TimesNewRoman 15 bold")
txtc = Entry(root,font = "TimesNewRoman 15 bold")

# Place In One Line
Iblt.grid(row = 3,column = 0,padx = 15,pady = 15,ipady = 5,ipadx = 15)
txtt.grid(row = 3,column = 1,padx = 15,pady = 15,ipady = 5,ipadx = 30)

Iblf.grid(row = 4,column = 0,padx = 15,pady = 15,ipady = 5,ipadx = 15)
txtf.grid(row = 4,column = 1,padx = 15,pady = 15,ipady = 5,ipadx = 30) #ipady Mens Row Height #ipadx mens Row Width

Ibll.grid(row = 5,column = 0,padx = 15,pady = 15,ipady = 5,ipadx = 15)
txtl.grid(row = 5,column = 1,padx = 15,pady = 15,ipady = 5,ipadx = 30)

Ibld.grid(row = 6,column=0,padx=15,pady=15,ipady=5,ipadx=15)
txtd.grid(row = 6,column = 1,padx = 15,pady = 15,ipady = 5,ipadx = 30)

Iblc.grid(row = 7,column = 0,padx = 15,pady = 15,ipady = 5,ipadx = 15)
txtc.grid(row = 7,column = 1,padx = 15,pady = 15,ipady = 5,ipadx = 30)


Save_Button=Button(root,text="Save",font="TimesNewRoman 15 bold",bg="green",command=savedata)
Save_Button.grid(row = 8,column = 1,padx = 20,pady = 20 ,ipady = 15,ipadx = 20)


root.mainloop()
