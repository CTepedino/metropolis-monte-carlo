import sys


def readMatrix(f, N):
    f.readline().strip()

    values = f.readline().split()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        results_file = sys.argv[1]
    else:
        results_file = "output.txt"

    state = []
    with open(results_file, "r") as f:
        N = int(f.readline().strip())
        p = float(f.readline().strip())

        state.append(readMatrix(f, N))

    print(N)
    print(p)


