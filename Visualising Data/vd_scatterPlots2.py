from matplotlib import pyplot as plt

if __name__ == '__main__':
    test_1_grades = [99, 90, 85, 97, 89]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades,test_2_grades)

    plt.xlabel('test 1 grades')
    plt.ylabel('test 2 grade')
    plt.title('axis are not comparable')

    plt.show()