import pyautogui
import time
import colorsys
import keyboard
import mss
import mss.tools
from PIL import Image

print('press crtl+c to quit')

pyautogui.FAILSAFE = True
#allows you to quit the program by moving the mouse to the upper left of the screen

#screenshot coordinates:
#top left: (695, 695)
#bottom right: (1225, 992)

#takes an extremely thin screenshot lol
ssTopLeft = (695, 899)
ssBottomRight = (1225, 901)

#size of picture: (530, 3)

#looks at the leftmost rectangle
#looking for black
#if there is black, it will click in the middle of that rectangle

#variables for faster addition
clickLgpx = ssTopLeft[0]+30
clickMLgpx = ssTopLeft[0]+165
clickMRgpx = ssTopLeft[0]+290
clickRgpx = ssTopLeft[0]+430
clickgpy = ssTopLeft[1]+1
clickLcx = ssTopLeft[0]+66
clickMLcx = ssTopLeft[0]+198
clickMRcx = ssTopLeft[0]+330
clickRcx = ssTopLeft[0]+462

#todo: hardcode these
def clickL(scrn):
    pixcol = scrn.getpixel((clickLgpx, clickgpy))
    pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
    if(pixcol[2] <= 5):
        #clicks the middle of the left box
        pyautogui.click(x=clickLcx, y=clickgpy, clicks=2)
        #print('detected on l, clicking...')
    #else:
        #tests another point within the left box
        #pixcol = scrn.getpixel((90, 1))
        #pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
        #if(pixcol[2] <= 5):
            #pyautogui.click(x=ssTopLeft[0]+66, y=ssTopLeft[1]+1)
            #print('detected on l, clicking...')

def clickML(scrn):
    pixcol = scrn.getpixel((clickMLgpx, clickgpy))
    pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
    if(pixcol[2] <= 5):
        pyautogui.click(x=clickMLcx, y=clickgpy, clicks=2)
        #print('detected on ml, clicking...')
    #else:
        #pixcol = scrn.getpixel((230, 1))
        #pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
        #if(pixcol[2] <= 5):
            #pyautogui.click(x=ssTopLeft[0]+198, y=ssTopLeft[1]+1)
            #print('detected on ml, clicking...')

def clickMR(scrn):
    pixcol = scrn.getpixel((clickMRgpx, clickgpy))
    pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
    if(pixcol[2] <= 5):
        pyautogui.click(x=clickMRcx, y=clickgpy, clicks=2)
        #print('detected on mr, clicking...')
    #else:
        #pixcol = scrn.getpixel((370, 1))
        #pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
        #if(pixcol[2] <= 5):
            #print('detected on mr, clicking...')
            #pyautogui.click(x=ssTopLeft[0]+330, y=ssTopLeft[1]+1)

def clickR(scrn):
    pixcol = scrn.getpixel((clickRgpx, clickgpy))
    pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
    if(pixcol[2] <= 5):
        pyautogui.click(x=clickRcx, y=clickgpy, clicks=2)
        #print('detected on r, clicking...')
    #else:
        #pixcol = scrn.getpixel((490, 1))
        #pixcol = colorsys.rgb_to_hsv(pixcol[0], pixcol[1], pixcol[2])
        #if(pixcol[2] <= 5):
            #print('detected on r, clicking...')
            #pyautogui.click(x=ssTopLeft[0]+462, y=ssTopLeft[1]+1)

try:
    #gives you three seconds to start the app
    print('3 second countdown now beginning')
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('go!')

    #iter = 0
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        while keyboard.is_pressed('c') == False:
            #scrn = pyautogui.screenshot(region=(ssTopLeft[0], ssTopLeft[1], ssBottomRight[0], ssBottomRight[1]))
            #old screenshot utility
            #grabbing mss screenshot object
            sshot = sct.grab(monitor)
            scrn = Image.frombytes("RGB", sshot.size, sshot.bgra, "raw", "BGRX")
            clickL(scrn)
            clickR(scrn)
            clickML(scrn)
            clickMR(scrn)
            #iter = iter + 1
            #print("iteration: " + str(iter))
        print('c pressed: Done')
except KeyboardInterrupt:
    print('KeyboardInterrupt: Done.')