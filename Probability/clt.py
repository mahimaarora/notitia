from matplotlib import pyplot as plt
import random
import collections
import math

if __name__ == '__main__':

    def uniform_pdf(x):
        return 1 if x in range(0, 1) else 0

    def uniform_cdf(x):
        if x < 0:
            return 0
        elif x < 1:
            return x
        else:
            return 1

    def normal_pdf(x,mu=0, sigma=1):
        sqrt_two_pi = math.sqrt(2 * math.pi)
        return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)

    def bernoulli_trial(p):
        return 1 if random.random() < p else 0

    # print(bernoulli_trial(0.3))

    def binomial(n, p):
        return sum(bernoulli_trial(p) for _ in range(n))
    # print(binomial(5, 0.5))

    def normal_cdf(x, mu=0, sigma=1):
        return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

    def make_hist(p, n, num_points):
        data = [binomial(n, p) for _ in range(num_points)]

        # bar chart => actual binomial samples
        histogram = collections.Counter(data)
        plt.bar([x for x in histogram.keys()],
                [y / num_points for y in histogram.values()],
                0.6,
                color='0.75')

        mu = p * n
        sigma = math.sqrt(n * p * (1 - p))

        # line chart => normal approximation
        xs = range(min(data), max(data))
        ys = []
        for i in xs:
            ys.append(normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma))
        plt.plot(xs, ys)
        plt.title('Binomial Distribution vs. Normal Approximation')
        plt.show()


    make_hist(0.6, 100, 10000)









