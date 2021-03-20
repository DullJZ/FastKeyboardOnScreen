import PyHook3 as pyHook
import pythoncom, os
import subprocess

Upper_left = 0
(x, y) = (0, 0)


def onMouseEvent(event):
    global x, y, Upper_left
    (x, y) = event.Position
    if x <= 5 and y <= 10:
        Upper_left += 1
        run(Upper_left)
    return True


def run(Upper_left):
    if Upper_left >= 5:  #左上角
        Upper_left = 0
        subprocess.Popen('屏幕键盘.exe')


def main():
    hm = pyHook.HookManager()
    hm.MouseAllButtonsDown = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()