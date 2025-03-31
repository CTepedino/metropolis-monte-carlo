import sys

import numpy as np

import matplotlib

from readFile import readFile, startIterator, nextGrid, closeIterator

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation



if __name__ == "__main__":
    global ani
    if len(sys.argv) > 1:
        matrix_file_path = sys.argv[1]
    else:
        matrix_file_path = "output.txt"

    N, p, steps, grid = startIterator(matrix_file_path)
    step = 0

    fig, ax = plt.subplots()
    cax = ax.imshow(grid, cmap="gray", vmin=-1, vmax=1)
    title = ax.set_title("monte carlo step 0")
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        global step
        global grid
        step += 1
        grid = nextGrid(grid)
        cax.set_array(grid)
        title.set_text(f"monte carlo step {frame}")
        return cax

    ani = animation.FuncAnimation(fig, update, frames=steps, interval=1, blit=False)

    plt.show()