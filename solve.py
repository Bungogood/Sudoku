from sudoku import sudoku
from time import time
from sys import argv

def load(path):
    grid = []
    with open(path, "r") as f:
        raw = f.read()
        for r in raw.split("\n"):
            grid.append([int(v) for v in r])
    return grid

if __name__ == "__main__":
    assert len(argv) == 2, "no sudoku provided"
    s = sudoku()
    s.grid = load(argv[1])
    start = time()
    solved = s.solve()
    print(s)
    print("solved: {}".format(solved))
    print("time: {}".format(time()-start))