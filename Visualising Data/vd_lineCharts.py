from matplotlib import pyplot as plt

if __name__ == '__main__':

    variance = []

    for i in range(9):
        variance.append(2 ** i)
    # print(variance)

    bias_squared = []

    for i in range(9):
        bias_squared.append(variance[len(variance) - i - 1])

    total_error = [x + y for x, y in zip(variance, bias_squared)]

    x = [i for i, _ in enumerate(variance)]

    plt.plot(x, variance, 'g-', label = 'variance')
    plt.plot(x, bias_squared, 'b-.', label = 'bias squared')
    plt.plot(x, total_error, 'r:', label = 'total error')

    plt.legend(loc=9)
    # top center

    plt.xlabel('model complexity')
    plt.title('bias-variance')

    plt.show()


