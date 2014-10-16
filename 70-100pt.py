##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=500,height=500, background='white')
drawpad.grid(row=0, column=1)
#Square house foundation
square = drawpad.create_rectangle(100,300,300,500, fill='red')
#roof
line = drawpad.create_line(100, 300, 200, 200)
line = drawpad.create_line(200, 200, 300, 300)
#both windows
square = drawpad.create_rectangle(120,320,180,380, fill='white')
square = drawpad.create_rectangle(220,320,280,380, fill='white')
#door
square = drawpad.create_rectangle(170,420,230,500, fill='white')
#doorhandle
oval = drawpad.create_oval(225, 450, 210, 465, fill='black')
#grass
square = drawpad.create_rectangle(0,500,500,497, fill='green')
#chimney
square = drawpad.create_rectangle(120,240,160,300, fill='red')
root.mainloop()