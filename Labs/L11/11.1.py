from tkinter import *
from tkinter.filedialog import Open, SaveAs

fn = None
def LoadFile():
    global fn
    fn = Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())

def SaveFile():
    global fn
    with open(fn, 'w') as file:
        file.write(textbox.get("1.0",END))

root = Tk()
panelFrame = Frame(root, height=20, bg='blue')
textFrame = Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font='Arial 12', wrap='word')

scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

Button(panelFrame, text='Open', command = LoadFile).place(x=10, y=1, width=40, height=20)  
Button(panelFrame, text='Save', command = SaveFile).place(x=55, y=1, width=40, height=20)
root.mainloop()
