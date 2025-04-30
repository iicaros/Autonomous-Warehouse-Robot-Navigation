# Matrix Class from Problem 3
class Matrix:                                                               
    def __init__(self, rows, cols, elements):
        if len(elements) != rows or any(len(row) != cols for row in elements):
            raise ValueError("Dimensions aren't consistent.")                       
        

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

# ///////////////////////////////////////////////////////////////////////////////// #


class SquareMatrix(Matrix):                                 # Square Matrix class that inherits from the Matrix class
    def __init__(self, size, elements):
        super().__init__(size, size, elements)              # Calls the parent class


sqmatrix = SquareMatrix(2, [[1, 2], [3, 4]])                # Creates matrix, only has space for ONE value that sets the rows and columns

sqmatrix.display()                                          # Display matrix from parent class

print("\nElement at (1,1):", sqmatrix.get_element(1, 1))    # Output: 4

print("\n")                                                 # Formatting

sqmatrix.set_element(0, 1, 9)                               # Set element from parent class
sqmatrix.display()