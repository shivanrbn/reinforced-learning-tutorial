import numpy as np
import gym

window_width, window_height = 1000, 500
rotation_max, acceleration_max = 0.08, 0.5


class CustomEnv(gym.Env):

    def __init__(self, env_config={}):
        # self.observation_space = gym.spaces.Box()
        # self.action_space = gym.spaces.Box()
        self.x = window_width/2
        self.y = window_height/2
        self.ang = 0.
        self.vel_x = 0.
        self.vel_y = 0.

    def reset(self):
        # reset the environment to initial state
        return observation

    def step(self, action):
        # perform one step in the game logic
        # ========================= Applying rotation =========================
        self.ang += rotation_max * action[1]
        if self.ang > np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < -np.pi:
            self.ang += 2 * np.pi
        
        # ========================= Applying acceleration =========================
        acceleration = action[0]
        if acceleration < 0:
            acceleration *= 0.5
        self.vel_x = self.vel_x + acceleration_max * acceleration * np.cos(self.ang)
        self.vel_y = self.vel_y - acceleration_max * acceleration * np.sin(self.ang)

        # moving the rocket
        self.x += self.vel_x
        self.y += self.vel_y

        # keep rocket on screen (optional)
        if self.x > window_width:
            self.x = self.x - window_width
        elif self.x < 0:
            self.x = self.x + window_width
        if self.y > window_height:
            self.y = self.y - window_height
        elif self.y < 0:
            self.y = self.y + window_height

        observation, reward, done, info = 0., 0., False, {}
        return observation, reward, done, info
