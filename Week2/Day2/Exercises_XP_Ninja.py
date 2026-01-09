# 1: Create the basic helper function for neighbors
def get_neighbors(cell):
    """Return the 8 possible neighbors of a cell (x, y)."""
    x, y = cell
    return [
        (x + dx, y + dy)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if not (dx == 0 and dy == 0)
    ]


# 2: Create the main GameOfLife class with fixed borders
class GameOfLife:
    """
    Conway's Game of Life with fixed borders.
    Cells outside the grid are considered dead (patterns can "exit" the game).
    """
    def __init__(self, width, height, initial_live_cells=None):
        """
        Initialize the game with fixed size grid.
        initial_live_cells: list of (x, y) tuples that are alive at start.
        """
        self.width = width
        self.height = height
        self.live_cells = set(initial_live_cells or [])


# 3: Add the step() method to advance one generation
    def step(self):
        """Compute the next generation according to the rules."""
        # Collect all cells that might change (live cells + their neighbors)
        candidates = set(self.live_cells)
        for cell in self.live_cells:
            candidates.update(get_neighbors(cell))

        new_live = set()

        for cell in candidates:
            x, y = cell
            # Skip cells outside the fixed borders
            if not (0 <= x < self.width and 0 <= y < self.height):
                continue

            neighbor_count = sum(n in self.live_cells for n in get_neighbors(cell))

            if cell in self.live_cells:
                # Survival: 2 or 3 neighbors → stays alive
                if neighbor_count in (2, 3):
                    new_live.add(cell)
            else:
                # Birth: exactly 3 neighbors → becomes alive
                if neighbor_count == 3:
                    new_live.add(cell)

        self.live_cells = new_live


# 4: Add display() method to print the grid
    def display(self):
        """Return a string representation of the current grid."""
        grid = [['.' for _ in range(self.width)] for _ in range(self.height)]
        for x, y in self.live_cells:
            if 0 <= x < self.width and 0 <= y < self.height:
                grid[y][x] = '#'
        return '\n'.join(''.join(row) for row in grid)


# 5: Bonus - Create ExpandableGameOfLife class with dynamic borders
class ExpandableGameOfLife:
    """
    Bonus version: Grid expands automatically as patterns grow.
    Maximum size limited to prevent memory issues.
    """
    def __init__(self, initial_live_cells=None, max_size=10000):
        self.max_size = max_size
        self.live_cells = set(initial_live_cells or [])
        self._update_bounds()

    def _update_bounds(self):
        """Update visible bounds with some padding for future growth."""
        if not self.live_cells:
            self.min_x = self.min_y = self.max_x = self.max_y = 0
            return

        xs = [x for x, y in self.live_cells]
        ys = [y for x, y in self.live_cells]

        self.min_x = min(xs) - 3
        self.max_x = max(xs) + 3
        self.min_y = min(ys) - 3
        self.max_y = max(ys) + 3

        # Safety check
        if (self.max_x - self.min_x > self.max_size or
            self.max_y - self.min_y > self.max_size):
            raise MemoryError("Pattern grew too large!")

    def step(self):
        """Advance one generation (same rules, no border limits)."""
        candidates = set(self.live_cells)
        for cell in self.live_cells:
            candidates.update(get_neighbors(cell))

        new_live = set()

        for cell in candidates:
            neighbor_count = sum(n in self.live_cells for n in get_neighbors(cell))
            if cell in self.live_cells:
                if neighbor_count in (2, 3):
                    new_live.add(cell)
            else:
                if neighbor_count == 3:
                    new_live.add(cell)

        self.live_cells = new_live
        self._update_bounds()

    def display(self):
        """Display the current generation with dynamic bounds."""
        if not self.live_cells:
            return "Empty grid"

        grid = []
        for y in range(self.min_y, self.max_y + 1):
            row = []
            for x in range(self.min_x, self.max_x + 1):
                row.append('#' if (x, y) in self.live_cells else '.')
            grid.append(''.join(row))
        return '\n'.join(grid)


# 6: Add a simulation runner with detection of stable/cycle/end
def run_simulation(game, max_steps=50, delay=0.2):
    """
    Run the simulation and print each generation.
    Detects:
      - Stability (no change)
      - Cycles (repeating state)
      - Death (all cells gone)
    """
    import time
    seen_states = {}
    step = 0

    while step < max_steps:
        state = frozenset(game.live_cells)

        print(f"\n=== Generation {step} ===")
        print(game.display())

        if not game.live_cells:
            print("→ All cells died! Game over.")
            break

        if state in seen_states:
            print(f"→ Cycle detected! Period: {step - seen_states[state]}")
            break

        seen_states[state] = step

        prev_state = state
        game.step()

        if frozenset(game.live_cells) == prev_state:
            print("→ Pattern stabilized!")
            print(game.display())
            break

        step += 1
        time.sleep(delay)  # Optional: slow down for visual effect
    else:
        print("→ Reached maximum steps.")


# 7: Provide several example initial patterns to test
if __name__ == "__main__":
    print("Conway's Game of Life - Examples\n")

    # Example 1: Block (still life - stable)
    print("Example 1: Block (stable)")
    block = GameOfLife(6, 6, [(2,2), (2,3), (3,2), (3,3)])
    run_simulation(block, max_steps=5)

    # Example 2: Blinker (oscillator - period 2)
    print("\nExample 2: Blinker (oscillates)")
    blinker = GameOfLife(7, 7, [(3,2), (3,3), (3,4)])
    run_simulation(blinker, max_steps=10)

    # Example 3: Glider (moves diagonally - hits border and dies)
    print("\nExample 3: Glider (with fixed borders - will eventually die)")
    glider_cells = [(1,0), (2,1), (0,2), (1,2), (2,2)]
    glider_fixed = GameOfLife(15, 15, glider_cells)
    run_simulation(glider_fixed, max_steps=40)

    # Bonus Example: Glider with expandable borders (keeps moving forever)
    print("\nBonus Example: Glider (expandable borders - moves forever)")
    glider_expand = ExpandableGameOfLife(glider_cells)
    run_simulation(glider_expand, max_steps=20)
