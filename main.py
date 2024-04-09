import pygame as g
from pygame.locals import *
import time
#this game is about filling the screen with diagonal movement only.
#requires high focus and iq
#the aim is to cover the entire background with white color in the shortest time possible
class Black:
    def __init__(self, screen_obj,x, y):
        self.black = g.image.load("resources/2416004.webp")
        self.black = g.transform.scale(self.black, (50,50))
        screen_obj.blit(self.black,(x,y))
        time.sleep(1)

class White:
    def __init__(self, screen_obj):
        self.screen_obj = screen_obj
        self.s1 = 50
        self.s2 = 50       
        self.x = 100
        self.y = 100

    def image_builder(self,x = 0, y = 0): 
        if(self.x + x > 0):
            self.s1 += x
            # self.s1 = abs(self.s1)
        if(self.s2 + y > 0):
            self.s2 += y 
            # self.s2 = abs(self.s2)
        self.white = g.image.load("resources\R.jpeg").convert()
        self.white = g.transform.scale(self.white,(self.s1,self.s2))

    def set_XY(self, x=0, y=0):
        self.x += x
        self.y += y

    def putOnScreen(self):
        # self.screen_obj.fill((250,200,156))
        self.screen_obj.blit(self.white,(self.x,self.y))

class Game:
    def __init__(self):
        g.init()
        g.display.set_caption("Diagonal Domination")
        self.screen = g.display.set_mode((920,800))
        self.screen.fill((250,200,156))#fill screen before using blit()
        self.white = White(self.screen)
        self.white.image_builder()
        self.white.putOnScreen()

    def run(self):
        running = True
        font = g.font.Font(None,25)
        start_time = time.time()
        description_msg = "Use w,s,a,d to move diagonally.\n Fill the entire area with white in the shortest time possible."
        cheat_msg = "Cheat1 - Press B to find the location of the pointer.\n"
        # cheat_msg1 = "Cheat2 - Press P to increase size of pointer and s to increase"
        clock = g.time.Clock()
        self.screen.fill((250,200,156))
        text = font.render(description_msg,False, (0,0,0))
        text1 = font.render(cheat_msg,True, (0,0,0))
        # text2 = font.render(cheat_msg1,True, (0,0,0))
        self.screen.blit(text, (100,250))
        self.screen.blit(text1, (100,500))
        # self.screen.blit(text2, (100,520))
        cheat_time = 0

        while(running):
            events = g.event.get()#list
            keys = g.key.get_pressed()
            for event in events:
                if event.type == g.QUIT or keys[g.K_ESCAPE]: running = False

            # if keys[g.K_UP] :self.white.set_XY(y=-10)
            # elif keys[g.K_DOWN] :self.white.set_XY(y=+10)
            # elif keys[g.K_LEFT] :self.white.set_XY(-10)
            # elif keys[g.K_RIGHT] :self.white.set_XY(10)
            if keys[g.K_w] :self.white.set_XY(-5,-5)
            elif keys[g.K_s] :self.white.set_XY(5,5)
            elif keys[g.K_a] :self.white.set_XY(-5,5)
            elif keys[g.K_d] :self.white.set_XY(5,-5)    
            elif keys[g.K_p] :self.white.image_builder(5,5)
            # elif keys[g.K_o] : self.white.image_builder(-5,-5)#doesn't work idk why
            time_elapsed = int(time.time() - start_time - cheat_time)
            time_info = font.render(f"Time: {time_elapsed} seconds", True,(0,0,0))
            self.screen.fill((255,255,255),(300,777,150,20))
            self.screen.blit(time_info,(300,777))
            if keys[g.K_b]:
                Black(self.screen,self.white.x, self.white.y)
                g.display.flip()#flip() puts the work on screen
                clock.tick(60)
                time.sleep(1)
                cheat_time = -2
            else:
                self.white.putOnScreen() 
                g.display.flip()#flip() puts the work on screen
                clock.tick(60)  
                cheat_time = 0  
        g.quit()
def main():
    game = Game()
    game.run()
if __name__ == "__main__": main()
