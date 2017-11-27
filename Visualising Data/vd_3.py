# implementting histogram

from matplotlib import pyplot as plt

from collections import Counter

if __name__ == '__main__':
    grades = [83, 95, 91, 87, 70, 0, 82, 85, 100, 67, 73, 77, 0]
    # print(grades)

    decile = lambda grade: grade
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 2)

    plt.axis([-5, 105, 0, 5])
    plt.xticks([10 * i for i in range(11)])

    plt.xlabel('Decile')
    plt.ylabel('# of students')
    plt.title('Grades Distribution')

    plt.show()
