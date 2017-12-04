import random

"""Computes the gradient (and takes a step) for only one point at a time.
It cycles over our data repeatedly until it reaches a stopping point.
"""

if __name__ == '__main__':

    def in_random_order(data):
        indexes = [i for i, _ in enumerate(data)]
        random.shuffle(indexes)                # returns elements of data in random order
        for i in indexes:
            yield data[i]

    def scalar_multiply(c, v):
        return [c * v_i for v_i in v]

    def vector_subtract(v, w):
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
        data = zip(x, y)
        theta = theta_0
        alpha = alpha_0
        min_theta, min_value = None, float("inf")
        iterations_with_no_improvement = 0

        while iterations_with_no_improvement < 100:
            value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

            if value < min_value:
                min_theta, min_value = theta, value
                iterations_with_no_improvement = 0
                alpha = alpha_0
            else:
                iterations_with_no_improvement += 1
                alpha *= 0.9

            for x_i, y_i in in_random_order(data):
                gradient_i = gradient_fn(x_i, y_i, theta)
                theta = vector_subtract(theta, scalar_multiply(alpha,gradient_i))

        return min_theta


    def negate(f):
        return lambda *args, **kwargs: -f(*args, **kwargs)


    def negate_all(f):
        return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


    def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
        return minimize_stochastic(negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0)




