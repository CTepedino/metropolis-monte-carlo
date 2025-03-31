import os
import sys

import matplotlib.pyplot as plt

import observables
from src.main.python.readFile import startIterator, nextGrid, closeIterator


def plot_consensus_evolution(consensus_list, n, p):
    os.makedirs('observables', exist_ok=True)
    
    steps = []
    for i in range(len(consensus_list)):
        steps.append(i)
    m_values = consensus_list

    plt.figure(figsize=(10, 6))
    plt.scatter(steps, m_values, marker='o', s=1)
    plt.xlabel('Paso de Monte Carlo')
    plt.ylabel('M')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    
    output_path = os.path.join('observables', f'consensus_evolution_n_{n}_p_{p}.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_file = sys.argv[1]
    else:
        results_file = "output.txt"

    N, p, steps, grid = startIterator(results_file)

    magnetization_list = []

    for i in range(steps-1):
        magnetization_list.append(observables.magnetization(N, grid))
        grid = nextGrid(grid)

    closeIterator()

    plot_consensus_evolution(magnetization_list, N, p)