"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

"""
import random
random.seed(0xBADC0FFE)

NO_OF_ITERATIONS = 1000000
SQUARE_SIZE = 100

pic = 0                 # Point In Circle
pis = 0                 # Point In Square

prev_pi = 0
pi_approx = 3

while True:
    while pis < NO_OF_ITERATIONS:
        x = random.randint(0, SQUARE_SIZE) / SQUARE_SIZE
        y = random.randint(0, SQUARE_SIZE) / SQUARE_SIZE

        if float(float(x ** 2) + float(y ** 2)) < float(1):
            pic += 1
            pis += 1
        else:
            pis += 1

    prev_pi = pi_approx
    pi_approx = 4 * pic / float(pis)
    print('prev_pi = {}, pi_approx = {}'.format(prev_pi, pi_approx))
    if abs(prev_pi - pi_approx) < 1e-9:
        break

print(
    pic, pis, pi_approx
)

