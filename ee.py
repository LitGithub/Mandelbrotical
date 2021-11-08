#Mandelbrot Set Program
#Graphs the Mandelbrot set iteratively (function is NOT recursive)
#Written by Dr. Mo, Fall 2019
import pygame
import math
import cmath
import threading
import datetime
import math
import colorsys
exit = False
pygame.init()  
pygame.display.set_caption("mandelbrot")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))

#mandelbrot function definition------------------------ 
def mandelbrot(c):
    z = complex(0,0);
    count = 0;
    while abs(z) < 2 and count < 80: 
        z = z * z + c;
        count+=0.5;
    return count;
#end mandelbrot function--------------------------------

def rainbow(num):
    h1 = colorsys.hsv_to_rgb(((num / 360)), 1, 1)
    (r, g, b) = h1
    r*=255
    g*=255
    b*=255
    r = round(r)
    g = round(g)
    b = round(b)
    return (r, g, b)

#-------------------------------------------------------
#in C++, this would be the start of main----------------
def run():
    t = -2 #lower bound for real axis
    
    while t<2: #upper bound for real (horizontal) axis
        event=pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
        t+=.005 #make this number SMALLER to increase picture resolution
    
        m = -2 #lower bound for imaginary axis
        while m<2: #upper bound for imaginary (vertical) axis
            m+=.005 #make this number SMALLER to increase picture resolution
        
            c = complex(t, m) #create a complex number from iterators
            num = mandelbrot(c); #call the function
            x = int(t * 700 + 900)
            y = int(m * 700 + 900)
            if x > 0 and x < 800 and y > 0 and y < 800:
                #these if statements are just to differentiate the colors more, not needed if you want black & white image
                screen.set_at((x, y), rainbow(num % 360 * 1/8 * 420))
                #screen.set_at((x,y),(255,0,0))
                pygame.display.flip()#this actually puts the pixel on the screen

t1=threading.Thread(target=run)
t2=threading.Thread(target=run)
t3=threading.Thread(target=run)
t4=threading.Thread(target=run)

t1.start()
t2.start()
t3.start()
t4.start()
#pygame.time.wait(10000)#pause to see the picture
#quit pygame
