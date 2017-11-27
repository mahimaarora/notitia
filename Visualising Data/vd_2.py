from random import randint
from matplotlib import pyplot as plt

if __name__ == '__main__':

    years = []

    for i in range(2000, 2010, 2):
        years.append(i)

    print(years)
    data = []

    for i in range(len(years)):
        data.append(randint(1, 10))

    x = [j + 0.1 for i, j in enumerate(years)]

    plt.bar(years, data)
    plt.ylabel('Random Data')
    plt.xlabel('Years')
    plt.title('Data')
    plt.show()


