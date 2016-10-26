from Tkinter import *
import tkMessageBox

def beenClicked():
    radioValue=relStatus.get()
    tkMessageBox.showinfo("You clicked", radioValue)
    return

def changeLabel():
    name="Hello "+yourName.get()
    labelText.set(name)
    yourName.delete(0, END)
    yourName.insert(0, "My name is Ben")
    return

app=Tk()
app.title("GUI test")
app.geometry('450x300+200+200')

labelText=StringVar()
labelText.set("Click Button")
label1=Label(app,textvariable=labelText,height=4)
label1.pack()

checkBoxVal=IntVar()
checkBox1=Checkbutton(app, variable=checkBoxVal, text="Happy?")
checkBox1.pack()

custName=StringVar(None)
yourName=Entry(app, textvariable=custName)
yourName.pack()

relStatus=StringVar()
relStatus.set(None)
radio1=Radiobutton(app, text="Student", value="Student", variable=relStatus, command=beenClicked).pack()
radio1=Radiobutton(app, text="Teacher", value="Teacher", variable=relStatus, command=beenClicked).pack()
radio1=Radiobutton(app, text="Other", value="Other", variable=relStatus, command=beenClicked).pack()

button1=Button(app, text="Click Here", width=20, command=changeLabel)
button1.pack(side='bottom', padx=15,pady=15)

app.mainloop()

