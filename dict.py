import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox

data = json.load(open("data.json"))

def translate(word):

	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]

	elif len(get_close_matches(word, data.keys())) > 0:
		decide = messagebox.askquestion('Not Found', "did you mean {} instead".format(get_close_matches(word, data.keys())[0]))
		if decide == "yes":
			e1.delete("0",END)
			e1.insert("0",get_close_matches(word, data.keys())[0])
			return data[get_close_matches(word, data.keys())[0]]
		else:
			return word + " not found"
	else:
		return word + " not found"

def show_mng(event = None):
	e2.delete('1.0', END)
	word = e1.get()
	meaning = translate(word)
	if type(meaning) == list:
		for each in meaning:
			e2.insert(END,each)
	else:
		e2.insert(END,meaning)


win = Tk()

win.configure(bg='thistle1')
win.geometry("410x250")

win.title("Dictionary")

l1 = Label(win, text = "Enter word",font = ('calibri', 12), background = "thistle1")
l1.grid(row = 1, column = 0, sticky = W)

l2 = Label(win, text = "Meaning",font = ('calibri', 12), background = "thistle1")
l2.grid(row = 2, column = 0,sticky = W)


e1 = Entry(win,width = 33)
e1.grid(row = 1, column = 2, sticky = W)
e2 = Text(win, height = 10, width=40)
e2.grid(row = 2, column = 2, sticky=W)

b2 = Button(win, text='Show', command = show_mng )
b2.grid(row=3, column=0, sticky = W)

b1 = Button(win, text='Quit', command = win.destroy)
b1.grid(row=3, column=2,sticky = W)

win.bind('<Return>', show_mng)

win.mainloop()