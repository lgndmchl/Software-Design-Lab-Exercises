from tkinter import *


# method that converts temperature in celsius to fahrenheit
def convertToFahrenheit(celsius):
    return (celsius * (9 / 5)) + 32


# method that converts temperature in fahrenheit to celsius
def convertToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# creating a window
root = Tk()

# setting up DoubleVar variables for accessing/mutating values of Entry fields
fahVar=DoubleVar()
fahVar.set(32) #using 32.0 as default value for fahrenheit
celVar=DoubleVar()

#arranging equal widths for each column on the grid
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)

#creating labels in first row
Label(root,text='Fahrenheit').grid(row=0, column=0)
Label(root,text='Celsius').grid(row=0, column=1)

#Entry objects in second row. setting fahVar as textvariable of first entry
#and celVar as textvariable of second Entry
Entry(root,textvariable=fahVar).grid(row=1, column=0)
Entry(root,textvariable=celVar).grid(row=1, column=1)

#creating and adding buttons in third row
#enabling >>>> button to call convertToCelsius method passing current fahrenheit value and update
#the result in entry field controlled by celVar, and vice versa
Button(root,text='>>>>', command=lambda: celVar.set(convertToCelsius(fahVar.get()))).grid(row=2, column=0)
Button(root,text='<<<<', command=lambda: fahVar.set(convertToFahrenheit(celVar.get()))).grid(row=2, column=1)

#displaying until user quits
root.mainloop()
