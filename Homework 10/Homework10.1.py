from tkinter import *


class Addition:
    def __init__(self, master, func):
        self.entry1 = Entry(master, width=20)
        self.entry2 = Entry(master, width=20)
        self.but = Button(master, text="Sum")
        self.lab = Label(master, width=20, bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.entry1.pack()
        self.entry2.pack()
        self.but.pack()
        self.lab.pack()

    def get_sum(self):
        a = int(self.entry1.get())
        b = int(self.entry2.get())
        sum = a + b
        self.lab['text'] = ' '.join(str(sum))


if __name__ == '__main__':
    root = Tk()
    addition = Addition(root, 'get_sum')
    root.mainloop()
