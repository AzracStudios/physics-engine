import random
from engine.config import *
from engine.engine import Engine


def ragdoll(args, sim):
    x, y, dist, spin = args

    ## HEAD ##

    head = Point(x, y, x - spin, y)
    neck_1 = Point(x + dist, y + dist, x + dist, y + dist)
    neck_2 = Point(x - dist, y + dist, x - dist, y + dist)

    sim.points.append(head)
    sim.points.append(neck_1)
    sim.points.append(neck_2)

    sim.sticks.append(Stick(head, neck_1))
    sim.sticks.append(Stick(head, neck_2))
    sim.sticks.append(Stick(neck_1, neck_2))

    ## BODY ##

    rand_mult = random.randrange(3, 5)

    torso_1 = Point(x + dist // 2, y + rand_mult * dist, x + dist // 2,
                    y + rand_mult * dist)
    torso_2 = Point(x - dist // 2, y + rand_mult * dist, x - dist // 2,
                    y + rand_mult * dist)

    sim.points.append(torso_1)
    sim.points.append(torso_2)

    sim.sticks.append(Stick(neck_1, torso_1))
    sim.sticks.append(Stick(neck_2, torso_2))
    sim.sticks.append(Stick(torso_1, torso_2))
    sim.sticks.append(Stick(torso_1, neck_2))

    ## HANDS ##
    fac_a = 2
    fac_b = 3

    elbow_1 = Point(x + fac_a * dist, y + fac_a * dist, x + fac_a * dist,
                    y + fac_a * dist)
    elbow_2 = Point(x - fac_a * dist, y + fac_a * dist, x - fac_a * dist,
                    y + fac_a * dist)

    hand_1 = Point(x + fac_b * dist, y + fac_b * dist, x + fac_b * dist,
                   y + fac_b * dist)

    hand_2 = Point(x - fac_b * dist, y + fac_b * dist, x - fac_b * dist,
                   y + fac_b * dist)

    sim.points.append(elbow_1)
    sim.points.append(elbow_2)
    sim.points.append(hand_1)
    sim.points.append(hand_2)

    sim.sticks.append(Stick(neck_1, elbow_1))
    sim.sticks.append(Stick(neck_2, elbow_2))
    sim.sticks.append(Stick(elbow_1, hand_1))
    sim.sticks.append(Stick(elbow_2, hand_2))

    ## LEGS ##

    knee_1 = Point(x + dist // 2, y + rand_mult * 1.5 * dist,
                   x + dist // 2 - 5, y + rand_mult * 1.5 * dist)
    knee_2 = Point(x - dist // 2, y + rand_mult * 1.5 * dist,
                   x - dist // 2 + 5, y + rand_mult * 1.5 * dist)

    leg_1 = Point(x + dist // 2 - 5, y + rand_mult * 2 * dist, x + dist // 2,
                  y + rand_mult * 2 * dist)
    leg_2 = Point(x - dist // 2 + 5, y + rand_mult * 2 * dist, x - dist // 2,
                  y + rand_mult * 2 * dist)

    sim.points.append(knee_1)
    sim.points.append(knee_2)
    sim.points.append(leg_1)
    sim.points.append(leg_2)

    sim.sticks.append(Stick(torso_1, knee_1))
    sim.sticks.append(Stick(torso_2, knee_2))
    sim.sticks.append(Stick(knee_1, leg_1))
    sim.sticks.append(Stick(knee_2, leg_2))


def setup_ragdolls(args, sim):
    ragdoll((500, 50, 20, -5), sim)
    ragdoll((300, 50, 20, 9), sim)
    ragdoll((700, 50, 20, 20), sim)


engine = Engine(setup_func=setup_ragdolls)
engine.run()