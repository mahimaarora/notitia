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
