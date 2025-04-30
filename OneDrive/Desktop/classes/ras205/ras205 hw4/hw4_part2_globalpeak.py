import random

def print_row_max(matrix):
    row_maxima = []
    for i, row in enumerate(matrix):
        max_value = max(row)                                                                    # Find the max value in each row
        row_maxima.append(max_value)
        print(f"Max of row {i}: {max_value}")
    return row_maxima

def find_global_peak(row_maxima):
    return max(row_maxima)

def count_peaks(matrix, peak_value):
    count = 0
    for row in matrix:
        count += row.count(peak_value)
    return count

rows = int(input("Enter the number of rows: "))                                                 # User Defined Matrix Size
cols = int(input("Enter the number of columns: "))

matrix = [[random.randint(0, 99) for _ in range(cols)] for _ in range(rows)]                    # Random Matrix Value Generation

print("Generated Matrix:")
for row in matrix:
    print(row)

row_maxima = print_row_max(matrix)                                                              # Prints the maximum value in each row

try:                                                                                            # Finds the global peak by comparing the row maxima
    global_peak = find_global_peak(row_maxima)
    print("\nThe global peak from the row maxima is:", global_peak)
    
    peak_count = count_peaks(matrix, global_peak)                                               # Exception handling for peaks appearing more than one time (Guarantee a test case by making a 100 x 100 matrix)
    print(f"The global peak value {global_peak} appears {peak_count} times in the matrix.")
    
except Exception as e:
    print(f"An error occurred: {e}")
