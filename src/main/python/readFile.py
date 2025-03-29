import sys



def readMatrix(f, N):
    matrix = []
    for i in range(N):
        values = f.readline().split()
        line = []
        for j in range(N):
            line.append(int(values[j]))
        matrix.append(line)
    return matrix

def readFile(filename):
    state = []
    with open(filename, "r") as f:
        N = int(f.readline().strip())
        p = float(f.readline().strip())

        state.append(readMatrix(f, N))
        next_iter = f.readline().strip()
        while next_iter != "end":
            state.append(readMatrix(f, N))
            next_iter = f.readline().strip()

    return N, p, state
