## Algebra: The Quadratic Formula and Complex Roots

The `root2` function solves for $x$ in the standard quadratic equation:
$$ax^2 + bx + c = 0$$

### The Mathematics
To find the roots, we use the **Quadratic Formula**:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### The Discriminant ($\Delta$)
The value inside the square root, $D = b^2 - 4ac$, is called the **discriminant**. It determines the nature of the roots:
* **$D > 0$:** Two distinct real roots.
* **$D = 0$:** One repeated real root.
* **$D < 0$:** Two complex conjugate roots (involving the imaginary unit $i$).



### Implementation Details
1.  **`cmath.sqrt(D)`:** Unlike the standard `math` library, `cmath` handles negative discriminants by returning complex numbers (e.g., `(0+2j)`).
2.  **The `a == 0` Guard:** If $a=0$, the equation becomes linear ($bx + c = 0$), and the quadratic formula would result in a division-by-zero error.
3.  **Numerical Validation:** The code uses `cmath.isclose(f(r1), 0)` to verify the result. Because of floating-point precision errors in computers, we check if the result is *almost* zero rather than *exactly* zero.

---

## 🚀 Final Summary of Capabilities

This project now covers a wide spectrum of mathematical computation:

| Domain | Key Concept | Python Tool |
| :--- | :--- | :--- |
| **Information Theory** | Entropy & Channel Capacity | Logarithmic modeling of data |
| **Statistics** | Z-Test & T-Tests | Hypothesis testing via `np.std` and `erf` |
| **Calculus** | Derivatives & Integrals | Numerical approximation with small $h$ |
| **Algebra** | Quadratic Solver | Complex number handling with `cmath` |