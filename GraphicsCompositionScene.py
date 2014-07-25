# Assignment #3 - Drawing a Scene using Functional Decomposition
# Sean Bucholtz (Section 3)
# 4/24/13

import Gui3

CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Creates single Mouse
def mouse(base_x, base_y, height):
    # Head
    head_x = base_x + height/7
    head_y = base_y + height*4/7
    head_radius = height*1.5/7
    # Nose
    nose_x = base_x + height/7
    nose_y = base_y + height*3.75/7
    nose_radius = height*.35/7
    # Mouth
    mouth_x1 = nose_x - height*.5/7
    mouth_y1 = nose_y - height*.3/7
    mouth_x2 = nose_x + height*.5/7
    mouth_y2 = nose_y - height*1/7
    # Wiskers
    wisk1_x1 = nose_x
    wisk1_y1 = nose_y
    wisk1_x2 = base_x + height*3/7
    wisk1_y2 = base_y + height*4.5/7
    wisk2_x1 = nose_x
    wisk2_y1 = nose_y
    wisk2_x2 = base_x + height*3/7
    wisk2_y2 = base_y + height*4/7
    wisk3_x1 = nose_x
    wisk3_y1 = nose_y
    wisk3_x2 = base_x + height*3/7
    wisk3_y2 = base_y + height*3.5/7
    wisk4_x1 = nose_x
    wisk4_y1 = nose_y
    wisk4_x2 = base_x - height/7
    wisk4_y2 = base_y + height*4.5/7
    wisk5_x1 = nose_x
    wisk5_y1 = nose_y
    wisk5_x2 = base_x - height/7
    wisk5_y2 = base_y + height*4/7
    wisk6_x1 = nose_x
    wisk6_y1 = nose_y
    wisk6_x2 = base_x - height/7
    wisk6_y2 = base_y + height*3.5/7
    # Eyes
    eye_r_x1 = nose_x - height*.5/7
    eye_r_y1 = base_y + height*4.25/7
    eye_r_x2 = nose_x - height*1.18/7
    eye_r_y2 = base_y + height*4.25/7
    eye_l_x1 = nose_x + height*.5/7
    eye_l_y1 = base_y + height*4.25/7
    eye_l_x2 = nose_x + height*1.18/7
    eye_l_y2 = base_y + height*4.25/7
    # Ears
    ear_r_x = nose_x - height*1.5/7
    ear_r_y = base_y + height*5.5/7
    inear_r_x = nose_x - height*1.5/7
    inear_r_y = base_y + height*5.5/7
    ear_l_x = nose_x + height*1.5/7
    ear_l_y = base_y + height*5.5/7
    inear_l_x = nose_x + height*1.5/7
    inear_l_y = base_y + height*5.5/7
    ear_radius = height*1/7
    inear_radius = height*.70/7
    # Body
    body_x1 = base_x + height/7
    body_y1 = base_y + height/7
    body_x2 = base_x + height*6/7
    body_y2 = base_y + height*2/3
    # Tail
    tail_x1 = base_x + height*6/7
    tail_y1 = base_y + height*3/7
    tail_x2 = base_x + height*6.5/7
    tail_y2 = base_y + height*4/7
    tail_x3 = tail_x1
    tail_y3 = tail_y1
    tail_x4 = base_x + height*6/7
    tail_y4 = base_y + height*5/7
    tail_x5 = tail_x4
    tail_y5 = tail_y4
    tail_x6 = base_x + height*13/14
    tail_y6 = base_y + height*6/7
    # Leg 1
    leg1_x1 = base_x + height*1.5/7
    leg1_y1 = base_y
    leg1_x2 = base_x + height*2/7
    leg1_y2 = base_y + height*2/7
    # leg2
    leg2_x1 = leg1_x2 + height*.5/7
    leg2_y1 = body_y1 + height/7
    leg2_x2 = leg1_x1 + height*1/7
    leg2_y2 = base_y
    # Leg 3
    leg3_x1 = base_x + height*4/7
    leg3_y1 = base_y
    leg3_x2 = base_x + height*4.125/7
    leg3_y2 = base_y + height*2/7
    # Leg 4
    leg4_x1 = base_x + height*5/7
    leg4_y1 = base_y
    leg4_x2 = leg1_x2 + height*2.5/7
    leg4_y2 = body_y1 + height*1/7
    canvas.line([[leg1_x1, leg1_y1], [leg1_x2, leg1_y2]], \
                width=3.25, fill='chocolate3' )
    canvas.line([[leg3_x1, leg3_y1], [leg3_x2, leg3_y2]], \
                width=3.25, fill='chocolate3')
    canvas.line([[tail_x1, tail_y1],[tail_x2, tail_y2], \
                 [tail_x4, tail_y4], [tail_x6, tail_y6]], \
                width=2.5, fill='chocolate3')
    canvas.oval([[body_x1, body_y1],[body_x2, body_y2]], \
                fill='khaki')
    canvas.line([[leg2_x1, leg2_y1], [leg2_x2, leg2_y2]], \
                width=3.25, fill='chocolate3')
    canvas.line([[leg4_x1, leg4_y1], [leg4_x2, leg4_y2]], \
                width=3.25, fill='chocolate3')
    canvas.circle([ear_r_x, ear_r_y], ear_radius, \
                  fill='chocolate3')
    canvas.circle([inear_r_x, inear_r_y],inear_radius, \
                  fill='pink')
    canvas.circle([ear_l_x, ear_l_y], ear_radius, \
                  fill='chocolate3')
    canvas.circle([inear_l_x, inear_l_y],inear_radius, \
                  fill='pink')
    canvas.circle([head_x, head_y], head_radius, \
                  fill='chocolate3')
    canvas.oval([[mouth_x1, mouth_y1],[mouth_x2, mouth_y2]], \
                fill='red')
    canvas.line([[wisk1_x1, wisk1_y1],[wisk1_x2, wisk1_y2]], \
                width=1, fill='black')
    canvas.line([[wisk2_x1, wisk2_y1],[wisk2_x2, wisk2_y2]], \
                width=1, fill='black')
    canvas.line([[wisk3_x1, wisk3_y1],[wisk3_x2, wisk3_y2]], \
                width=1, fill='black')
    canvas.line([[wisk4_x1, wisk4_y1],[wisk4_x2, wisk4_y2]], \
                width=1, fill='black')
    canvas.line([[wisk5_x1, wisk5_y1],[wisk5_x2, wisk5_y2]], \
                width=1, fill='black')
    canvas.line([[wisk6_x1, wisk6_y1],[wisk6_x2, wisk6_y2]], \
                width=1, fill='black')
    canvas.circle([nose_x, nose_y], nose_radius, fill='HotPink')
    canvas.line([[eye_r_x1, eye_r_y1],[eye_r_x2, eye_r_y2]],\
                width=1, fill='yellow')
    canvas.line([[eye_l_x1, eye_l_y1],[eye_l_x2, eye_l_y2]],\
                width=1, fill='yellow')

# Creates block of Cheese
def cheese(base_x, base_y, height):
    top_x1 = base_x - height*1/2
    top_y1 = base_y
    top_x2 = base_x
    top_y2 = base_y + height*5/8
    top_x3 = base_x - height
    top_y3 = base_y + height*5/8
    ls_bottom_x1 = base_x - height*1/2
    ls_bottom_y1 = base_y
    ls_bottom_x2 = base_x - height*1/2
    ls_bottom_y2 = base_y - height*5/8
    ls_bottom_x3 = base_x
    ls_bottom_y3 = base_y
    ls_top_x1 = base_x - height*1/2
    ls_top_y1 = base_y
    ls_top_x2 = base_x
    ls_top_y2 = base_y
    ls_top_x3 = base_x
    ls_top_y3 = base_y + height*5/8
    rs_bottom_x1 = base_x - height*1/2
    rs_bottom_y1 = base_y
    rs_bottom_x2 = base_x - height*1/2
    rs_bottom_y2 = base_y - height*5/8
    rs_bottom_x3 = base_x - height
    rs_bottom_y3 = base_y
    rs_top_x1 = base_x - height*1/2
    rs_top_y1 = base_y
    rs_top_x2 = base_x - height
    rs_top_y2 = base_y
    rs_top_x3 = base_x - height
    rs_top_y3 = base_y + height*5/8
    
    canvas.polygon([[top_x1, top_y1],[top_x2, top_y2],\
                     [top_x3, top_y3],], fill='yellow')
    canvas.polygon([[ls_bottom_x1, ls_bottom_y1],\
                    [ls_bottom_x2, ls_bottom_y2],\
                    [ls_bottom_x3, ls_bottom_y3],], \
                   fill='yellow')
    canvas.polygon([[ls_top_x1, ls_top_y1],\
                    [ls_top_x2, ls_top_y2],\
                    [ls_top_x3, ls_top_y3],], fill='yellow')
    canvas.polygon([[rs_bottom_x1, rs_bottom_y1],\
                    [rs_bottom_x2, rs_bottom_y2],\
                    [rs_bottom_x3, rs_bottom_y3]], \
                   fill='yellow2')
    canvas.polygon([[rs_top_x1, rs_top_y1],\
                    [rs_top_x2, rs_top_y2],\
                    [rs_top_x3, rs_top_y3]], fill='yellow2')
    canvas.line([[top_x2, top_y2],[top_x3, top_y3],\
                [rs_bottom_x3, rs_bottom_y3],\
                [ls_bottom_x2, ls_bottom_y2],\
                [ls_top_x2, ls_top_y2],[top_x2, top_y2],\
                [top_x1, top_y1],[rs_top_x3, rs_top_y3]], \
                width=3, fill='orange')
    canvas.line([[top_x1, top_y1],[rs_bottom_x2, rs_bottom_y2]],\
                width=3, fill='orange') 

# Creates Mouse Trap
def mouse_trap(base_x, base_y, height):
    wood_x1 = base_x
    wood_y1 = base_y
    wood_x2 = base_x + height
    wood_y2 = base_y + height*1/10
    spring_x1 = base_x + height*5/10
    spring_y1 = base_y + height*2/10
    spring_radius = height*1/10
    kill_bar_x1 = spring_x1
    kill_bar_y1 = spring_y1
    kill_bar_x2 = base_x + height*.5/10
    kill_bar_y2 = spring_y1
    spike_x1 = kill_bar_x2
    spike_y1 = kill_bar_y2
    spike_x2 = base_x + height*2/10
    spike_y2 = kill_bar_y2
    spike_x3 = base_x + height*1.15/10
    spike_y3 = base_y + height*4/10
    canvas.rectangle([[wood_x1, wood_y1],[wood_x2, wood_y2]],\
                     fill='brown')
    canvas.circle([spring_x1, spring_y1], spring_radius, \
                  fill='black')
    canvas.line([[kill_bar_x1, kill_bar_y1],\
                 [kill_bar_x2, kill_bar_y2]], width=4, \
                fill='black')
    canvas.polygon([[spike_x1, spike_y1],[spike_x2, spike_y2],\
                    [spike_x3, spike_y3]], fill='black')

# Creates multiple mouse traps grouped together
def traps(x, y, size):
    mouse_trap(x - size*9/10, y + size*3/10, size - size*2/10)
    mouse_trap(x,y,size)
    mouse_trap(x + size*11/10,y - size*4/10, size + size*2/10)

# Creates a group of three cheese blocks    
def cheese_buffet(x, y, size):
    cheese(x + size*7/10,y + size*6/10, size)
    cheese(x,y,size - size*1/8) #Cheese is good!
    cheese(x + size*8/10,y - size*4/10,size - size*1/4)

# Creates a family of mice    
def mouse_family(x, y, size):
    mouse(x, y + size*1/10, size*8/7) #Daddy Mouse
    mouse(x + size*7/7, y - size*3/7, size*7/7) #Mommy Mouse
    mouse(x + size*3.25/7, y - size*4/7, size*4/7) #Baby Mouse
    mouse(x + size*7.25/7, y - size*7/7, size*3.5/7) #Runt Mouse 2

def main():
    canvas.rectangle([[-320,170],[320,240]], \
                     fill='PaleTurquoise3')
    canvas.circle([275,190], 20, fill='black')
    mouse_family(-20,120,65)
    mouse_family(150,100,50)
    mouse_family(230,140,35)
    mouse_family(-185,85,90)
    mouse(-280,80, 80)
    mouse_family(0,0,100)
    mouse_family(190,-40, 75)
    cheese(-290,-5,30)
    cheese_buffet(-275,-75,50)
    cheese_buffet(-65,-145,80)
    cheese_buffet(-70,-240,60)
    cheese_buffet(-200,-150,100)
    cheese_buffet(-300,-220,50)
    mouse(25,-220, 35)
    mouse_trap(-320,40,45)
    traps(-200,0,75)
    traps(110,-150,125)

## Testing

    """The objective of this assignment was to create multiple
objects that could be abstractly reproduced anywhere in the GUI
and at any size. The values used in the main function
demonstrate that each object or group of objects can be
replicated and placed at any coordinate location and at any size with
the dimensions remaining intact."""

#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui3.Gui()
win.title('Mouse Frenzy')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html


