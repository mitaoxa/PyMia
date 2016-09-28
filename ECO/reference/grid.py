from Tkinter import *

class GUIDemo(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.grid()
		self.CW()

	def CW(self): #create Widget
		self.inputText=Label(self)
		self.inputText["text"]="Input:"
		self.inputText.grid(row=0,column=0)
		self.inputField=Entry(self)
		self.inputField["width"]=50
		self.inputField.grid(row=0, column=1, columnspan=6)


if __name__=='__main__':
	root=Tk()
	app=GUIDemo(master=root)
	app.mainloop()
