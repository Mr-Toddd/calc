# Python program to create a simple GUI Calculator using Tkinter

# importing from tkinter module
from tkinter import *

# globally declaring the expression variable
expression = ""

# function to update expression in the text entry box:
def press(num):
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)

# function to evaluate the final expression:
def equalpress():
	try:
		global expression

		# eval function evaluates the expression
		# and str function converts the result into string
		total = str(eval(expression))

		equation.set(total)

		# initializing the expression variable by empty string
		expression = ""

	# if error is generated, then handle by the except block
	except:
		equation.set(" error ")
		expression = ""

# function to clear the contents of text entry box:
def clear():
	global expression
	expression = ""
	equation.set("")

# driver code:
if __name__ == "__main__":
	# creating a GUI window
	gui = Tk()

	# setting the background colour of GUI window
	gui.configure(background = "gray")

	# setting the title of GUI window
	gui.title("Simple GUI Calculator")

	# setting the configuration of GUI window
	gui.geometry("600x480")
	equation = StringVar()

	# creating the text entry box for showing the expression
	expression_field = Entry(gui, textvariable = equation)

	# grid method is used for creating a table like structure
	expression_field.grid(columnspan = 4, ipadx = 70)

	# create buttons and placing at a particular location inside the root window .
	button1 = Button(gui, text=' 1 ', fg='white', bg='black',
					command=lambda: press(1), height=2, width=8)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='white', bg='black',
					command=lambda: press(2), height=2, width=8)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='white', bg='black',
					command=lambda: press(3), height=2, width=8)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='white', bg='black',
					command=lambda: press(4), height=2, width=8)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='white', bg='black',
					command=lambda: press(5), height=2, width=8)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='white', bg='black',
					command=lambda: press(6), height=2, width=8)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='white', bg='black',
					command=lambda: press(7), height=2, width=8)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='white', bg='black',
					command=lambda: press(8), height=2, width=8)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='white', bg='black',
					command=lambda: press(9), height=2, width=8)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='white', bg='black',
					command=lambda: press(0), height=2, width=8)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='white', bg='black',
				command=lambda: press("+"), height=2, width=8)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='white', bg='black',
				command=lambda: press("-"), height=2, width=8)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='white', bg='black',
					command=lambda: press("*"), height=2, width=8)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='white', bg='black',
					command=lambda: press("/"), height=2, width=8)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='white', bg='black',
				command=equalpress, height=2, width=8)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='white', bg='black',
				command=clear, height=2, width=8)
	clear.grid(row=5, column='1')

	decimal= Button(gui, text='.', fg='white', bg='black',
					command=lambda: press('.'), height=2, width=8)
	decimal.grid(row=6, column=0)

	# start the GUI
	gui.mainloop()

    