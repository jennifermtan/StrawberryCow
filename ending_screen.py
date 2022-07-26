import sys
import pygame
import os

def ending_screen(screen, config, score, highest_score):
    bg_image = pygame.image.load(os.path.join("images", "background.jpg")) #Background image
    font_big = pygame.font.Font(config.FONT, 60) 
    font_small = pygame.font.Font(config.FONT, 40)
    title = font_big.render(f"Time is up!", True, (0, 0, 0))
    
    title_rect = title.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.centery = screen.get_rect().centery - 100
    text_score = font_small.render(f"Score: {score}, Highest Score: {highest_score}", True, (0, 0, 0))
    
    text_score_rect = text_score.get_rect()
    text_score_rect.centerx = screen.get_rect().centerx
    text_score_rect.centery = screen.get_rect().centery
    
    while True:
        screen.blit(bg_image, (0, 0)) #Draw the background image
        for event in pygame.event.get(): #Ends the game if user exits
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #Draw the text on the screen
        screen.blit(title, title_rect)
        screen.blit(text_score, text_score_rect)

        pygame.display.flip()
