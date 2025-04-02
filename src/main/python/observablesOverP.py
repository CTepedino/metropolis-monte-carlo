import sys

import numpy as np

from observables import magnetization_mean, magnetization, susceptibility
from readFile import readFile

def magnetization_mean_mean_and_std(p):
    magnetization_means = []

    for i in range(36, 46):
        magnetization_list = []
        N, p, grids = readFile(f"outs/p_{p:.6f}_s_{i}")
        for g in grids:
            magnetization_list.append(magnetization(N, g))
        magnetization_means.append(magnetization_mean(magnetization_list[5000:])[0])

    return np.mean(magnetization_means), np.std(magnetization_means), magnetization_list


def susceptibility_mean_and_std(p, N, magnetization_list):
    susceptibilities = []

    #for i in range(36, 46):
        #magnetization_list = []
        #N, p, grids = readFile(f"outs/p_{p:.6f}_s_{i}")
        #for g in grids:
            #magnetization_list.append(magnetization(N, g))
    susceptibilities.append(susceptibility(N, magnetization_list[5000:])[0])

    return np.mean(susceptibilities), np.std(susceptibilities)

if __name__ == "__main__":
    all_probabilities = [0.05, 0.075, 0.0875, 0.09375, 0.096875]
    #all_probabilities = [0.2, 0.15, 0.125, 0.1125, 0.10625, 0.01, 0.05, 0.075, 0.0875, 0.09375, 0.096875]
    all_numbers = [50]

    for p in all_probabilities:
        for n in all_numbers:
            with open(f"magnetization_p_{p}_n_{n}.txt", "w") as f1:
                magnetization_mean_result, magnetization_std, magnetization_list = magnetization_mean_mean_and_std(p)
                f1.write(f"{p} {magnetization_mean_result} {magnetization_std}")
            with open(f"susceptibility_p_{p}_n_{n}.txt", "w") as f2:
                susceptibility_mean_result, susceptibility_std = susceptibility_mean_and_std(p,n,magnetization_list)
                f2.write(f"{p} {susceptibility_mean_result} {susceptibility_std}")
