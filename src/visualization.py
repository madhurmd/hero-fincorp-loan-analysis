import matplotlib.pyplot as plt

def plot_histogram(data, column, title):
    plt.figure()
    plt.hist(data[column], bins=30)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()
