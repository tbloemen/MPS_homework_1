"""
Send more money in CPMpy

sudoku solver
altered from CPMpy examples to work on sudoku's of any size
"""
import math

import numpy as np
from cpmpy import *
from numpy import ndarray

e = 0


def sudoku(given: ndarray):
    N = given.shape[0]
    # size of a region is region_n x region_n
    region_n = math.floor(math.sqrt(N))
    assert given.shape == (N, N)
    puzzle = intvar(1, N, shape=given.shape, name="puzzle")

    model = Model(
        # Constraints on values (cells that are not empty)
        puzzle[given != e] == given[given != e],  # numpy's indexing, vectorized equality
        # Constraints on rows and columns
        [AllDifferent(row) for row in puzzle],
        [AllDifferent(col) for col in puzzle.T],  # numpy's Transpose
    )

    # Constraints on blocks
    for i in range(0, N, region_n):
        ubi = i + region_n
        # the regions are not necessarily square if N is not a square number
        if ubi > N:
            ubi = N
        for j in range(0, N, region_n):
            ubj = j + region_n
            if ubi > N:
                ubi = N

            model += AllDifferent(puzzle[i:ubi, j:ubj])  # python's indexing

    return model, puzzle, N, region_n


# Solve and print
def sudoku_solve(given: ndarray):
    (model, puzzle, N, region_n) = sudoku(given)
    # print(N, region_n)
    if model.solve():
        # print(puzzle.value())
        # pretty print, mark givens with *
        out = ""
        for r in range(0, N):
            for c in range(0, N):
                out += str(puzzle[r, c].value())
                out += '* ' if given[r, c] else '  '
                out += ' ' if puzzle[r, c].value() < 10 else ''
                if (c + 1) % region_n == 0 and c != N - 1:  # end of block
                    out += '| '
            out += '\n'
            if (r + 1) % region_n == 0 and r != N - 1:  # end of block
                out += (('-' * region_n * 4) + '+-') * (region_n - 1) + ('-' * region_n * 4) + '\n'
        print(out)
    else:
        print("No solution found")


def main():
    e = 0  # value for empty cells
    _ = 0
    given = np.array([
        [e, e, e, 2, e, 5, e, e, e],
        [e, 9, e, e, e, e, 7, 3, e],
        [e, e, 2, e, e, 9, e, 6, e],

        [2, e, e, e, e, e, 4, e, 9],
        [e, e, e, e, 7, e, e, e, e],
        [6, e, 9, e, e, e, e, e, 1],

        [e, 8, e, 4, e, e, 1, e, e],
        [e, 6, 3, e, e, e, e, 8, e],
        [e, e, e, 6, e, 8, e, e, e]])
    sudoku1 = np.array([
        [_, 2, _, _, 3, _, 9, _, 7],
        [_, 1, _, _, _, _, _, _, _],
        [4, _, 7, _, _, _, 2, _, 8],
        [_, _, 5, 2, _, _, _, 9, _],
        [_, _, _, 1, 8, _, 7, _, _],
        [_, 4, _, _, _, 3, _, _, _],
        [_, _, _, _, 6, _, _, 7, 1],
        [_, 7, _, _, _, _, _, _, _],
        [9, _, 3, _, 2, _, 6, _, 5]
    ])
    sudoku_p0 = np.array([
        [_, _, _, 2, _, 5, _, _, _],
        [_, 9, _, _, _, _, 7, 3, _],
        [_, _, 2, _, _, 9, _, 6, _],
        [2, _, _, _, _, _, 4, _, 9],
        [_, _, _, _, 7, _, _, _, _],
        [6, _, 9, _, _, _, _, _, 1],
        [_, 8, _, 4, _, _, 1, _, _],
        [_, 6, 3, _, _, _, _, 8, _],
        [_, _, _, 6, _, 8, _, _, _]
    ])
    sudoku_p1 = np.array([
        [3, _, _, 9, _, 4, _, _, 1],
        [_, _, 2, _, _, _, 4, _, _],
        [_, 6, 1, _, _, _, 7, 9, _],
        [6, _, _, 2, 4, 7, _, _, 5],
        [_, _, _, _, _, _, _, _, _],
        [2, _, _, 8, 3, 6, _, _, 4],
        [_, 4, 6, _, _, _, 2, 3, _],
        [_, _, 9, _, _, _, 6, _, _],
        [5, _, _, 3, _, 9, _, _, 8]
    ])
    sudoku_p2 = np.array([
        [_, _, _, _, 1, _, _, _, _],
        [3, _, 1, 4, _, _, 8, 6, _],
        [9, _, _, 5, _, _, 2, _, _],
        [7, _, _, 1, 6, _, _, _, _],
        [_, 2, _, 8, _, 5, _, 1, _],
        [_, _, _, _, 9, 7, _, _, 4],
        [_, _, 3, _, _, 4, _, _, 6],
        [_, 4, 8, _, _, 6, 9, _, 7],
        [_, _, _, _, 8, _, _, _, _]
    ])
    sudoku_p3 = np.array([
        [_, _, 4, _, _, 3, _, 7, _],
        [_, 8, _, _, 7, _, _, _, _],
        [_, 7, _, _, _, 8, 2, _, 5],
        [4, _, _, _, _, _, 3, 1, _],
        [9, _, _, _, _, _, _, _, 8],
        [_, 1, 5, _, _, _, _, _, 4],
        [1, _, 6, 9, _, _, _, 3, _],
        [_, _, _, _, 2, _, _, 6, _],
        [_, 2, _, 4, _, _, 5, _, _]
    ])
    sudoku_p4 = np.array([
        [_, 4, 3, _, 8, _, 2, 5, _],
        [6, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, 1, _, 9, 4],
        [9, _, _, _, _, 4, _, 7, _],
        [_, _, _, 6, _, 8, _, _, _],
        [_, 1, _, 2, _, _, _, _, 3],
        [8, 2, _, 5, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, 5],
        [_, 3, 4, _, 9, _, 7, 1, _]
    ])
    sudoku_p5 = np.array([
        [_, _, _, _, _, 3, _, 6, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _],
        [_, 9, 7, 5, _, _, _, 8, _, _, _, _, _, 9, _, 2, _, _],
        [_, _, 8, _, 7, _, 4, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, 3, _, 6, _, _, _, _, _, 1, _, _, _, 2, 8, 9, _],
        [_, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, 5, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
    ])
    sudoku_p6 = np.array([
        [_, _, 3],
        [3, 1, 2],
        [2, 3, 1],
    ])
    sudoku_p89 = np.array([
        [11, 23, 13, 10, 19, 16, 6, 2, 24, 7, 5, 9, 1, 20, 17, 15, 8, 18, 25, 3, 4, 12, 21, 22, 14],
        [15, 16, e, 22, e, 11, 8, e, e, e, 25, e, 14, e, e, e, 12, 19, e, e, 17, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, 16, e, 4, e, 17, e, 13, e, 24, e, 23, 19, 10, 2],
        [e, e, e, e, e, 19, e, 14, 23, 4, e, 21, 6, 22, 10, e, 11, e, 2, e, e, e, e, e, e],
        [17, 14, e, e, 2, e, e, 13, 12, e, e, e, e, e, 15, 4, 20, 22, 10, e, 11, e, 9, 24, 8],
        [22, e, e, e, e, 6, 2, e, e, e, 4, 7, 12, 1, 9, e, e, e, e, e, e, 14, 5, e, e],
        [e, 18, 2, e, 8, 22, e, 19, 16, 21, e, e, e, 10, 13, 23, e, e, 20, e, e, 3, e, 15, 7],
        [e, e, 17, 3, e, 5, e, e, 8, 9, e, e, e, e, 18, e, 19, e, e, e, e, e, 23, 21, e],
        [1, 11, e, e, 9, e, 15, 10, 25, e, 6, e, 23, e, e, e, e, 5, 3, 7, e, 17, e, e, 24],
        [e, e, e, e, e, e, 1, e, e, 23, e, e, e, 24, e, e, e, 21, 12, e, 6, 8, e, 25, 16],
        [20, 24, 10, e, 15, 23, 11, 17, e, e, e, e, e, 7, e, 12, e, e, e, e, e, 22, e, e, 6],
        [4, 5, e, 14, 12, 25, e, 18, e, e, 23, e, 15, e, 19, 1, e, e, e, 22, 20, e, 7, 9, e],
        [18, e, 21, e, e, 8, e, 24, e, e, 9, e, 25, e, e, e, 10, e, e, e, 2, e, 1, 19, e],
        [e, e, 6, 2, 1, e, 13, e, 22, e, e, e, e, e, 11, 8, 21, 16, e, e, 25, e, e, 12, 17],
        [e, 17, 25, e, 23, 7, 14, e, 21, 1, e, e, e, e, 3, e, e, 11, e, e, 24, e, 16, 4, 5],
        [e, e, e, e, 11, 18, 24, e, e, e, e, 5, e, 12, e, 25, e, e, e, 15, 23, 4, 8, 14, e],
        [e, e, e, 15, 21, e, e, e, e, e, 2, e, 13, 17, e, e, 1, 7, e, e, 5, 9, 24, e, e],
        [e, e, 18, e, 22, 15, e, e, 2, 16, e, 23, e, e, e, 10, 6, 24, e, 17, 12, e, 25, 11, e],
        [7, 2, e, 1, e, e, 21, e, e, e, 18, 22, e, 9, 6, 14, e, 4, 5, 16, e, e, e, e, e],
        [e, e, 9, e, e, e, 7, 22, e, e, 10, e, 24, e, e, e, 18, e, e, e, 21, e, e, e, e],
        [e, 12, e, 19, 10, e, e, e, e, e, e, e, e, e, 1, e, e, e, e, e, 14, e, 4, 8, e],
        [24, e, 11, 18, e, e, e, e, e, e, e, 25, 17, 21, e, 6, e, e, 1, e, e, e, e, 5, 12],
        [16, 6, 22, e, e, e, 23, 4, 15, 18, 8, e, e, e, 20, e, e, 17, e, 14, e, e, e, e, e],
        [e, 21, e, e, 4, e, 9, 1, 7, e, e, e, e, 11, 14, e, 16, 8, 15, e, 22, e, 18, e, e],
        [8, 15, e, e, e, e, e, e, 5, e, 24, 3, e, e, 4, e, e, e, 9, e, e, e, e, e, 20]])
    sudoku_solve(given)


if __name__ == "__main__":
    main()
