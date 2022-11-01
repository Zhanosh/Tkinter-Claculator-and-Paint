from ast import keyword
from distutils.command.config import config
from operator import ne
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from turtle import bgcolor, window_height
from typing import KeysView
import webbrowser

def nextWindow():
    class newwindow():
        nextwindow=tk.Tk()
        btn_Paint_Page=Button(nextwindow,text="Paint",command=lambda :paint_Page(),border=5,activebackground="white",background="dimgray",fg="white",width=10)
        btn_Paint_Page.grid()



            

        nextwindow.mainloop()


icon_win="cal_tk.ico"

numm=''
none = ""


def z():
    number=""
    number=int(entry1.get())
    number = number * number
    entry1.set(number)
    return number


def web_Filimo():
    webbrowser.open_new('https://www.filimo.com')


#=======================================================================
#=======================================================================


#============================Calculator funcrion===========================================
def press(num):
    global  none
    none= none + str(num)
    entry1.set(none)

def equalprees():
    try:
        global none
        total = str(eval(none))
        entry1.set(total)
        none=""
    except:
        entry1.set("error")
        none=""

def clear():
    global none
    none=""
    entry1.set("")
#=======================================================================
#=======================================================================


#============================Paint window===========================================
def paint_Page():


    class Paint(object):

        DEFAULT_PEN_SIZE = 1
        DEFAULT_COLOR = 'black'

        def __init__(self):
            self.root = Tk()
            self.root.configure(background="gray")
            self.pen_button = Button(self.root, text='pen', command=self.use_pen,background="gray")
            self.pen_button.grid(row=0, column=0)

            self.brush_button = Button(self.root, text='brush', command=self.use_brush,background="gray")
            self.brush_button.grid(row=0, column=1)

            self.color_button = Button(self.root, text='color', command=self.choose_color,background="gray")
            self.color_button.grid(row=0, column=2)

            self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser,background="gray")
            self.eraser_button.grid(row=0, column=3)

            self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL,background="gray")
            self.choose_size_button.grid(row=0, column=4)

            self.c = Canvas(self.root, bg='white', width=600, height=600)
            self.c.grid(row=1, columnspan=5)

            self.setup()
            self.root.mainloop()

        def setup(self):
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)

        def use_pen(self):
            self.activate_button(self.pen_button)

        def use_brush(self):
            self.activate_button(self.brush_button)

        def choose_color(self):
            self.eraser_on = False
            self.color = askcolor(color=self.color)[1]

        def use_eraser(self):
            self.activate_button(self.eraser_button, eraser_mode=True)

        def activate_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=RAISED)
            some_button.config(relief=SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode

        def paint(self, event):      #حرکت موس
            self.line_width = self.choose_size_button.get()
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=self.line_width, fill=paint_color,
                                   capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.old_x = event.x                            #حرکت موس
            self.old_y = event.y               #حرکت موس

        def reset(self, event):          #حرکت موس
            self.old_x, self.old_y = None, None                   #حرکت موس

    if __name__ == '__main__':
        Paint()
#=========================================================================================
#=========================================================================================


HEIGHT=300
WIDTH=500



#===============******Calculator Window******===============

window =tk.Tk()

#======================== Window desingn =================================
# window.iconbitmap(icon_win)
window.title("Calculator App")
window.resizable(width=True,height=True)
window.geometry("355x360")
window.configure(background="gray")
window.resizable(width=False,height=False)
#========================================================================
#========================================================================





# label_1=Label(window,text='----------------------------------------------------------',background='gray')
# label_1.grid(columnspan=4,ipadx=20,row=6)
# label_Other=Label(window,text='===Other===',background="gray")
# label_Other.grid(columnspan=4,row=7,ipadx=10)



#=========================Netflix button=================================
# btn_Filimo=Button(window,text='Filimo',background='gray',command=web_Filimo)
# btn_Filimo.grid(row=8,column=3)

#========================================================================
#========================================================================


#======================== Calculator Entry =============================
entry1=StringVar()

input_Number=Entry(window,textvariable=entry1,background="silver")
input_Number.grid(columnspan=4,ipadx=113.5,column=0,row=0,padx=2,pady=2,ipady=10)

#========================================================================
#========================================================================




#======================== Calculator button =============================
btn_Number_1=Button(window,text="1",command=lambda :press(1),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_1.grid(column=0,row=1)

btn_Number_2=Button(window,text="2",command=lambda :press(2),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_2.grid(column=1,row=1)

btn_Number_3=Button(window,text="3",command=lambda :press(3),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_3.grid(column=2,row=1)

btn_Number_4=Button(window,text="4",command=lambda :press(4),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_4.grid(column=0,row=2)

btn_Number_5=Button(window,text="5",command=lambda :press(5),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_5.grid(column=1,row=2)

btn_Number_6=Button(window,text="6",command=lambda :press(6),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_6.grid(column=2,row=2)

btn_Number_7=Button(window,text="7",command=lambda :press(7),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_7.grid(column=0,row=3)

btn_Number_8=Button(window,text="8",command=lambda :press(8),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_8.grid(column=1,row=3)

btn_Number_9=Button(window,text="9",command=lambda :press(9),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_9.grid(column=2,row=3)

btn_Number_0=Button(window,text="0",command=lambda:press(0),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Number_0.grid(column=1,row=4)

btn_Plus=Button(window,text="+",command=lambda:press("+"),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Plus.grid(column=3,row=1)

btn_Equal=Button(window,text="=",command=lambda:equalprees(),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Equal.grid(column=2,row=4)

btn_Negative=Button(window,text="-",command=lambda:press('-'),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Negative.grid(row=2,column=3)

btn_Distribution=Button(window,text="/",command=lambda:press('/'),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Distribution.grid(column=3,row=4)

btn_Hit=Button(window,command=lambda :press('*'),text="*",border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Hit.grid(column=3,row=3)

btn_Dot=Button(window,text=".",command=lambda:press('.'),border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Dot.grid(column=0,row=4)

btn_Clear=Button(window,text="clear",command=clear,border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_Clear.grid(column=2,row=5)

btn_to_the_power_of_two=Button(window,text='n²',command=z,border=5,activebackground="white",background="dimgray",fg="white",width=10,height=3)
btn_to_the_power_of_two.grid(column=1,row=5)

btn_Next_Page=Button(window,text='Next page',command=nextWindow,activebackground="white",background='#E0EEEE',fg="black",width=8,height=2)
btn_Next_Page.grid(column=3,row=5)
#=================================================================================================================
#=================================================================================================================




#====================================================================
#====================================================================
#====================================================================
#                        Thanks for use the app 
window.mainloop()
def exit_message():
    messagebox.showinfo("Thanks",'maker is zhano')
    return exit_message


exit_message()

#====================================================================
#====================================================================
#====================================================================

#                *Created by ZhanoSh*
