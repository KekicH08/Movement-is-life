import random

import balls


#  появление вражеских шариков
def spawn_ball(radius, type, speed):
    if random.randint(0, 1):
        balls.Ball(radius, random.randint(-50, -30), random.randint(-200, 800), type, speed)
    else:
        balls.Ball(radius, random.randint(-20, 0) + 1220, random.randint(-200, 800), type,
                   speed)


#  случайная генерация разных шариков
def generate_balls(level):
    for i in range(2 * level):
        ball_seed = random.randint(0, 100)
        if ball_seed < (6 / level + 4):
            spawn_ball(20, 'green', 6)
        elif (6 / level + 9) > ball_seed > (6 / level + 4) and level > 1:
            spawn_ball(15, 'pink', 10)
        elif (6 / level + 13) > ball_seed > (6 / level + 9) and level > 1:
            spawn_ball(25, 'brown', 4)
        elif (6 / level + 17) > ball_seed > (6 / level + 13) and level > 2:
            spawn_ball(35, 'crimson', 3)
        elif (6 / level + 22) > ball_seed > (6 / level + 17) and level > 2:
            spawn_ball(15, 'gold', 7)
        elif (6 / level + 30) > ball_seed > (6 / level + 22):
            spawn_ball(20, 'black', 5)
        else:
            spawn_ball(20, 'blue', 6)
