def harmonic_series(n):
    total = 0
    for i in range(1, n + 1):
        total += 1/i
    return total


n = 10
print(f"For n = {n}, Harmonic Sum = {harmonic_series(n)}")
n = 100
print(f"For n = {n}, Harmonic Sum = {harmonic_series(n)}")
n = 1000
print(f"For n = {n}, Harmonic Sum = {harmonic_series(n)}")