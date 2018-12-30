##try:
##    from ctypes import windll
##    global io
##    io = windll.dlportio # requires dlportio.dll !!!
##    print 'Parallel port open'
##except:
##    print 'The parallel port couldn\'t be opened'
from random import randint
import random
import pygame.image
import pygame.display
from pygame.locals import *
import time
import os
##from psychopy import parallel
##try:
##    global port
##    port = parallel.ParallelPort(address=0x0000D100)
##    print 'Parallel port opened'
##except:
##    print 'Parallel port not opened'




#---------parameters--------change as per the requirement
#TOTALIMAGES = 100           #number of images to search from
PATH = 'E:\\ENGINEERING\\MTech\\Sem2\\miniProject\\ERP_images\\'
FOLDERS = ("animals","cars")# a tuple of folders
IMAGEDURATION = 0.9         #300ms
BLANKSCREENPATH = "E:\\ENGINEERING\\MTech\\Sem2\\miniProject\\ERP_images\\blankScreen.jpg" # path of blank black image
MAXBLNKSCRDUR = 2           # blank screen duration (from 1 to this value)
TOTALRUN = 19               # total number of images to show
numberOfImages = {}
#----------------------------------------------------------------------------
for f in FOLDERS:
    numberOfImages[f] = len(os.listdir(PATH+f))

#--------------function to display image
def displayImage(imagePath,resolution):
    image = pygame.image.load(imagePath)
    surface = pygame.display.get_surface()
    image = pygame.transform.scale(image,resolution)
    surface.blit(image,(0,0))
    pygame.display.flip()    
#----------------------------------------------------------------------------


#--------------function to send trigger
def sendTrigger(triggerValue):
    windll.inpout32.Out32(0x0000D100, triggerValue)
    print ('Trigger sent ' + str(triggerValue))
    #win.flip()
    core.wait(0.05)
    windll.inpout32.Out32(0x0000D100, 0)
##    port.setData(triggerValue)
##    wait(0.04)
##    port.setData(0)
##    print("Trigger sent: "+FOLDERS[triggerValue])
#---------------------------------------------------------------------------


#--------------main function----------------------------------------------------
def main():
    os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'      #position the window to the center of screen
    pygame.init()
    #---set screen resolution--------
    pygame.display.init()
    RESOLUTION = (pygame.display.Info().current_w,pygame.display.Info().current_h)
    pygame.display.set_mode(RESOLUTION,FULLSCREEN)
    surface = pygame.display.get_surface()
    #--------------------------------
    font = pygame.font.SysFont("monospace", 36)
    text = font.render("Press any key to START....(ESC to exit)", 1, (10, 255, 10))
    textPos = text.get_rect()
    textPos.center = surface.get_rect().center
    surface.blit(text, textPos)
    pygame.display.flip()
    #---wait for user to start-------
    stayHere = True
    while stayHere:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                return
            elif event.type == KEYDOWN:
                stayHere = False
    #--------------------------------
    for i in range(0,TOTALRUN):
        folderNumber = randint(0,len(FOLDERS)-1)
        imageNumber = randint(1,numberOfImages[FOLDERS[folderNumber]])
        newPicPath = PATH+FOLDERS[folderNumber]+'\\'+FOLDERS[folderNumber]+'('+str(imageNumber)+').jpg'
        blankScreenDuration = random.randrange(1,MAXBLNKSCRDUR)     #generate random floating point number from para1 to para2

        displayImage(newPicPath,RESOLUTION)
        #sendTrigger(folderNumber)
        time.sleep(IMAGEDURATION)
        displayImage(BLANKSCREENPATH,RESOLUTION)                   #display blank screen
        time.sleep(blankScreenDuration)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                return
    pygame.display.quit()
    return
#----------------------------------------------------------------------------
main()




#port.setData(4)
#port.readPin(2)
#port.setPin(2, 1)


##try:
##        from ctypes import windll
##        global io
##        io = windll.dlportio # requires dlportio.dll !!!
##        print 'Parallel port open'
##except:
##        print 'The parallel port couldn\'t be opened'
##
##def trigger(n):
##    #global io
##    #trigger = n
##    #global port = 0x0000D100
##    try:
##                    #io.DlPortWritePortUchar(port, trigger)
##        windll.inpout32.Out32(0x0000D100, n)
##        print ('Trigger sent ' + str(n))
##        #win.flip()
##        core.wait(0.05)
##        windll.inpout32.Out32(0x0000D100, 0)
##        #core.wait(0.05)
##    except:
##        print 'No Trigger'
##
##
##if aTrial['type'] == 'face':
##        marker = 1
##        trigger(1)
##    elif aTrial['type'] == 'object':
##        marker = 2
##        trigger(2)
##    else:
##        marker = 0
