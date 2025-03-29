import sys

import numpy as np

import matplotlib

from src.main.python.readFile import readFile

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation



if __name__ == "__main__":
    global ani
    if len(sys.argv) > 1:
        matrix_file_path = sys.argv[1]
    else:
        matrix_file_path = "output.txt"

    N, p, grids = readFile(matrix_file_path)

    fig, ax = plt.subplots()
    cax = ax.imshow(grids[0], cmap="gray", vmin=-1, vmax=1)
    title = ax.set_title("monte carlo step 0")
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        cax.set_array(grids[frame])
        title.set_text(f"monte carlo step {frame}")
        return cax, title

    ani = animation.FuncAnimation(fig, update, frames=len(grids), interval=1, blit=False)

    plt.show()