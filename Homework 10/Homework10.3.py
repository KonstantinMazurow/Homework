from tkinter import *


class Phonebook:

    def __init__(self, master, func):
        self.lab1 = Label(master, text='Name')
        self.entry1 = Entry(master, width=60)
        self.lab2 = Label(master, text='Phone')
        self.entry2 = Entry(master, width=60)
        self.but = Button(master, text='Add to Phonebook')
        self.but['command'] = getattr(self, func)
        self.lab1.pack()
        self.entry1.pack()
        self.lab2.pack()
        self.entry2.pack()
        self.but.pack()
        self.list_phones = Text(master, height = 28, width = 40)
        self.list_phones.pack()

    def add_to_phonebook(self):
        name = self.entry1.get()
        number = self.entry2.get()
        self.list_phones.insert(END, name + "\t"+ number + "\n")


if __name__ == '__main__':
    root = Tk()
    root.title('Phonebook')
    root.geometry("400x600")
    phbook1 = Phonebook(root, 'add_to_phonebook')
    root.mainloop()
