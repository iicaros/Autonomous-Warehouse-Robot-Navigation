class Matrix:
    def __init__(self, rows, cols, elements):
        if len(elements) != rows or any(len(row) != cols for row in elements):
            raise ValueError("Dimensions aren't consistent.")                       # stops the creation of matrices with blank elements
        

        self.rows = rows
        self.cols = cols
        self.data = elements

    def get_element(self, row, col):
        return self.data[row][col]
    

    def set_element(self, row, col, val):
        self.data[row][col] = val

    def display(self):
        for row in self.data:
            print(row)

# Matrix(len, height, [row 1], [row 2], ...)                        Matrix Creation
m1 = Matrix(2, 2, [[1, 2], [3, 4]])

m1.display()                                                      # Displaying Matrix in terminal


print(f"\nElement at (0,0): {m1.get_element(0,0)}\n")             # Data retrieval

# set_element(row, col, val)
m1.set_element(0, 0, 100)                                         # Set Element
m1.display()                                                      # Display updated matrix

print("\n")
m2 = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])              # Make more matrices using class definition
m2.display()