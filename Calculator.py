"""
Calculator
"""

from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="white")
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
        Entry(self, relief=FLAT, textvariable=display, justify='right', bd=4, bg="grey").pack(side=TOP, expand=YES, fill=BOTH)


        for clearBut in(["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))
        
        for nambutton in("789/", "456*", "123-", "0.+"):
            functionNam = iCalc(self, TOP)
            for char in nambutton:
                button(functionNam, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))


        EqualButton = iCalc(self, TOP)            
        for enterBut in "=":
            if enterBut == '=':
                btniEquals = button(EqualButton, LEFT, enterBut)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualButton, LEFT, enterBut, lambda storeObj=display, s=' %s '%enterBut: storeObj.set(storeObj.get()+s))



            #functionEnter = iCalc(self, TOP)
            #for echar in enterBut:
            #    button(functionEnter, LEFT, echar, lambda storeObj=display, q=ichar: storeObj.set(''))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
        


if __name__ =='__main__':
    app().mainloop()
