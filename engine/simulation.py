from engine.config import *


class Simulation:

    def __init__(self):
        self.points = []
        self.sticks = []
        self.bounce_force = 0.9
        self.gravity = 0.5
        self.friction = 0.999

    def update_points(self):
        for point in self.points:
            if not point.fixed:
                vx = (point.x - point.old_x) * self.friction
                vy = (point.y - point.old_y) * self.friction

                point.old_x = point.x
                point.old_y = point.y

                point.x += vx
                point.y += vy + self.gravity

            if point.x > Config.WIN_WIDTH:
                point.x = Config.WIN_WIDTH
                point.old_x = point.x + vx * self.bounce_force

            if point.x < 0:
                point.x = 0
                point.old_x = point.x + vx * self.bounce_force

            if point.y > Config.WIN_HEIGHT:
                point.y = Config.WIN_HEIGHT
                point.old_y = point.y + vy * self.bounce_force

            if point.y < 0:
                point.y = 0
                point.old_y = point.y + vy * self.bounce_force

    def constrain_points(self):
        for point in self.points:
            if not point.fixed:
                vx = (point.x - point.old_x) * self.friction
                vy = (point.y - point.old_y) * self.friction

                if point.x > Config.WIN_WIDTH:
                    point.x = Config.WIN_WIDTH
                    point.old_x = point.x + vx * self.bounce_force

                if point.x < 0:
                    point.x = 0
                    point.old_x = point.x + vx * self.bounce_force

                if point.y > Config.WIN_HEIGHT:
                    point.y = Config.WIN_HEIGHT
                    point.old_y = point.y + vy * self.bounce_force

                if point.y < 0:
                    point.y = 0
                    point.old_y = point.y + vy * self.bounce_force

    def update_sticks(self):
        for stick in self.sticks:
            dx = stick.p1.x - stick.p0.x
            dy = stick.p1.y - stick.p0.y
            distance = (dx**2 + dy**2)**0.5
            difference = stick.length - distance
            percentage = percentage = difference / distance / 2

            if stick.p0.fixed or stick.p1.fixed:
                percentage *= 2

            offset_x = dx * percentage
            offset_y = dy * percentage

            if not stick.p0.fixed:
                stick.p0.x -= offset_x
                stick.p0.y -= offset_y

            if not stick.p1.fixed:
                stick.p1.x += offset_x
                stick.p1.y += offset_y

    def render_sticks(self):
        for stick in self.sticks:
            stick_rect = pygame.draw.line(Config.SCREEN, Config.STICK_COLOR,
                                          (stick.p0.x - Config.POINT_RADIUS,
                                           stick.p0.y - Config.POINT_RADIUS),
                                          (stick.p1.x - Config.POINT_RADIUS,
                                           stick.p1.y - Config.POINT_RADIUS),
                                          Config.STICK_WIDTH)
            stick.rect = stick_rect

    def render_points(self):
        for point in self.points:
            point_rect = pygame.draw.circle(
                Config.SCREEN, Config.NORMAL_POINT_COLOR
                if not point.fixed else Config.FIXED_POINT_COLOR,
                (point.x - Config.POINT_RADIUS, point.y - Config.POINT_RADIUS),
                Config.POINT_RADIUS, Config.POINT_WIDTH)

            point.rect = point_rect
