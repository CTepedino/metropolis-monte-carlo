import sys
from readFile import readFile
from analysis import plot_consensus_evolution

def magnetization(N: int, state, t: int):
    grid_sum = 0
    for row in state[t]:
        for s in row:
            grid_sum += s

    return abs(grid_sum/(N**2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_file = sys.argv[1]
    else:
        results_file = "output.txt"

    N, p, state = readFile(results_file)

    magnetization_list = []
    for i, grid in enumerate(state):
        magnetization_list.append(magnetization(N, state, i))

    plot_consensus_evolution(magnetization_list, N, p)
