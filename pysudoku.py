
class SudokuPuzzle(object):
    def __init__(self):
        self.grid = [[] for _ in range(9)]

    def __str__(self):
        return '\n'.join([str(row) for row in self.grid])

    @classmethod
    def from_rows(cls, rows):
        new_puzzle = cls()
        for index, row in enumerate(rows):
            for number in row:
                new_puzzle.grid[index].append(int(number))
        return new_puzzle

    def get_cell(self, x, y):
        return self.grid[y-1][x-1]

    def set_cell(self, x, y, value):
        self.grid[y-1][x-1] = value

if __name__ == '__main__':
    with open('puzzle') as f:
        rows = f.read().splitlines()

    grid = SudokuPuzzle.from_rows(rows)
    print grid
