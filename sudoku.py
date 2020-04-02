class sudoku:
    def __init__(self, size=3):
        self.size = size
    
    def __str__(self):
        out = []
        for ri, r in enumerate(self.grid):
            if ri % self.size == 0:
                out.append(("+-" + "--" * self.size) * self.size + "+")
            row = []
            for ci, v in enumerate(r):
                if ci % self.size == 0:
                    row.append("|")
                row.append(" " if v == 0 else str(v))
            row.append("|")
            out.append(" ".join(row))
        out.append(("+-" + "--" * self.size) * self.size + "+")
        return "\n".join(out)
    
    def solve(self, r=0, c=0):
        if c == self.size**2:
            r, c = r+1, 0
            if r == self.size**2:
                return True
        
        if self.grid[r][c] != 0: 
            return self.solve(r, c+1)
        
        sr, sc = (r//self.size)*self.size, (c//self.size)*self.size
        for v in range(1, self.size**2+1):
            if self.valid(r, c, sr, sc, v):
                self.grid[r][c] = v
                if self.solve(r, c+1): 
                    return True
        
        self.grid[r][c] = 0
        return False
    
    def valid(self, r, c, sr, sc, v):
        for i in range(self.size**2):
            if self.grid[r][i] == v:
                return False
            elif self.grid[i][c] == v:
                return False
            elif self.grid[sr+i//self.size][sc+i%self.size] == v:
                return False
        else:
            return True