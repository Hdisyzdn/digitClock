
#  1400148058 پروژه درس ساختمان داده و طراحی الگوریتم حدیثه یزدانی 1400 148 100 و پارسا شفیغی

from tkinter import *
import time
import calendar

year = 2023
month = 10
page = calendar.month( year , month)

window = Tk ()
window.title('Digitl Clock')
window.geometry('550x500')

def myTime ():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm  = time.strftime('%p')
    day    = time.strftime('%A')
    zone   = time.strftime('%Z')
   
    myText = hour + ":" + minute + ":" + second  + " " + am_pm
    myText2 = day + " ," + zone
    myText3 = page 
    myLabel.config  (text = myText)
    myLabel2.config (text = myText2)
    myLabel3.config (text = myText3)

    myLabel.after (1000, myTime)

myLabel = Label(window , text = "",font=(
    'Aria1', 72) , fg='white' , bg='blue')
myLabel.pack()

myLabel2 = Label(window,text = "" , font=("Arial" , 24))
myLabel2.pack()

myLabel3 = Label(window,text = "" , font=("Arial" , 24))
myLabel3.pack()

myTime()

window.mainloop()
