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
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='brown')
drawpad.grid(row=0, column=1)
# create_oval(x,y,width,height,fill color)
oval = drawpad.create_oval(10, 50, 100, 100, fill='green')
#create_square(top left x,top left y, bottom right x, bottom right y, fill color)
square = drawpad.create_rectangle(200,200,250,250, fill='red')
#create_line(top left x,top left y, bottom right x, bottom right y, fill color)
line = drawpad.create_line(0, 0, 200, 100)
root.mainloop()