import matplotlib.pyplot as plt
import numpy as np
import sys

def read_data(file_path):
    """
    Reads the data from a file where each line contains 'p mean std'.
    Returns three lists: probabilities (p), means, and standard deviations (std).
    """
    probabilities = []
    means = []
    stds = []
    
    with open(file_path, 'r') as file:
        for line in file:
            p, mean, std = map(float, line.strip().split())
            probabilities.append(p)
            means.append(mean)
            stds.append(std)
    
    return probabilities, means, stds

def plot_data(probabilities, means, stds):
    """
    Creates a scatter plot with error bars.
    X-axis: probabilities (p)
    Y-axis: susceptibility (mean)
    Error bars: standard deviations (std)
    """
    plt.errorbar(probabilities, means, yerr=stds, fmt='o', ecolor='black', capsize=5, markersize=8)
    plt.plot(probabilities, means, linestyle='-', color='blue')
    plt.xlabel('Probablidad')
    plt.ylabel('Susceptibilidad')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "data.txt"
    
    # Read the data from the file
    probabilities, means, stds = read_data(file_path)
    
    # Plot the data
    plot_data(probabilities, means, stds)
