import matplotlib.pyplot as plt
import numpy as np
import sys
import os

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
    Y-axis: consensus averages (mean)
    Error bars: standard deviations (std)
    """
    plt.errorbar(probabilities, means, yerr=stds, fmt='o', ecolor='black', capsize=5, markersize=10)
    plt.plot(probabilities, means, linestyle='-', color='blue')
    plt.xlabel('Probablidad')
    plt.ylabel('Consenso Promedio')
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.grid(True, linestyle='--', alpha=0.7)
    output_path = os.path.join('observables', f'consensus_average_from_{probabilities[0]}_to_{probabilities[-1]}.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "data.txt"
    
    # Read the data from the file
    probabilities, means, stds = read_data(file_path)
    
    # Plot the data
    plot_data(probabilities, means, stds)
