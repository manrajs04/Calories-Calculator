# Project 1
# Manraj S

from tkinter import *

root = Tk()

root.title("Calories Calculator")
root.minsize(500,350)
root.configure(bg='lavenderblush')

def gender():
        return(clicked.get())
def exe():
        return(clicked1.get())

def f1():
        w = int(E1.get())
        h = int(E2.get())
        a = int(E3.get())
        if exe()== "No exercise":
                amo = 1.2
        elif exe()== "Occasional":
                amo = 1.35
        elif exe()== "Moderate":
                amo = 1.50
        elif exe()== "Active":
                amo = 1.65
        else:
                amo = 1.80
        
        if gender()== "Male":
                cal = ((10*w)+(6.25*h)-(5*a)+5)
                calf = cal * amo
                LR.config(text="Minimum calories needed per day: " + str(calf))
        elif gender()== "Female":
                cal1 = ((10*w)+(6.25*h)-(5*a)+161)
                calf1 = cal1 * amo
                LR.config(text="Calories: " + str(calf1))
        
# Dropdown gender options

options = [
	"Male",
	"Female",
]


clicked = StringVar()

clicked.set( "Choose..." )

drop = OptionMenu( root , clicked , *options )
drop.pack()
drop.place(x=250, y=5)
drop.configure(background="lavenderblush", foreground="black")


L1 = Label(text = "Select Gender: ", background="lavenderblush", foreground="black")
L1.place(x=10, y=5)

# Dropdown Exercise options

options = [
	"No exercise",
	"Occasional",
        "Moderate",
        "Active",
        "Very Active",
]

clicked1 = StringVar()

clicked1.set( "Choose..." )

drop1 = OptionMenu( root , clicked1 , *options )
drop1.pack()
drop1.place(x=250, y=35)
drop1.configure(background="lavenderblush", foreground="black")

L5 = Label(text = "Select exercise level: ", background="lavenderblush", foreground="black")
L5.place(x=10, y=35)


# Other Information

LR = Label(text="Result: ", background="lavenderblush", foreground="black" )
LR.place(x=100, y=275)

L2 = Label(text="Enter your Weight in kilograms: ", background="lavenderblush", foreground="black" )
L2.place(x=10, y=75)

L3 = Label(text="Enter your Height in centimetres: ", background="lavenderblush", foreground="black" )
L3.place(x=10, y=120)

L4 = Label(text="Enter your Age : ", background="lavenderblush", foreground="black" )
L4.place(x=10, y=165)

E1 = Entry()
E1.place(x=250, y=75)
E1.configure(background='white', foreground='black')

E2 = Entry()
E2.place(x=250, y=120)
E2.configure(background='white', foreground='black')

E3 = Entry()
E3.place(x=250, y=165)
E3.configure(background='white', foreground='black')

B1 = Button(text='Calculate', command=f1)
B1.place(x=200, y=215)
B1.configure(background= "white", foreground="black")

root.mainloop()
