def harmonic_number(n):
    if n < 1:   
        raise ValueError("Input must be a positive integer.")       # Cant have negative harmonic sums
    return sum(1 / i for i in range(1, n + 1))
try:
    n = int(input("Enter a positive integer for n: "))
    result = harmonic_number(n)
    print(f"The {n}th harmonic number is: {result}")
except ValueError:
    print("Please enter a valid positive integer.")