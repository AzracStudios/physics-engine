import random
from engine.config import *
from engine.simulation import Simulation


class Engine:

    def __init__(self, setup_func=None, setup_func_args=None):
        self.clock = pygame.time.Clock()
        self.start = False
        self.points_to_make_stick = []
        self.sim = Simulation()

        self.setup_func = setup_func
        self.setup_func_args = setup_func_args

    def add_point(self):
        pos = pygame.mouse.get_pos()
        pos_x = pos[0]
        pos_y = pos[1]

        new_point = Point(pos_x, pos_y, [pos_x, pos_x * random.random() * 0.1
                                         ][random.randrange(0, 1)],
                          [pos_y, pos_y * random.random() * 0.1
                           ][random.randrange(0, 1)])

        self.sim.points.append(new_point)

    def fix_point(self):
        pos = pygame.mouse.get_pos()
        clicked_stick_index = [
            p for p in self.sim.points if p.rect.collidepoint(pos)
        ]

        if clicked_stick_index:
            clicked_stick_index = clicked_stick_index[0]
            clicked_stick_index.fixed = not clicked_stick_index.fixed

    def add_stick(self):
        pos = pygame.mouse.get_pos()
        clicked_stick_index = [
            p for p in self.sim.points if p.rect.collidepoint(pos)
        ]

        if clicked_stick_index:
            clicked_stick_index = clicked_stick_index[0]
            if len(
                    self.points_to_make_stick
            ) < 2 and not clicked_stick_index in self.points_to_make_stick:
                self.points_to_make_stick.append(clicked_stick_index)

            if len(self.points_to_make_stick) == 2:
                new_stick = Stick(self.points_to_make_stick[0],
                                  self.points_to_make_stick[1])

                if not new_stick in self.sim.sticks:
                    self.sim.sticks.append(new_stick)

                self.points_to_make_stick = []

    def remove_stick(self):
        pos = pygame.mouse.get_pos()
        clicked_stick_index = [
            i for i, s in enumerate(self.sim.sticks)
            if s.rect.collidepoint(pos)
        ]

        if clicked_stick_index:
            for stick in clicked_stick_index:
                self.sim.sticks.pop(stick)

    def draw_stick_helper(self, mouse_pos):
        start = self.points_to_make_stick[0]
        pygame.draw.line(
            Config.SCREEN, Config.STICK_COLOR,
            (start.x - Config.POINT_RADIUS, start.y - Config.POINT_RADIUS),
            mouse_pos, 2)
        pygame.display.update()

    def render(self):
        Config.SCREEN.fill(Config.WIN_BG)

        self.sim.render_sticks()
        self.sim.render_points()

        pygame.display.update()

    def update(self):
        self.sim.update_points()

        for i in range(Config.CORRECTION_ITTR):
            self.sim.update_sticks()
            self.sim.constrain_points()

    def run(self):
        if self.setup_func:
            self.setup_func(self.setup_func_args, self.sim)

        while True:
            self.clock.tick(Config.FPS)

            if self.start: self.update()
            self.render()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = not self.start

                if event.type == pygame.MOUSEBUTTONDOWN and not self.start:
                    if pygame.mouse.get_pressed()[0]:
                        self.add_point()

                    if pygame.mouse.get_pressed()[1]:
                        self.fix_point()

                    if pygame.mouse.get_pressed()[2]:
                        self.add_stick()

                if len(self.points_to_make_stick) > 0:
                    self.draw_stick_helper(pygame.mouse.get_pos())

                if event.type == pygame.MOUSEMOTION and self.start:
                    if pygame.mouse.get_pressed()[0]:
                        self.remove_stick()
