import random
import collections

if __name__ == '__main__':

    def mean(x):
        return sum(x)/len(x)

    def median(v):
        n = len(v)
        sorted_v = sorted(v)

        midpoint = n // 2

        if n % 2 == 1:
            return sorted_v[midpoint]
        else:
            return (sorted_v[midpoint - 1] + sorted_v[midpoint]) / 2

    def quantile(x, p):
        p_index = int(p * len(x))
        return sorted(x)[p_index]

    def mode(x):
        counts = collections.Counter(x)
        max_count = max(counts.values())
        return [x_i for x_i in counts if counts[x_i] == max_count]


    data = []
    for i in range(200):
        data.append(random.randint(1, 100))
    print(sorted(data))
    print("Mean = %f" % mean(data))
    print("Median =  %f" % median(data))
    print("Quantile = %f" % quantile(data, 0.75))
    print("Mode = ", mode(data))

