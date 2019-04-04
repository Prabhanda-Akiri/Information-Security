from tkinter import *
import cyclic_attack as cy
import chosen_cipher_attack as chci
import blind_attack as blind 

def b1():
	
	clear_screen()
	wlcm = Label(window, text="Cyclic Attack Program\n")
	wlcm.pack() 

	ctext = Label(window, text="\nEnter Cipher Text:")
	ctext.pack()
	global txt1
	txt1 = Entry(window,width=20)
	txt1.pack()

	Nval = Label(window, text="N:")
	Nval.pack()
	global txt2
	txt2 = Entry(window,width=20)
	txt2.pack()

	Eval = Label(window, text="e:")
	Eval.pack()
	global txt3
	txt3 = Entry(window,width=20)
	txt3.pack()

	space_lbl = Label(window, text="\n\n")
	space_lbl.pack()

	ptextb = Button(window, text="Get Plain Text", command=b1c1) 
	ptextb.pack()

def b1c1():

	ci_text=int(txt1.get())
	N=int(txt2.get())
	e=int(txt3.get())
	plain_text=cy.apply_cyclic_attack(ci_text,N,e)
	lbl = Label(window, text="\n\nPlain text :		"+str(plain_text))
	lbl.pack()

def b2():
	clear_screen()
	wlcm = Label(window, text="Chosen Cipher-text Attack Program\n")
	wlcm.pack() 

	ctext = Label(window, text="Enter Cipher Text:")
	ctext.pack()
	global txt1
	txt1 = Entry(window,width=20)
	txt1.pack()

	Nval = Label(window, text="P:")
	Nval.pack()
	global txt2
	txt2 = Entry(window,width=20)
	txt2.pack()

	Eval = Label(window, text="Q:")
	Eval.pack()
	global txt3
	txt3 = Entry(window,width=20)
	txt3.pack()

	Eval = Label(window, text="e:")
	Eval.pack()
	global txt4
	txt4 = Entry(window,width=20)
	txt4.pack()

	Eval = Label(window, text="r:")
	Eval.pack()
	global txt5
	txt5 = Entry(window,width=20)
	txt5.pack()

	space_lbl = Label(window, text="\n")
	space_lbl.pack()

	ptextb = Button(window, text="Get Plain Text", command=b2c1) 
	ptextb.pack()

def b2c1():

	ci_text=txt1.get()
	P=int(txt2.get())
	Q=int(txt3.get())
	e=int(txt4.get())
	r=int(txt5.get())
	window.geometry('350x600')
	chci.apply_attack(ci_text,P,Q,e,r,window)

def b3():
	clear_screen()
	wlcm = Label(window, text="Blinding Attack Program\n")
	wlcm.pack() 

	ctext = Label(window, text="Enter the Message:")
	ctext.pack()
	global txt1
	txt1 = Entry(window,width=20)
	txt1.pack()

	Nval = Label(window, text="P:")
	Nval.pack()
	global txt2
	txt2 = Entry(window,width=20)
	txt2.pack()

	Eval = Label(window, text="Q:")
	Eval.pack()
	global txt3
	txt3 = Entry(window,width=20)
	txt3.pack()

	Eval = Label(window, text="e:")
	Eval.pack()
	global txt4
	txt4 = Entry(window,width=20)
	txt4.pack()

	Eval = Label(window, text="r:")
	Eval.pack()
	global txt5
	txt5 = Entry(window,width=20)
	txt5.pack()

	space_lbl = Label(window, text="\n")
	space_lbl.pack()

	ptextb = Button(window, text="Get Signature", command=b3c1) 
	ptextb.pack()

def b3c1():

	ci_text=txt1.get()
	P=int(txt2.get())
	Q=int(txt3.get())
	e=int(txt4.get())
	r=int(txt5.get())
	window.geometry('350x600')
	blind.apply_attack(ci_text,P,Q,e,r,window)

def clear_screen():
	lbl1.destroy()
	btn_1.destroy()
	btn_2.destroy()
	btn_3.destroy()

window = Tk()	 
window.title("IT-352 Assignment 10")
 
window.geometry('350x400')

lbl1 = Label(window, text="Choose a program..!\n\n")
lbl1.pack()

#cyclic attack button
btn_1 = Button(window, text="Cyclic Attack", command=b1) 
btn_1.pack()

#Chosen Cipher Text button
btn_2 = Button(window, text="Chosen Cipher Text Attack", command=b2) 
btn_2.pack()

#Blind Signature Attack button
btn_3 = Button(window, text="Blind Signature Attack", command=b3) 
btn_3.pack()



window.mainloop()


#Cyclic Attack, Chosen Cipher Text and Blind Signature Attack

# lbl1 = Label(window, text="Plain Text")
# lbl1.grid(column=0, row=0)
# txt1 = Entry(window,width=10)
# txt1.grid(column=1, row=0)

# lbl2 = Label(window, text="Key")
# lbl2.grid(column=0, row=1)
# txt2 = Entry(window,width=10)
# txt2.grid(column=1, row=1)

# #Blind Signature Attack button
# 	btn_3 = Button(window, text="Blind Signature Attack", command=clicked_blind_attack) 
# 	#btn_1.grid(column=2, row=3)
# 	btn_3.pack()

# space_lbl = Label(window, text="\n")
# 	space_lbl.pack()

# class cyclic:
# 	def __init__(self):
# 		self.ctext=None
# 		self.N=None
# 		self.e=None
# 	def get_plain(self):
# 		lbl = Label(window, text=self.ctext)
# 		lbl.pack()
# 		pass