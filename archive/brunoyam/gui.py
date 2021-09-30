from tkinter import Frame


class Example(Frame):
    def __init__(self, parent, send_action):
        Frame.__init__(self, parent)
        self.parent = parent
        self.action = send_action
        self.initUI()

    def foo(self):
        text = self.text_input.get(1.0, END).strip()
        # self.list.insert(END, text)
        self.action(bytes(text, 'utf-8'))
        self.text_input.delete(1.0, END)

    def initUI(self):
        self.parent.title("Hello")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1,  weight=1)
        self.rowconfigure(4, weight=1)

        self.list = Listbox(self)
        self.list.grid(row=0, column=0, columnspan=2, rowspan=2,
                   sticky=E+W+S+N)

        self.text_input = Text(self)
        self.text_input.grid(row=3, column=0)

        self.ok_button = Button(self, text='SEND', command=self.foo)
        self.ok_button.grid(row=4, column=1)

        scroll = Scrollbar(self.list, command=self.list.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.list.config(yscrollcommand=scroll.set)

    def add_input(self, value):
        self.list.insert(END, value)


def main():
    root = tk()
    root.geometry('700x700+300+300')
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()