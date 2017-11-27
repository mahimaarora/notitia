from matplotlib import pyplot as plt

if __name__ == '__main__':

    x = []
    y = []

    for i in range(100):
        x.append(i)

    for i in range(100):
        y.append(x[i]**2)

    plt.plot(x,y,marker = '.',linestyle = 'solid',color = 'green')
    plt.ylabel('Square')
    plt.xlabel('n')
    plt.title('Square Function')
    plt.show()





