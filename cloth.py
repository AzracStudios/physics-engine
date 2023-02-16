import random

from engine.utils import Point, Stick
from engine.engine import Engine


def cloth(args, sim):
    size, dist = args

    points = []
    ## POINTS IN A GRID ##
    for i in range(size):
        points.append([])
        for j in range(size):

            x = i * dist + dist / 2
            y = j * dist + dist / 2

            new_point = Point(x, y, [x, x * random.random() * 0.1
                                     ][random.randrange(0, 1)],
                              [y, y * random.random() * 0.1
                               ][random.randrange(0, 1)])

            points[i].append(new_point)

    for y, row in enumerate(points):
        for x, point in enumerate(row):
            ## PIN EVERY FOURTH POINT IN THE TOP ROW ##
            if x == 0:
                if y % 4 == 0 or y == len(row) - 1:
                    point.fixed = True

            ## CONNECT POINT TO ITS NEIGHBOURS ##
            neighbours = []
            pos = (y, x)

            if pos[0] + 1 < size:
                neighbours.append(points[pos[0] + 1][pos[1]])

            if pos[0] - 1 >= 0:
                neighbours.append(points[pos[0] - 1][pos[1]])

            if pos[1] + 1 < size:
                neighbours.append(points[pos[0]][pos[1] + 1])

            if pos[1] - 1 >= 0:
                neighbours.append(points[pos[0]][pos[1] - 1])

            for neighbour in neighbours:
                if point not in sim.points:
                    sim.points.append(point)
                if neighbour not in sim.points:
                    sim.points.append(neighbour)

                new_stick = Stick(point, neighbour)

                if new_stick not in sim.sticks:
                    sim.sticks.append(new_stick)


engine = Engine(setup_func=cloth, setup_func_args=(10, 50))
engine.run()