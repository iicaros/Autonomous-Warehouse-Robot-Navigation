import random

def find_peak(matrix, left, right, top, bottom):
    
    # Find the middle column
    mid_col = (left + right) // 2
    
    max_row = top
    max_value = matrix[top][mid_col]
    
    for i in range(top, bottom + 1):
        if matrix[i][mid_col] > max_value:
            max_value = matrix[i][mid_col]
            max_row = i
    
    left_neighbor = matrix[max_row][mid_col - 1] if mid_col - 1 >= left else float('-inf')                                      # Check neighbors
    right_neighbor = matrix[max_row][mid_col + 1] if mid_col + 1 <= right else float('-inf')
    up_neighbor = matrix[max_row - 1][mid_col] if max_row - 1 >= top else float('-inf')
    down_neighbor = matrix[max_row + 1][mid_col] if max_row + 1 <= bottom else float('-inf')
    
    if max_value >= left_neighbor and max_value >= right_neighbor and max_value >= up_neighbor and max_value >= down_neighbor:  # Checks if current element is a peak
        return max_value
    
    if left_neighbor > right_neighbor:
        return find_peak(matrix, left, mid_col - 1, top, bottom)
    else:
        return find_peak(matrix, mid_col + 1, right, top, bottom)

def main():
    rows = int(input("Enter the number of rows: "))                                        # User Defined Matrix Size
    cols = int(input("Enter the number of columns: "))

    # Random Matrix Value Generation
    matrix = [[random.randint(0, 99) for _ in range(cols)] for _ in range(rows)]

    print("Generated Matrix:")
    for row in matrix:
        print(row)
    
    try:                                                                                   # Divide and Conquer to find a single peak
        peak = find_peak(matrix, 0, cols - 1, 0, rows - 1)
        print("\nA peak element is:", peak)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
