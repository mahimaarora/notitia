from matplotlib import pyplot as plt

if __name__ == '__main__':
    mentions = [500, 510]
    years = [2013, 2014]

    plt.bar([2013, 2014], mentions, 0.8)
    plt.xticks(years)
    plt.ticklabel_format(useOffset=False)
    plt.axis([2012.5, 2014.5, 499, 511])
    plt.show()