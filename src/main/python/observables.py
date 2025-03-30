import sys
from readFile import readFile
from analysis import plot_consensus_evolution
from readFile import startIterator, nextGrid, closeIterator


def magnetization(N: int, grid: [[int]]):
    grid_sum = 0
    for row in grid:
        for s in row:
            grid_sum += s

    return abs(grid_sum/(N**2))

def steady_magnetization_mean(consensus_list: [int], minimal_value: float):
    steady_sum = 0 
    n = 0
    for m in consensus_list:
        if m >= minimal_value:
            n += 1
            steady_sum += m
        
    return steady_sum/n

def steady_squared_magnetization_mean(consensus_list: [int], minimal_value: float):
    steady_sum = 0 
    n = 0
    for m in consensus_list:
        if m >= minimal_value:
            n += 1
            steady_sum += m ** 2
        
    return steady_sum/n


def susceptibility(N: int, consensus_list: [int], minimal_value: float):
    return (N ** 2) * (steady_squared_magnetization_mean(consensus_list, minimal_value) - (steady_magnetization_mean(consensus_list, minimal_value) ** 2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_file = sys.argv[1]
    else:
        results_file = "output.txt"

    N, p, steps, grid = startIterator(results_file)

    magnetization_list = []

    for i in range(steps-1):
        magnetization_list.append(magnetization(N, grid))
        grid = nextGrid(grid)

    closeIterator()

    plot_consensus_evolution(magnetization_list, N, p)
