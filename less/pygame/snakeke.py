 import pygame
 from pygame import *
 pygame.init()

 done = False
 done2 = False

 ref = image.load('ready.png')
 loose = image.load('loose.png')
 cntnu = image.load('continue.png')
 goon = 0
 screen = display.set_mode((700, 500))
 display.set_caption('Maze Game')
 event.set_grab(1)

 while done == False:
     screen.blit(ref, (0, 0))
     display.update()
     done2 = False

     for e in event.get():
         if e.type == KEYUP:
            if e.key == K_ESCAPE:
                 done = True
         if screen.get_at((mouse.get_pos())) == (0, 0, 0):
             ref = image.load('map.png')
             done2 = True
         if screen.get_at((mouse.get_pos())) == (1, 0, 0):
             screen.blit(loose, (0, 0))
             display.update()
             done2 = True
             time.wait(2000)
             done = True
         if screen.get_at((mouse.get_pos())) == (0, 255, 0):
             screen.blit(cntnu, (0, 0))
             display.update()
             time.wait(3000)
 pygame.quit()