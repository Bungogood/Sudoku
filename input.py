from sudoku import sudoku
from time import time
from sys import argv

def read():
    grid = []
    for r in range(1,10):
        row = input("row {}: ".format(r))
        while len(row) != 9:
            print("invalid row")
            row = input("row {}: ".format(r))
        grid.append([int(v) for v in row])
    return grid

if __name__ == "__main__":
    s = sudoku()
    s.grid = read()
    start = time()
    solved = s.solve()
    print(s)
    print("solved: {}".format(solved))
    print("time: {}".format(time()-start))