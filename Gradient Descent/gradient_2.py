
if __name__ == '__main__':
    # returns f , if f gives an error returns infinity
    def safe(f):
        def safe_f(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                return float('inf')
        return safe_f

    # move step_size in the direction from v
    def step(vv, direction, step_size):
        return [v_i + step_size * direction_i
                for v_i, direction_i in zip(vv, direction)]

    def minimize_batch(target_fn,  gradient_fn, theta_0, tolerance=0.000001):
        step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

        theta = theta_0
        target_fn = safe(target_fn)
        value = target_fn(theta)

        while True:
            gradient = gradient_fn(theta)
            next_thetas = [step(theta, gradient, -step_size)
                           for step_size in step_sizes]
            next_theta = min(next_thetas)
            next_value = target_fn(next_theta)

            if abs(value - next_value) < tolerance:
                return theta
            else:
                theta, value = next_theta, next_value

    def negate(f):
        return lambda *args, **kwargs : -f(*args, **kwargs)

    def negate_all(f):
        return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

    def maximize_batch(target_fn,  gradient_fn, theta_0, tolerance=0.000001):
        return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)

