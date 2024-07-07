import matplotlib.pyplot as plt

def plot_results(numbers):
    plt.plot(numbers)
    plt.ylabel('Numbers')
    plt.xlabel('Index')
    plt.title('Line Diagram')
    plt.show()

def plot_lines(lists, names):
    colors = ['b', 'g', 'r', 'c', 'm']
    for i in range(len(lists)):
        plt.plot(lists[i], color=colors[i], label=names[i])
    plt.ylabel('Numbers')
    plt.xlabel('Index')
    plt.title('Line Diagrams')
    plt.legend()
    plt.show()