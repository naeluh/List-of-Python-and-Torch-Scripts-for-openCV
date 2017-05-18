import gphoto2 as gp
from datetime import datetime
from Tkinter import *
from random import *
context = gp.Context()
camera = gp.Camera()
camera.init(context)
text = camera.get_summary(context)
root=Tk()
def space(event=None):
    print('Summary')
    print('=======')
    print(str(text))
    camera.exit(context)
root.bind("<space>", space)
root.mainloop()
