import matplotlib.pyplot as plt

def plot_results(numbers):
    plt.plot(numbers)
    plt.ylabel('Numbers')
    plt.xlabel('Index')
    plt.title('Line Diagram')
    plt.show()