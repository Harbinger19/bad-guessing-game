#Importing the modules that I will be using
#Time to control how fast stuff is displayed, random to get a random number between 1 and 500, and pygame to handle the GUI
import random
import time
import pygame, sys
from pygame.color import THECOLORS
from pygame.locals import *

#Getting the random number
num = random.randrange(1, 501)
guess = ""
won = False

#Function to compare the random number and the guees
def comparing(x, y, z) :
        if y > x :
                text = font.render("Your guess was higher than the number. Please try again.", True, THECOLORS["black"], THECOLORS["ivory"])
                textRect = text.get_rect()
                textRect.center = (640, 360)                        
                
                screen.blit(text, textRect)
                pygame.display.flip()
                time.sleep(2)
                screen.fill(THECOLORS["ivory"])
                pygame.display.flip()
        elif y < x :
                text = font.render("Your guess was lower than the number. Please try again.", True, THECOLORS["black"], THECOLORS["ivory"])
                textRect = text.get_rect()
                textRect.center = (640, 360)                        
                
                screen.blit(text, textRect)
                pygame.display.flip()
                time.sleep(2)
                screen.fill(THECOLORS["ivory"])
                pygame.display.flip()
        else :
                text = font.render("You won! Good job.", True, THECOLORS["black"], THECOLORS["ivory"])
                textRect = text.get_rect()
                textRect.center = (640, 360)                        
                
                screen.blit(text, textRect)
                pygame.display.flip()
                time.sleep(1.5)
                screen.fill(THECOLORS["ivory"])
                pygame.display.flip()
                
                #Displays the star when you win
                star = pygame.image.load('Star.png')
                
                x = 0
                y = 0
                
                screen.blit(star, (x, y))
                pygame.display.flip()
                time.sleep(3)

#Setting up the pygame stuff
if 1 == 1 :
        
        pygame.init()
        
        SIZE = (1280, 720)
        screen = pygame.display.set_mode(SIZE)
        
        pygame.display.set_caption("Guess 500!")
        
        clock = pygame.time.Clock()
        events = pygame.event.get()
        
        keepGoing = True
        
        inputBox = pygame.Rect(540, 340, 200, 40)
        inputText = ""
        
        color_active = THECOLORS["azure4"]
        color_inactive = THECOLORS["black"]
        color = color_inactive
        
        active = False
        
        pygameSucks = False
        
        font = pygame.font.SysFont("Helvetica", 32)
        
        star = pygame.image.load('Star.png')
        
        screen.fill(THECOLORS["ivory"])
        
        x = 0
        y = 0
        
        #Telling the user what guess they are on, and using the function to determine what to display
        for i in range(1, 10):
                #Making sure to exit the loop if you have won
                if won == True :
                        pygame.quit()
                        sys.exit()
                guess = ""
                pygameSucks = False
                active = False
                color = color_inactive
                
                #Iterating through nine guesses
                if i == 9 :
                        text = font.render("This is your final guess.", True, THECOLORS["black"], THECOLORS["ivory"])
                        textRect = text.get_rect()
                        textRect.center = (640, 360)                        
                        
                        screen.blit(text, textRect)
                        pygame.display.flip()
                        time.sleep(2)
                        screen.fill(THECOLORS["ivory"])
                        pygame.display.flip()
                else :        
                        if  i == 1 :
                                ending = "st"
                        elif i == 2 :
                                ending = "nd"
                        elif i == 3 :
                                ending = "rd"
                        else : 
                                ending = "th"
                        text = font.render("This is your " + str(i) + ending +" guess.", True, THECOLORS["black"], THECOLORS["ivory"])
                        textRect = text.get_rect()
                        textRect.center = (640, 360)
                        
                        screen.blit(text, textRect)
                        pygame.display.flip()
                        time.sleep(2)
                        screen.fill(THECOLORS["ivory"])
                        pygame.display.flip()
                
                pygame.draw.rect(screen, color, inputBox) 
                pygame.display.flip()
                
                #I was having trouble with the event loop so I just made it run for a really long time
                for x in range(1, 10000000000) :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        #Checks if the user presses inside the box and changes the color
                                        if event.pos[0] < 740 and event.pos[0] > 540 and event.pos[1] < 380 and event.pos[1] > 340 :
                                                active = not active
                                                color = color_active if active else color_inactive
                                                pygame.draw.rect(screen, THECOLORS["black"], (535, 335, 210, 50))
                                                pygame.draw.rect(screen, color, inputBox) 
                                                pygame.display.flip()                                                
                                        else :
                                                active = False
                                        
                                        
                                #This handles taking in the keystrokes from the player
                                if event.type == pygame.KEYDOWN:
                                        if active:
                                                if event.key == pygame.K_RETURN:
                                                        pygameSucks = True
                                                        break
                                                        
                                                elif event.key == pygame.K_BACKSPACE:
                                                        guess = guess[:-1]
                                                        
                                                        screen.fill(THECOLORS["ivory"])
                                                        pygame.draw.rect(screen, THECOLORS["black"], (535, 335, 210, 50))
                                                        pygame.draw.rect(screen, color, inputBox) 
                                                        
                                                        text = font.render(guess, True, THECOLORS["black"], THECOLORS["azure4"])
                                                        textRect = text.get_rect()
                                                        textRect.center = (640, 360)                        
                                                        
                                                        screen.blit(text, textRect)
                                                        pygame.display.flip()  
                                                        
                                                else:
                                                        guess += event.unicode
                                                        text = font.render(guess, True, THECOLORS["black"], THECOLORS["azure4"])
                                                        textRect = text.get_rect()
                                                        textRect.center = (640, 360)                        
                                                        
                                                        screen.blit(text, textRect)
                                                        pygame.display.flip()                                                        
                        #Breaks the loop if you press enter/return so that we can compare guess to num                                
                        if pygameSucks :
                                break
                screen.fill(THECOLORS["ivory"])
                pygame.display.flip()
                #Comparing guess to num
                if guess.isdigit() :
                        guess = int(guess)
                        comparing(num, guess, won)
                        if guess == num :
                                won = True
                else :
                        #If you don't enter just numbers
                        text = font.render("The guess you entered was not correctly formatted.", True, THECOLORS["black"], THECOLORS["ivory"])
                        textRect = text.get_rect()
                        textRect.center = (640, 360)
                                
                        screen.blit(text, textRect)
                        pygame.display.flip()
                        time.sleep(3)
                        screen.fill(THECOLORS["ivory"])
                        pygame.display.flip()                        
        
        pygame.quit()        