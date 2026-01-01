import numpy as np
import sympy as sp

def solve_ode_general(coefficients):
    t = sp.symbols('t')
    
    # 1. Find the roots of the characteristic equation
    # np.roots expects coefficients in order of descending powers
    roots = np.roots(coefficients)
    
    # 2. Group roots by value to handle multiplicities
    unique_roots = {}
    for r in roots:
        # Rounding to handle floating point precision issues
        r_rounded = round(complex(r).real, 6) + round(complex(r).imag, 6) * 1j
        unique_roots[r_rounded] = unique_roots.get(r_rounded, 0) + 1

    general_solution = 0
    constant_index = 1

    # 3. Construct the solution terms
    for root, multiplicity in unique_roots.items():
        real_part = float(root.real)
        imag_part = float(root.imag)

        for k in range(multiplicity):
            C = sp.symbols(f'C{constant_index}')
            
            if abs(imag_part) < 1e-6:
                # Real Root Case: C * t^k * e^{rt}
                term = C * (t**k) * sp.exp(real_part * t)
                general_solution += term
                constant_index += 1
            elif imag_part > 0:
                # Complex Root Case: e^{at} * (C1 cos(bt) + C2 sin(bt))
                # We only process the positive imaginary part to handle the pair (a +/- bi)
                C_cos = sp.symbols(f'C{constant_index}')
                C_sin = sp.symbols(f'C{constant_index + 1}')
                
                term = (t**k) * sp.exp(real_part * t) * \
                       (C_cos * sp.cos(imag_part * t) + C_sin * sp.sin(imag_part * t))
                
                general_solution += term
                constant_index += 2
                
    return sp.simplify(general_solution)

# Example usage for y'' - 4y' + 4y = 0:
# sol = solve_ode_general([1, -4, 4])
# print(f"y(t) = {sol}")