from threading import *
from tkinter import *
import traceback
import os, sys

sys.set_int_max_str_digits(100_000_000)
os.system('title Console For Show Words')
print("Please Don't Close This Console")
NoType = None

r = Tk()
r.geometry('300x300+0+0')
r.protocol('WM_DELETE_WINDOW', lambda: NoType)
r.title('Script code')

def ask_close_logic():
    mypy = sys.executable
    while True:
        yesno = input('Type [Y] To Close, [N] For Not Close:  ')
        yesno = yesno.lower().strip()
        if yesno == 'y' or yesno == 'yes':
            r.destroy()
            os._exit(0)
        elif yesno == 'n' or yesno == 'no':
            break
        else:
            print('just write Y or N')

brain = """\
t = Text(r, font=('Consolas', 16), bg='black', fg='lightgreen')
t.grid(row=1, column=0, columnspan=3, rowspan=6)

def close_all():
    th = Thread(target=ask_close_logic)
    th.start()

def runc():
    ck = 0
    global t
    coderun = t.get('1.0', END)
    mypy = sys.executable
    try:
        exec(coderun)
    except:
        print(traceback.format_exc())

def savef():
    global t, ck
    desktop = os.path.join(os.path.expanduser('~'), r"Desktop")
    save = t.get('1.0', END)
    while True:
        try:
            f = open(f'{desktop}{os.sep}code-cao-ky-thay-toan-de({ck}).py', 'r', encoding='utf-8')
            f.close()
        except:
            break
        else:
            ck += 1
    with open(f'{desktop}{os.sep}code-cao-ky-thay-toan-de({ck}).py', 'w', encoding='utf-8') as f:
        f.write(str(save))

caokycode = Label(r, text="SCRIPT CODE", font=('Arial', 30, 'bold'), bg='white', fg='black')
caokycode.grid(row=0, column=0, columnspan=2)

closebt = Button(r, text='close', font=('Arial', '30', 'underline'),  bg='white', fg='red', activebackground='red', activeforeground='white', command=close_all)
closebt.grid(row=7, column=0, rowspan=2)

saveme = Button(r, text='save', bg='white', fg='red', activebackground='red', activeforeground='white', font=('Arial', '30', 'underline'), command=savef)
saveme.grid(row=7, column=1, rowspan=2)

runmycode = Button(r, text='run code', bg='white', fg='red', activebackground='red', activeforeground='white', font=('Arial', '30', 'underline'), command=runc)
runmycode.grid(row=7, column=2, rowspan=2)
"""

def thread():
    global brain
    exec(brain)

ck = 0
thread()
r.mainloop()
