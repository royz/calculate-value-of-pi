import random
import math

# let the length of a side of the square be 10
sq_side = 10000000000
sq_area = sq_side ** 2

# radius of the circle would be half of the square's height
radius = sq_side / 2


# check if the dart hit the circle
def within_circle(x, y, r):
    """
    if the distance of the dart from the center is less than
    or equal to radius then the dart hit the circle
    """
    return math.sqrt(x * x + y * y) <= r


# check with 1 billion darts
num_darts = 1_000_000_000

# num_darts = int(input('num darts: '))

# for all the darts randomly generate a coordinate within the
# square and check how many of them hit the circle

darts_within_circle = 0
pi = None

for i in range(num_darts):
    x = random.uniform(0, radius)
    y = random.uniform(0, radius)
    if within_circle(x, y, radius):
        darts_within_circle += 1

    # print value of pi at each 5000000 darts thrown
    if i % 5000000 == 0 and i != 0:
        # this ratio would be same as pi/4
        # so, the value of pi = ratio * 4
        ratio_of_c_and_s = darts_within_circle / i
        pi = ratio_of_c_and_s * 4
        print(f'{i} darts thrown. value of pi = {pi} ')

print(f'{num_darts} darts thrown. value of pi = {pi} ')
