import sys

import numpy as np

from observables import magnetization_mean, magnetization, susceptibility
from src.main.python.readFile import readFile


def magnetization_mean_mean_and_std(p):
    magnetization_means = []

    for i in range(36, 46):
        magnetization_list = []
        N, p, grids = readFile(f"outs/p_{p:.6f}_s_{i}")
        for g in grids:
            magnetization_list.append(magnetization(N, g))
        magnetization_means.append(magnetization_mean(magnetization_list[5000:])[0])

    return np.mean(magnetization_means), np.std(magnetization_means)


def susceptibility_mean_and_std(p):
    susceptibilities = []

    for i in range(36, 46):
        magnetization_list = []
        N, p, grids = readFile(f"outs/p_{p:.6f}_s_{i}")
        for g in grids:
            magnetization_list.append(magnetization(N, g))
        susceptibilities.append(susceptibility(N, magnetization_list[5000:])[0])

    return np.mean(susceptibilities), np.std(susceptibilities)

if __name__ == "__main__":
    p = 0.05

    print(magnetization_mean_mean_and_std(p))
    print(susceptibility_mean_and_std(p))