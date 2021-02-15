import pygame
import time
import random


pygame.init()

#dimensions
dis_width = 800
dis_height = 600

disp=pygame.display.set_mode((dis_width,dis_height),0,32)
pygame.display.update()
game_over= False

#colors
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)

#initial position
x1 = dis_width/2
y1 = dis_height/2

#size of snake
snake_block=10
snake_speed = 30


#direction changes
x_change = 0
y_change = 0

#initialising the clock time
clock = pygame.time.Clock()


#font 
font_style = pygame.font.SysFont(None, 50)

def message (msg, color):
  message = font_style.render(msg, True, color)
  disp.blit(message, [dis_width/2, dis_height/2])



while not game_over:
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT: #when you clicking to the cross
      game_over=True
    if event.type == pygame.KEYDOWN:
      if event.key==pygame.K_UP:
        x_change = 0
        y_change = -snake_block
        print("up")
      if event.key==pygame.K_DOWN:
        x_change = 0
        y_change = snake_block
        print("down")
      if event.key==pygame.K_LEFT:
        x_change = -snake_block
        y_change = 0
        print("left")
      if event.key==pygame.K_RIGHT:
        x_change = snake_block
        y_change = 0
        print("right")
    #print(event)
  if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
    game_over = True
  x1 += x_change  
  y1 += y_change
  disp.fill(black)
  pygame.draw.rect(disp, blue, (x1, y1, snake_block, snake_block))
  pygame.display.update()
  clock.tick(snake_speed)
message("Il a cané l'animal", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()