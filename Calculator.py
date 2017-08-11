"""
Calculator
"""

from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="red")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RAISED, textvariable=display, justify='right', bd=3, bg="blue").pack(side=TOP, expand=YES, fill=BOTH)


        for clearBut in(["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))
        
        for nambutton in("789/", "456*", "123-", "0.+"):
            functionNam = iCalc(self, TOP)
            for char in nambutton:
                button(functionNam, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))

        for enterBut in(["="]):
            functionEnter = iCalc(self, TOP)
            for echar in enterBut:
                button(functionEnter, LEFT, echar, lambda storeObj=display, q=ichar: storeObj.set(''))

        


if __name__ =='__main__':
    app().mainloop()
