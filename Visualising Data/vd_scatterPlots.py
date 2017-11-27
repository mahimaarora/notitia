from matplotlib import pyplot as plt

if __name__ == '__main__':

    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    # labelling each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, xy=(friend_count,minute_count),xytext=(5, -5),textcoords='offset points')

    plt.title("Daily minutes vs # of friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes")
    plt.show()