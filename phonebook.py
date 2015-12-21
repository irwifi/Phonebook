from tkinter import Tk, Frame, BOTH

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.parent.title("Phonebook")
        self.pack(fill=BOTH, expand=1)
        self.init_window()


    def init_window(self):
        w = 480
        h = 520

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/4
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
# w = Label(root, text="Hello Tkinter!")
# w.pack()
