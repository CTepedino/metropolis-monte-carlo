import os
import re

import matplotlib.pyplot as plt
import numpy as np


def plot_consensus_evolution(consensus_list, n, p):
    os.makedirs('observables', exist_ok=True)
    
    steps = []
    for i in range(len(consensus_list)):
        steps.append(i)
    m_values = consensus_list

    plt.figure(figsize=(10, 6))
    plt.scatter(steps, m_values)
    plt.title(f'Evolución temporal del Consenso (M) en pasos de Monte Carlo para N = {n} y p = {p}')
    plt.xlabel('Cantidad de pasos de Monte Carlo')
    plt.ylabel('M')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    output_path = os.path.join('observables', 'consensus_evolution.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    