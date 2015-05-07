import sys
import time
import Tkinter as tk
from Tkinter import *

sign = set()

master = Tk()

master.title("Sign In")

v = StringVar()

inp = None

canvas = Canvas()

master.geometry("250x150+300+300")

e = Entry(master, textvariable = v, bd =5 )

e.pack()

e.focus_set()

def callback(args):
	# sign.add(e.get())
#	clear()
	val = (e.get()) 
	equalLoc = val.find('=')
	val = "N"+ val[2:-6]
	if(val == "exit"):
			master.quit()
	print val
	if(not(val in sign) and len(val)== 9):
		sign.add(val)
		logic(True)
	else:
		logic(False)
	clear()
	print sign
   # clear()
#    print "yolo"

def clear():
    e.delete(0,'end')
    #canvas.delete("all")

b=Button(master, text="clear",width=10,command=clear)
b.pack()


master.bind('<Return>', callback)
def logic(yolo):
	if(yolo == False):
		canvas.create_oval(10, 10, 80, 80, outline="white", 
    		fill="red", width=2)
	else:
                canvas.delete("all")
		canvas.create_oval(10, 10, 80, 80, outline="white", 
    		fill="green", width=2)
	canvas.pack()
        #time.sleep(5)
        #canvas.delete("all")

mainloop()
f = open("backup.txt", 'w')
print >> f, sign 
print sign
