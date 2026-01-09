import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # If items is None, use empty list
        self.items = items if items is not None else []
        self.page_size = int(page_size)  # Ensure it's an integer
        self.current_idx = 0  # Internal 0-based page index
        
        # Calculate total pages (0 if no items)
        if len(self.items) == 0:
            self.total_pages = 0
        else:
            self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """Return the items on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        """Go to a specific page (1-based indexing). Raises ValueError if invalid."""
        if not isinstance(page_num, int):
            raise ValueError("Page number must be an integer.")
        
        if page_num < 1 or (self.total_pages > 0 and page_num > self.total_pages):
            raise ValueError(f"Page {page_num} does not exist.")
        
        # Convert to 0-based index
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        """Go to the first page and return self for chaining."""
        self.current_idx = 0
        return self

    def last_page(self):
        """Go to the last page and return self for chaining."""
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """Go to the next page if possible and return self for chaining."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """Go to the previous page if possible and return self for chaining."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """Return string representation: visible items, each on a new line."""
        return "\n".join(str(item) for item in self.get_visible_items())


# --------------------- Test Cases ---------------------
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())
    # Expected: ['a', 'b', 'c', 'd']

    p.next_page()
    print(p.get_visible_items())
    # Expected: ['e', 'f', 'g', 'h']

    p.last_page()
    print(p.get_visible_items())
    # Expected: ['y', 'z']

    # Test method chaining (Bonus)
    print(p.first_page().next_page().next_page().next_page().get_visible_items())
    # Expected: ['m', 'n', 'o', 'p']

    # Test __str__
    p.first_page()
    print("Current page items:")
    print(p)
    # Expected:
    # a
    # b
    # c
    # d

    # Test error handling
    try:
        p.go_to_page(10)
    except ValueError as e:
        print(e)  # Expected: Page 10 does not exist.

    try:
        p.go_to_page(0)
    except ValueError as e:
        print(e)  # Expected: Page 0 does not exist.
