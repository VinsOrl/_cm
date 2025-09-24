import numpy as np

def solve_polynomial_roots(coefficients):
    # The numpy.roots function directly implements the companion matrix method.
    roots = np.roots(coefficients)
    
    return roots

# Example 1: A simple quadratic equation
# x^2 - 5x + 6 = 0  --> roots are 2 and 3
coeffs1 = [1, -5, 6]
roots1 = solve_polynomial_roots(coeffs1)
print(f"Roots of x^2 - 5x + 6 = 0 are: {roots1}")
print("-" * 30)

# Example 2: A cubic equation
# x^3 - 6x^2 + 11x - 6 = 0  --> roots are 1, 2, and 3
coeffs2 = [1, -6, 11, -6]
roots2 = solve_polynomial_roots(coeffs2)
print(f"Roots of x^3 - 6x^2 + 11x - 6 = 0 are: {roots2}")
print("-" * 30)

# Example 3: A polynomial with complex roots
# x^2 + 1 = 0 --> roots are i and -i
coeffs3 = [1, 0, 1]
roots3 = solve_polynomial_roots(coeffs3)
print(f"Roots of x^2 + 1 = 0 are: {roots3}")