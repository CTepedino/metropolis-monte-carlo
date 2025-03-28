import matplotlib
import matplotlib.pyplot as plt
import os
import numpy as np
import re

def get_consensus(grid):
    N = grid.shape[0]
    return abs(np.sum(grid) / (N ** 2))

def get_consensus_list_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    match = re.match(r'N:\s*(\d+)\s*\np:\s*([\d,\.]+)', content)
    if not match:
        raise ValueError("Could not find N and p values at the start of the file")
    
    N = int(match.group(1))
    p = float(match.group(2).replace(',', '.'))
    
    matrix_pattern = re.compile(r'\[\s*(\[[^\]]*\][\s\n]*)+\]', re.DOTALL)
    matrices = [match.group(0) for match in matrix_pattern.finditer(content)]

    consensus_list = []
    
    row_pattern = re.compile(r'\[([^\[\]]*)\]')
    for matrix_str in matrices:
        matrix_rows = []
        rows = row_pattern.findall(matrix_str)
        for row in rows:
            row = [int(x) for x in row.split()]
            matrix_rows.append(row)
        
        grid = np.array(matrix_rows)
        
        consensus = get_consensus(grid)
        consensus_list.append(consensus)
    
    return N, p, consensus_list

def plot_consensus_evolution(consensus_list, n, p):
    os.makedirs('observables', exist_ok=True)
    
    steps = []
    for i in range(len(consensus_list)):
        steps.append(i)
    m_values = consensus_list

    plt.figure(figsize=(10, 6))
    plt.plot(steps, m_values, marker='o', linestyle='-', markersize=4)
    plt.title(f'Evolución temporal del Consenso (M) en pasos de Monte Carlo para N = {n} y p = {p}')
    plt.xlabel('Cantidad de pasos de Monte Carlo')
    plt.ylabel('M')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    output_path = os.path.join('observables', 'consensus_evolution.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
n, p ,consensus_list = get_consensus_list_from_file('output.txt')
plot_consensus_evolution(consensus_list, n, p)