import pygame
from engine.utils import Point, Stick

pygame.init()
pygame.font.init()
pygame.display.set_caption("Verlet Integeration Simulation")


class Config:
    WIN_WIDTH = 992
    WIN_HEIGHT = 558

    WIN_BG = (62, 107, 179)

    NORMAL_POINT_COLOR = (255, 237, 237)
    FIXED_POINT_COLOR = (230, 103, 103)
    STICK_COLOR = (255, 237, 237)

    POINT_RADIUS = 5
    POINT_WIDTH = 0
    STICK_WIDTH = 2

    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    FPS = 20

    CORRECTION_ITTR = 3
