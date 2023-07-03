class GameOfLife:
    def __init__(self, width, height, expandable_borders=False, max_border_size=10000):
        self.width = width
        self.height = height
        self.expandable_borders = expandable_borders
        self.max_border_size = max_border_size
        self.grid = [[False] * self.width for _ in range(self.height)]

    def initialize_random(self, density=0.5):
        import random
        for row in range(self.height):
            for col in range(self.width):
                if random.random() < density:
                    self.grid[row][col] = True

    def initialize_custom(self, cells):
        for row, col in cells:
            if 0 <= row < self.height and 0 <= col < self.width:
                self.grid[row][col] = True

    def display(self):
        for row in self.grid:
            for cell in row:
                print("X" if cell else ".", end=" ")
            print()

    def get_neighbours(self, row, col):
        neighbours = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row = row + dr
                new_col = col + dc
                if self.expandable_borders:
                    if 0 <= new_row < self.height and 0 <= new_col < self.width:
                        neighbours.append((new_row, new_col))
                else:
                    if (
                        0 <= new_row < self.height
                        and 0 <= new_col < self.width
                        and self.grid[new_row][new_col]
                    ):
                        neighbours.append((new_row, new_col))
        return neighbours

    def update(self):
        new_grid = [[False] * self.width for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                cell = self.grid[row][col]
                neighbours = self.get_neighbours(row, col)
                live_neighbours = sum(self.grid[r][c] for r, c in neighbours)

                if cell and live_neighbours < 2:
                    new_grid[row][col] = False
                elif cell and 2 <= live_neighbours <= 3:
                    new_grid[row][col] = True
                elif cell and live_neighbours > 3:
                    new_grid[row][col] = False
                elif not cell and live_neighbours == 3:
                    new_grid[row][col] = True

        self.grid = new_grid

    def play(self, generations=50):
        for generation in range(generations):
            print(f"Generation {generation+1}:")
            self.display()
            self.update()
            print()

            if not self.expandable_borders and self.is_grid_empty():
                print("All cells have died. Game Over.")
                break

    def is_grid_empty(self):
        return all(not any(row) for row in self.grid)


# Example usage:

# Fixed Borders
game_fixed = GameOfLife(10, 10)
game_fixed.initialize_random(density=0.3)
game_fixed.play()

# Expandable Borders
game_expandable = GameOfLife(10, 10, expandable_borders=True)
game_expandable.initialize_random(density=0.3)
game_expandable.play()
