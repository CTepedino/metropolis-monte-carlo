import sys
from readFile import readFile


def magnetization(N, state, t):
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

    for i in range(100):
        print(magnetization(N, state, i))


