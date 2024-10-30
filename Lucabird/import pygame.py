import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

bird_img = pygame.Surface((40, 40))
bird_img.fill(RED)
bird_rect = bird_img.get_rect(center=(100, SCREEN_HEIGHT // 2))

bird_img = pygame.image.load("luca.png").convert_alpha()  
bird_rect = bird_img.get_rect(center=(100, SCREEN_HEIGHT // 2))

gravity = 0.25  
bird_movement = 0
jump_height = -6  

PIPE_WIDTH = 60
pipe_height = random.randint(150, 400)

pipe_list = []
pipe_spawn_time = pygame.USEREVENT
pygame.time.set_timer(pipe_spawn_time, 1200)

def create_pipe():
    pipe_height = random.randint(150, 400)
    pipe_top = pygame.Rect(SCREEN_WIDTH, pipe_height - SCREEN_HEIGHT, PIPE_WIDTH, SCREEN_HEIGHT)
    pipe_bottom = pygame.Rect(SCREEN_WIDTH, pipe_height + 150, PIPE_WIDTH, SCREEN_HEIGHT)
    return pipe_top, pipe_bottom

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, BLACK, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True  
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True  
    return False


def main_game():
    global bird_movement
    bird_movement = 0
    bird_rect.center = (100, SCREEN_HEIGHT // 2)

    pipe_list = []  
    score = 0
    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird_movement = jump_height
                if event.key == pygame.K_r and game_over:  
                    main_game()
            if event.type == pipe_spawn_time and not game_over:
                pipe_list.extend(create_pipe())

        if not game_over:
            bird_movement += gravity
            bird_rect.centery += bird_movement

          
            pipe_list = move_pipes(pipe_list)

         
            if check_collision(pipe_list):
                game_over = True

          
            pipe_list = [pipe for pipe in pipe_list if pipe.right > 0]

        screen.fill(WHITE)
        draw_pipes(pipe_list)

       
        screen.blit(bird_img, bird_rect)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main_game()
