import matplotlib.pyplot as plt


if __name__ == '__main__':

    def difference_quotient(f, x, h):
        return (f(x + h) - f(x)) / h

    def square(x):
        return x * x

    def derivative(x):
        return 2 * x

    y = []
    for x in range(-10, 10):
        y.append(derivative(x))

    y_estimate = []
    for x in range(-10, 10):
        y_estimate.append(difference_quotient(square, x, h=0.00001))

    x = range(-10, 10)
    plt.title("Actual Derivatives vs. Estimates")
    plt.plot(x, y, 'rx', label='Actual')
    plt.plot(x, y_estimate, 'b+', label='Estimate')

    plt.legend(loc=9)
    plt.show()

    # compute the ith partial difference quotient of f at v
    def partial_difference_quotient(f, v, i, h):
        w = [v_j + (h if j == i else 0)
             for j, v_j in enumerate(v)]
        return (f(w) - f(v)) / h

    def estimate_gradient(f, v, h=0.00001):
        return [partial_difference_quotient(f, v, i, h)
                for i, _ in enumerate(v)]

   




