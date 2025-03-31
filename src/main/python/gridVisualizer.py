import os
import sys

import numpy as np

import matplotlib


from readFile import readFile, startIterator, nextGrid, closeIterator

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation


if __name__ == "__main__":
    os.makedirs('animations', exist_ok=True)

    global ani
    if len(sys.argv) > 1:
        matrix_file_path = sys.argv[1]
    else:
        matrix_file_path = "output.txt"

    N, p, steps, grid = startIterator(matrix_file_path)

    fig, ax = plt.subplots()
    cax = ax.imshow(grid, cmap="gray", vmin=-1, vmax=1)
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        global grid
        grid = nextGrid(grid)
        cax.set_array(grid)
        return [cax]

    ani = animation.FuncAnimation(fig, update, frames=5000, interval=1, blit=True)

    output_path = os.path.join('animations', f'animation_n_{N}_p_{p}.mp4')
    writer = animation.FFMpegWriter(fps=60, bitrate=1800)

    ani.save(output_path, writer=writer)