import random
import math
if __name__ == '__main__':

    # move step_size in the direction from v
    def step(vv, direction, step_size):
        return [v_i + step_size * direction_i
                for v_i, direction_i in zip(vv, direction)]

    def sum_of_squares_gradient(v):
        return [2 * v_i for v_i in v]

    v = [random.randint(-10, 10) for i in range(3)]
    # random starting point
    tolerance = 0.0000001   # 0.01, 0.001, 0.00001 ...

    def dist(a, b):
        return math.sqrt(sum((a_i - b_i) ** 2 for a_i, b_i in zip(a, b)))

    while True:
        gradient = sum_of_squares_gradient(v)
        next_v = step(v, gradient, -0.01)
        if dist(next_v, v) < tolerance:
            break
        v = next_v

    print(v)   # v ~ 0 (smaller tolerance)
