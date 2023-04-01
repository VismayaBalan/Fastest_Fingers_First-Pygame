import pygame
import random

pygame.init()

# Set up the game window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Fastest Fingers First")
# Set up the font
font = pygame.font.SysFont(None, 40)

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the space shuttle image and position
shuttle_img = pygame.image.load('spaceship.png')
shuttle_width = 5
shuttle_height = 5
shuttle_x = (win_width - shuttle_width) // 2
shuttle_y = win_height - shuttle_height - 175

# Set up the enemy letters and position
enemies = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
enemy_width = 40
enemy_height = 40
enemy_x = random.randint(enemy_width, win_width - enemy_width)
enemy_y = 0
enemy_speed = 5
enemy_letter = random.choice(enemies)

# Set up the game loop
run = True
score = 0
clock = pygame.time.Clock()

def display_text(text, color, x, y):
    """Helper function to display text on the screen"""
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

while run:
    clock.tick(60)

    # Events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pressed_key = pygame.key.name(event.key).upper()
            if pressed_key == enemy_letter:
                score += 1
                if score > 5:
                    enemy_speed = 7
                if score > 10:
                    enemy_speed = 10
                enemy_x = random.randint(enemy_width, win_width - enemy_width)
                enemy_y = 0
                enemy_letter = random.choice(enemies)

    # Move the enemy letter down the screen
    enemy_y += enemy_speed

    # Check if enemy letter has reachedthe bottom of the screen
    if enemy_y > win_height:
        enemy_x = random.randint(enemy_width, win_width - enemy_width)
        enemy_y = 0
        enemy_letter = random.choice(enemies)

    # Update the screen
    win.fill(BLACK)
    win.blit(shuttle_img, (shuttle_x, shuttle_y))
    display_text(f'Score: {score}', WHITE, 10, 10)
    display_text(enemy_letter, WHITE, enemy_x, enemy_y)

    # Check for collision between shuttle and enemy letter
    shuttle_rect = pygame.Rect(shuttle_x, shuttle_y, shuttle_width, shuttle_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if shuttle_rect.colliderect(enemy_rect):
        run = False

    pygame.display.update()

# Game over display
win.fill(BLACK)
display_text('GAME OVER', WHITE, win_width//2 - 100, win_height//2 - 40)
display_text(f'FINAL SCORE: {score}', WHITE, win_width//2 - 100, win_height//2)
pygame.display.update()

# Quit the game
pygame.time.wait(2000)
pygame.quit()