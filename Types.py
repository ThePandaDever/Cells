import pygame as pg

class Scene:
    organisms: list
    def __init__(self):
        self.organisms = []

class Context:
    screen: pg.Surface
    scene: Scene
    screen_size: tuple
    screen_ratioa: float
    screen_ratiob: float
    deltatime: float
    def __init__(self,screen):
        self.screen = screen
        self.scene = Scene()
        self.screen_size = self.screen.get_size()
        self.screen_ratioa = self.screen_size[0]/self.screen_size[1]
        self.screen_ratiob = self.screen_size[1]/self.screen_size[0]
        self.deltatime = 0
    def update(self):
        self.screen_size = self.screen.get_size()
        self.screen_ratioa = self.screen_size[0]/self.screen_size[1]
        self.screen_ratiob = self.screen_size[1]/self.screen_size[0]