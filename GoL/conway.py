"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from numpy.core.shape_base import block
import config

ON = 1
OFF = 0
vals = [ON, OFF]
GEN = 0
N = config.UNIVERSE_SIZE

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def countNeighbors(grid, x, y, limx, limy):
    """count number of live neighbors"""
    neighbors = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            if x+i >= 0 and x+i < limx:
                if y+j >= 0 and y+j < limy:
                    neighbors += grid[x+i][y+j]
            j += 1 
        i += 1
    # ommit self value
    neighbors -= grid[x][y]
    return neighbors


def checkCells(newGrid):
    """check the rules for Conway's GoL"""
    for i in range(newGrid.shape[0]):
        for j in range(newGrid.shape[1]):
            # count live neighbors
            print(j)

            print(f"live neighbors at [{i} , {j}]: {countNeighbors(newGrid, i, j, N, N)}\n")



def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 1], 
                       [1,  0, 1], 
                       [0,  1, 1]])
    grid[i:i+3, j:j+3] = glider

def addLightWeight(i, j, grid):
    """adds a light-weight spaceship with top left cell at (i, j)"""
    lightWeight = np.array([[0, 1, 1, 0, 1],
                            [1, 1, 1, 1,0],
                            [0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 0]])
    grid[i:i+4, j:j+5] = lightWeight

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    checkCells(newGrid)

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
        
    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(N)
    # Uncomment lines to see the "glider" & "light weight" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)
    #addLightWeight(5, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show(block=True)

# call main
if __name__ == '__main__':
    main()