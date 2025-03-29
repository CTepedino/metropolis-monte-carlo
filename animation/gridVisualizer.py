import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
matplotlib.use("TkAgg")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        matrix_file_path = sys.argv[1]
    else:
        matrix_file_path = "output.txt"

    # Example input grids (list of NxN numpy arrays)
    grids = [np.random.choice([1, -1], size=(5, 5)) for _ in range(10)]  # Example with 10 frames

    fig, ax = plt.subplots()
    cax = ax.imshow(grids[0], cmap="coolwarm", vmin= -1, vmax=1)

    def update(frame):
        cax.set_array(grids[frame])
        ax.set_title(f"step {(frame + 1)**2}")

    ani = animation.FuncAnimation(fig, update, frames = len(grids), interval= 1000)


    plt.show()
    plt.close()