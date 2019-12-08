from ECA import ECA

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit
import time

debug = True

def visualize_board(board, title=None):
    plt.figure(figsize=(5,2.5))
    plt.imshow(board, cmap="Greys")
    plt.axis("off")
    if title is not None:
        plt.title(title, fontsize=14)
    plt.show()
    plt.close()

def main():

    rules =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19,
        22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40,
        41, 42, 43, 44, 45, 46, 50, 51, 54, 56, 57, 58, 60, 62, 72, 73, 74,
        76, 77, 78, 90, 94, 104, 105, 106, 108, 110, 122, 126, 128, 130,
        132, 134, 136, 138, 140, 142, 146, 150, 152, 154, 156, 160, 162,
        164, 168, 170, 172, 178, 184, 200, 204, 232]

    rules = [126]

    width = 3600
    height = 5400

    starting_configuration = [0] * width
    starting_configuration[int(width / 2)] = 1

    for rule in rules:
        if debug: print("rule : " + str(rule));

        automata = ECA(rule, width, height, starting_configuration)
        automata.generate()
        # print(automata.universe)
        print("visualizing board...")
        visualize_board(automata.get_2d_universe(), rule)


if __name__ == '__main__':

    time_start = time.time()
    main()
    time_end = time.time()

    print("runtime : " + str(time_end - time_start) + " seconds")
