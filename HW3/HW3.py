import cmath

def root3(a, b, c, d):
    if a == 0:
        raise ValueError("a cannot be 0 (not a cubic equation).")

    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    Δ = (q/2)**2 + (p/3)**3

    omega = complex(-0.5, cmath.sqrt(3)/2)
    roots = []

    if cmath.isclose(Δ, 0, rel_tol=1e-12, abs_tol=0.0):

        u = (-q/2)**(1/3) if q != 0 else 0
        t1 = 2*u
        t2 = -u
        roots = [t1, t2, t2]
    else:
        sqrtΔ = cmath.sqrt(Δ)
        u = (-q/2 + sqrtΔ)**(1/3)
        v = (-q/2 - sqrtΔ)**(1/3)
        t1 = u + v
        t2 = u*omega + v*omega.conjugate()
        t3 = u*omega.conjugate() + v*omega
        roots = [t1, t2, t3]

    shift = -b / (3*a)
    roots = [t + shift for t in roots]


    def f(x): return a*x**3 + b*x**2 + c*x + d
    roots_with_check = [(r, cmath.isclose(f(r), 0, rel_tol=1e-9, abs_tol=0.0)) for r in roots]

    return roots_with_check

print("Equation: x^3 - 6x^2 + 11x - 6 = 0 (roots: 1, 2, 3)")
print(root3(1, -6, 11, -6))
