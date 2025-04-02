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

def plot_data(probabilities, means, stds, scalar):
    """
    Creates a scatter plot with error bars.
    X-axis: probabilities (p)
    Y-axis: consensus averages (mean)
    Error bars: standard deviations (std)
    """
    plt.errorbar(probabilities, means, yerr=stds, fmt='o', ecolor='black', capsize=5, markersize=10)
    plt.scatter(probabilities, means, color='blue')
    plt.xlabel('Probablidad')
    plt.ylabel(f'{scalar} Promedio')
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.grid(True, linestyle='--', alpha=0.7)
    output_path = os.path.join('observables', f'{scalar}_average_from_{probabilities[0]}_to_{probabilities[-1]}.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "data.txt"
    
    all_probabilities = [0.2, 0.15, 0.125, 0.1125, 0.10625, 0.01, 0.05, 0.075, 0.0875, 0.09375, 0.096875]
    all_numbers = [50]
    scalars = ["magnetization", "susceptibility"]
    magnetization_means = []
    magnetization_stds = []
    susceptibility_means = []
    susceptibility_stds = []

    for scalar in scalars:
        for p in all_probabilities:
            for n in all_numbers:
                file_path = f"{scalar}_p_{p}_n_{n}.txt"
                probabilities, means, stds = read_data(file_path)
                if scalar == "magnetization":
                    magnetization_means.append(means[0])
                    magnetization_stds.append(stds[0])
                else:
                    susceptibility_means.append(means[0])
                    susceptibility_stds.append(stds[0])

    plot_data(all_probabilities, magnetization_means, magnetization_stds, scalars[0])
    plot_data(all_probabilities, susceptibility_means, susceptibility_stds, scalars[1])
    