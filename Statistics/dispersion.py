import math
import random

if __name__ == '__main__':

    def data_range(x):
        return max(x) - min(x)

    def mean(x):
        return sum(x)/len(x)

    def de_mean(x):
        x_bar = mean(x)
        return [x_i - x_bar for x_i in x]

    def de_mean_sq(x):
        x_bar = mean(x)
        return [(x_i - x_bar) ** 2 for x_i in x]

    def variance(x):
        return sum(de_mean_sq(x)) / (len(x) - 1)

    def standard_deviation(x):
        return math.sqrt(variance(x))

    def quantile(x, p):
        p_index = int(p * len(x))
        return sorted(x)[p_index]

    def inter_quartile_range(x):
        return quantile(x, 0.75) - quantile(x, 0.25)

    def dot(x, y):
        return sum([x_i * y_i for x_i, y_i in zip(x, y)])

    def covariance(x, y):
        n = len(x)
        return dot(de_mean(x), de_mean(y)) / (n - 1)

    def correlation(x, y):  # -1 <= correlation(x, y) <= 1
        sd_x = standard_deviation(x)
        sd_y = standard_deviation(y)

        if sd_x > 0 and sd_y > 0:
            return covariance(x, y)/(sd_x * sd_y)


    data = []
    for i in range(200):
        data.append(random.randint(1, 100))
    print(sorted(data))

    print("Range = ", data_range(data))
    print("Variance = ", variance(data))
    print("Standard Deviation = ", standard_deviation(data))
    print("Inter-Quantile range = ", inter_quartile_range(data))

    data2 = []
    for i in range(200):
        data2.append(random.randint(1, 100))
    print(sorted(data2))
    print("Covariance = ", covariance(data, data2))
    print("Correlation = ", correlation(data, data2))
