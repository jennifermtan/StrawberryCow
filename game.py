import pygame
import os
import random
import sys
import config
from ending_screen import ending_screen
from food import Food
from sprite import Sprite

def main():
    #Initialising pygame
    pygame.init()
    screen = pygame.display.set_mode([config.WIDTH, config.HEIGHT])
    pygame.display.set_caption("Strawberry Cow")
    bg_image = pygame.image.load(os.path.join("images", "background.jpg"))
    font = pygame.font.Font(config.FONT, 40)
    strawberry_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "strawberry.png")), (50, 50)) #Resize the strawberry    
    rotten_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "rotten.png")), (50, 50)) #Resize the rotten strawberry

    #Scores
    score = 0
    highest_score = 0 if not os.path.exists(config.HIGHEST_SCORE_RECORD_FILEPATH) else int(open(config.HIGHEST_SCORE_RECORD_FILEPATH).read())

    #Create the sprite
    strawberry_cow = Sprite(100, 275) #Set position of the sprite
    sprite_group = pygame.sprite.RenderPlain()
    sprite_group.add(strawberry_cow)

    #Create the food
    food_freq = random.randint(15, 20)
    food_count = 0

    #Creating the strawberry object
    strawberry_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "strawberry.png")), (50, 50)) #Resize the strawberry
    strawberry = Food(100, 100, strawberry_image)
    #Creating the bad strawberry object
    rotten_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "rotten.png")), (50, 50)) #Resize the rotten strawberry
    bad_strawberry = Food(100, 100, rotten_image)

    food_group = pygame.sprite.RenderPlain()
    food_group.add(strawberry)
    food_group.add(bad_strawberry)

    #Set the timer
    clock = pygame.time.Clock()

    happy_sound = pygame.mixer.Sound(os.path.join("audios", "happy.wav"))
    bg_sound = pygame.mixer.Sound(os.path.join("audios", "strawberrycow.wav"))

    pygame.mixer.Sound.play(bg_sound)

    while True:
        screen.blit(bg_image, (0, 0)) #Display the background

        #Set countdown on screen (15 seconds)
        timer = 15 - pygame.time.get_ticks() // 1000 % 60
        if timer <= 0:
            break

        #Set the timer and show it on the screen
        countdown_text = 'Count down: ' + str(round(timer))
        countdown_text = font.render(countdown_text, True, (0,0,0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topright = [config.WIDTH-30, 5]
        screen.blit(countdown_text, countdown_rect)
        
        #Set the score and show it on the screen
        score_text = f'Score: {score}, Highest: {highest_score}'
        score_text = font.render(score_text, True, (0,0,0))
        score_rect = score_text.get_rect()
        score_rect.topleft = [5, 5]
        screen.blit(score_text, score_rect)

        strawberry_cow.update()
        strawberry.update()
        bad_strawberry.update()

        #Player controls for left and right arrows
        for event in pygame.event.get():
            #If key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    strawberry_cow.control(8)
                if event.key == pygame.K_LEFT:
                    strawberry_cow.control(-8)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #Add another strawberry (good or bad) to the screen after one falls
        food_count += 1
        if food_count > food_freq:
            food_freq = random.randint(25, 30)
            food_count = 0
            strawberry = Food(100, 100, strawberry_image)
            bad_strawberry = Food(100, 100, rotten_image)
            food_group.add(strawberry)
            food_group.add(bad_strawberry)
    
        #Remove the strawberry if it is out of the screen
        for food in food_group:
            if food.update():
                food_group.remove(food)

        #Adding up scores and removing strawberries if player collides with a strawberry
        for food in food_group:
            if food == strawberry:
                if strawberry_cow.rect.colliderect(strawberry):
                    pygame.mixer.Sound.play(happy_sound) #Play happy sound if good strawberry collected
                    food_group.remove(strawberry)
                    score += 1 #Add a score if good strawberry is collected
                    if score > highest_score:
                        highest_score = score #Set the high score if it is more than the previous high score
            if food == bad_strawberry:
                if strawberry_cow.rect.colliderect(bad_strawberry):
                    food_group.remove(bad_strawberry)
                    score -= 1 #Add a score if good strawberry is collected
                    if score > highest_score:
                        highest_score = score 

        sprite_group.draw(screen) #Draw the sprite
        food_group.draw(screen) #Draw the food objects

        pygame.display.flip()
        clock.tick(config.FPS) #Strawberries falling according to FPS

    fp = open(config.HIGHEST_SCORE_RECORD_FILEPATH, 'w')
    fp.write(str(highest_score)) #Write the highest score in the HIGHEST_SCORE_RECORD_FILEPATH
    fp.close()
    return ending_screen(screen, config, score, highest_score) #Show ending screen

if __name__ == "__main__":
    main()

        