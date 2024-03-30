# import random
# import time
# from configparser import ConfigParser
# from initinterception import interception, move_to, move_relative, left_click, keydown, keyup, sleep
from action import Action









class Teleport(Action):

    def __init__(self):
        super().__init__()
        self.offsety=10
        self.offsetx=10

    def define(self):
        pass
    
    