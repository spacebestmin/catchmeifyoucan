import pygame
import time
import random

pygame.init()  # initializes all of the imported Pygame modules

dis_width = 800
dis_height = 800

blue=(0,0,255)
yellow=(255,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green = (0, 255, 0)
dark_green = (5, 102, 8)
cobalt_blue=(0, 71, 171)
grass = (143, 179, 0)

font_style = pygame.font.SysFont("bahnscrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
snake_block = 10
snake_speed = 10


clock = pygame.time.Clock()
pygame.display.set_caption('Snake game by Helena with Edureka')
display=pygame.display.set_mode((dis_width, dis_height))
game_over = False


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, dark_green)
    display.blit(value, [0,0])


def our_snake(snake_block, snake_list, length):
    for x in snake_list:
        pygame.draw.rect(display, dark_green, [x[0], x[1], snake_block, snake_block])

        # if length % 2 == 0:
        #     pygame.draw.rect(display, dark_green, [x[0], x[1], snake_block, snake_block])
        #
        # else :
        #     pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width/4, dis_height/2])


def gameLoop():  # creating a function, set the game to the start condition
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list =[]
    length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:  # when the snake died
            display.fill(grass)
            message("The snake died! Press Q-quit or C-play Again", dark_green)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key is pygame.K_q:
                        game_over = True  # be out of the whole game while loop
                        game_close = False  # be out of current while
                    if event.key is pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type is pygame.QUIT: # QUIT when mouse hits x box on window
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if (x1 >= dis_width or x1 < 0) or (y1 >= dis_height or y1<0):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(grass)
        pygame.draw.rect(display, yellow, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                print("I bit my tail! oh no!")
                game_close = True
                # the snake should not touch its own tail
        our_snake(snake_block, snake_list, length_of_snake)
        your_score(length_of_snake - 1)
        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
# quit py program
