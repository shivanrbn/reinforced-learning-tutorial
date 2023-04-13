import pygame

# input capture method 1: pygame.event.get
get_event = pygame.event.get()
for event in get_event:
    # input capture method 2: pygame.key.get_pressed()
    get_pressed = pygame.key.get_pressed()
    if get_pressed[273]: # upwards arrow key
        # do something
        print("Upwards pressed!")