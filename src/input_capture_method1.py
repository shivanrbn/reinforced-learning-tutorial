import pygame

# input capture method 1: pygame.event.get
get_event = pygame.event.get()
for event in get_event:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            # do something
            print("Upwards is pressed?")
    if event.type == pygame.QUIT:
        # end loop when pygame window closed
        run = False
