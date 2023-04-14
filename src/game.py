import pygame
import numpy as np

from src.input import InputControls
from src.environment import CustomEnv


class Game:

    def __init__(
        self,
        window_width: int = 1000,
        window_height: int = 500,
        fps: int = 30
    ):
        pygame.init()

        # set window
        self.window = pygame.display.set_mode((window_width, window_height))

        # set clock and fps
        self.clock = pygame.time.Clock()
        self.fps = fps

        # add controls/keyboard events
        self.controls = InputControls()

        # initialize environemnt
        self.environment = CustomEnv()

    def run(self):
        # end while-loop when window is closed
        while game.__get_event():
            # ─── CONTROLS ────────────────────────────────────
            # get pressed keys, generate action
            self.clock.tick(self.fps)
            get_pressed = pygame.key.get_pressed()
            action = game.controls.pressed_to_action(get_pressed)
            # calculate one step
            self.environment.step(action)
            # render current state
            self.__render()
        pygame.quit()

    def __get_event(self):
        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                return False
        return True

    def __render(self):
        self.window.fill((0, 0, 0))
        pygame.draw.circle(self.window, (0, 200, 200), (int(self.environment.x), int(self.environment.y)), 6)
        # draw orientation
        p1 = (self.environment.x - 10 * np.cos(self.environment.ang), self.environment.y + 10 * np.sin(self.environment.ang))
        p2 = (self.environment.x + 15 * np.cos(self.environment.ang), self.environment.y - 15 * np.sin(self.environment.ang))
        pygame.draw.line(self.window, (0, 100, 100), p1, p2, 2)
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
