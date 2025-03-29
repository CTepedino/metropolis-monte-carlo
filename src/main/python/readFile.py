import copy
from typing import TextIO


def readMatrix(f, N):
    matrix = []
    for i in range(N):
        values = f.readline().split()
        line = []
        for j in range(N):
            line.append(int(values[j]))
        matrix.append(line)
    return matrix

# def readFile(filename):
#     state = []
#     with open(filename, "r") as f:
#         N = int(f.readline().strip())
#         p = float(f.readline().strip())
#
#         state.append(readMatrix(f, N))
#         next_iter = f.readline().strip()
#         while next_iter != "end":
#             state.append(readMatrix(f, N))
#             next_iter = f.readline().strip()
#
#     return N, p, state

def readFile(filename):
    state = []
    with open(filename, "r") as f:
        N = int(f.readline().strip())
        p = float(f.readline().strip())
        step_count = int(f.readline().strip())

        state.append(readMatrix(f, N))
        for i in range(step_count):
            next_matrix = copy.deepcopy(state[i])
            while True:
                line = f.readline().split()
                if line[0] == "next" or line[0] == "end":
                    break
                row, col = line
                next_matrix[int(row)][int(col)] = -1 * next_matrix[int(row)][int(col)]
            state.append(next_matrix)

    return N, p, state

f: TextIO

def startIterator(filename):
    global f
    f = open(filename, "r")
    N = int(f.readline().strip())
    p = float(f.readline().strip())
    step_count = int(f.readline().strip())
    grid = readMatrix(f, N)

    return N, p, step_count, grid

def nextGrid(prev_grid: [[int]]):
    global f
    while True:
        line = f.readline().split()
        if line[0] == "next" or line[0] == "end":
            break
        row, col = line
        prev_grid[int(row)][int(col)] = -1 * prev_grid[int(row)][int(col)]

    return prev_grid


def closeIterator():
    global f
    f.close()