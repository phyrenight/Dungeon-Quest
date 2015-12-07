from Tkinter import *
top = Tk()
top.title("Box")
top.geometry("200x200")
app = Frame(top)
app.grid()
label = Label(app, text = "This is a label")
label.grid()
button1 = Button(app, text = "This is a button.")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "This will show text'")

button3 = Button(app)
button3.grid()
button3["text"] = "This will show up as well."

top.mainloop()

def time():
	print "What is the time?"
	
if __name__ == "__main__":

	print " do you know what time it is?"
	
