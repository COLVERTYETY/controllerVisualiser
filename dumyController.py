import pygame as pg
from pynput import keyboard
import sys
import time
BASEWIDTH = 40

SCREENA= pg.Surface((BASEWIDTH*5,BASEWIDTH*3)) #pylint: disable=too-many-function-args
SCREENB= pg.Surface((BASEWIDTH*5,BASEWIDTH*3)) #pylint: disable=too-many-function-args
LISTA = ['z','q','s','d','v','b']
LISTB = ['z','q','s','d','v','b']
COLORA = (255,0,0)
COLORB = (0,255,0)
THELIST = [
    [LISTA,SCREENA,COLORA],
    [LISTB,SCREENB,COLORB],
]
screen = pg.display.set_mode((BASEWIDTH*10+10,BASEWIDTH*3))
pg.display.set_caption("the incredible controller display")

def actifup(screen,basecolor):
    pg.draw.rect(screen,basecolor,pg.Rect(BASEWIDTH,0,BASEWIDTH,BASEWIDTH))
def actifdown(screen,basecolor):
    pg.draw.rect(screen,basecolor,pg.Rect(BASEWIDTH,BASEWIDTH*2,BASEWIDTH,BASEWIDTH))
def actifleft(screen,basecolor):
    pg.draw.rect(screen,basecolor,pg.Rect(0,BASEWIDTH,BASEWIDTH,BASEWIDTH))
def actifright(screen,basecolor):
    pg.draw.rect(screen,basecolor,pg.Rect(BASEWIDTH*2,BASEWIDTH,BASEWIDTH,BASEWIDTH))
def actifjump(screen,basecolor):
    pg.draw.circle(screen,basecolor,((BASEWIDTH*4)+5-BASEWIDTH//2,int(BASEWIDTH*2.5)-10),BASEWIDTH//2)
def actifpunch(screen,basecolor):
    pg.draw.circle(screen,basecolor,((BASEWIDTH*4)+BASEWIDTH//2,(BASEWIDTH//2)+10),BASEWIDTH//2)

def unactifup(screen,basecolor):
    mod = 0.6
    pg.draw.rect(screen,colo(basecolor,mod),pg.Rect(BASEWIDTH,0,BASEWIDTH,BASEWIDTH))
def unactifdown(screen,basecolor):
    mod = 0.6
    pg.draw.rect(screen,colo(basecolor,mod),pg.Rect(BASEWIDTH,BASEWIDTH*2,BASEWIDTH,BASEWIDTH))
def unactifleft(screen,basecolor):
    mod = 0.6
    pg.draw.rect(screen,colo(basecolor,mod),pg.Rect(0,BASEWIDTH,BASEWIDTH,BASEWIDTH))
def unactifright(screen,basecolor):
    mod = 0.6
    pg.draw.rect(screen,colo(basecolor,mod),pg.Rect(BASEWIDTH*2,BASEWIDTH,BASEWIDTH,BASEWIDTH))
def unactifjump(screen,basecolor):
    mod = 0.6
    pg.draw.circle(screen,colo(basecolor,mod),((BASEWIDTH*4)+5-BASEWIDTH//2,int(BASEWIDTH*2.5)-10),BASEWIDTH//2)
def unactifpunch(screen,basecolor):
    mod = 0.6
    pg.draw.circle(screen,colo(basecolor,mod),((BASEWIDTH*4)+BASEWIDTH//2,(BASEWIDTH//2)+10),BASEWIDTH//2)


def colo(basecolor, mod):
    (a,b,c) = basecolor
    return (int(a*mod),int(b*mod),int(c*mod))

def listpress(key , list , tscreenn,basecolor):
    if key == keyboard.KeyCode.from_char( list[0]) : 
        actifup(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[1]) : 
        actifleft(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[2]) : 
        actifdown(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[3]) : 
        actifright(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[4]) : 
        actifjump(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[5]) : 
        actifpunch(tscreenn,basecolor)

def listrelease(key , list , tscreenn,basecolor):
    if key == keyboard.KeyCode.from_char( list[0]) : 
        unactifup(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[1]) : 
        unactifleft(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[2]) : 
        unactifdown(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[3]) : 
        unactifright(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[4]) : 
        unactifjump(tscreenn,basecolor)
    elif key == keyboard.KeyCode.from_char( list[5]) : 
        unactifpunch(tscreenn,basecolor)

def onpress(key):
    global THELIST
    for llist in THELIST:
        listpress(key,llist[0],llist[1],llist[2])
    screen.blit(SCREENA,(0,0))
    screen.blit(SCREENB,(BASEWIDTH*5+10,0))
    pg.display.flip()
    

def onrelease(key):
    global THELIST
    for llist in THELIST:
        listrelease(key,llist[0],llist[1],llist[2])
    screen.blit(SCREENA,(0,0))
    screen.blit(SCREENB,(BASEWIDTH*5+10,0))
    pg.display.flip()

def initialize(list_of_controlsA):
    global LISTA
    LISTA = list_of_controlsA

def default():
    global LISTA , SCREENA, SCREENB
    listener = keyboard.Listener(
    on_press=onpress,
    on_release=onrelease)
    listener.start()
def runloop():
    done  = False
    global SCREENA , screen
    while not done:
        for event in pg.event.get():
                    if event.type == pg.QUIT:# pylint: disable=no-member
                            done = True
                            sys.exit()
        time.sleep(1)
default()
runloop()