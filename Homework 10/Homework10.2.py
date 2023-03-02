from tkinter import *


class Counter:
    def __init__(self, master, func):
        self.entry1 = Entry(master, width=60)
        self.but = Button(master, text='Count, how many words contain "e"')
        self.lab = Label(master, width=20, bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.entry1.pack()
        self.but.pack()
        self.lab.pack()

    def get_count(self):
        a = self.entry1.get()
        count = 0
        for i in a.split():
            if i.find("e") != -1 or i.find("е") != -1:
                count += 1
        self.lab['text'] = ' '.join(str(count))


if __name__ == '__main__':
    root = Tk()
    count = Counter(root, 'get_count')
    root.mainloop()
