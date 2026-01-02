# Numerical Root Finding: The Companion Matrix Method

This module implements a generalized polynomial root finder. Unlike algebraic formulas (which only work for degrees $\le 4$), this method uses **Linear Algebra** to find the roots of a polynomial of any degree.

---

## 1. The Mathematical Logic

To find the roots of a polynomial:
$$P(x) = c_n x^n + c_{n-1} x_{n-1} + \dots + c_1 x + c_0 = 0$$

We construct a special square matrix known as the **Companion Matrix**. The fundamental property of this matrix is that its **characteristic polynomial** is exactly the same as the polynomial we are trying to solve. Therefore, the **eigenvalues** of the matrix are the roots of the equation.



---

## 2. The Implementation Steps

### A. Normalization
The code first divides all coefficients by the leading coefficient ($c_n$). This creates a **monic polynomial** where the highest degree term has a coefficient of 1, which is a requirement for the standard companion matrix.

### B. Matrix Construction
For a polynomial of degree $n$, the code builds an $n \times n$ matrix:
1.  The first row is populated with the negative of the normalized coefficients (excluding the leading term).
2.  A sub-diagonal of 1s (an identity matrix) is placed below the first row to create the structure.

$$
C = \begin{bmatrix} 
-c_{n-1} & -c_{n-2} & \dots & -c_0 \\
1 & 0 & \dots & 0 \\
0 & 1 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & 1 & 0 
\end{bmatrix}
$$

### C. Eigenvalue Calculation
The code uses `np.linalg.eigvals(companion)`. Since the roots of the polynomial are the values that make the determinant $|C - xI| = 0$, finding the eigenvalues is mathematically equivalent to finding the roots.

---

## 3. Key Features in the Code

| Feature | Logic |
| :--- | :--- |
| **Trailing Zero Removal** | Prevents errors if the user inputs high-degree coefficients that are actually zero. |
| **Degree 1 Handling** | Automatically switches to the linear solution ($x = -b/a$) for efficiency. |
| **Generality** | Can solve $x^2 + 1 = 0$ (Complex) just as easily as $x^3 - 6x^2 + 11x - 6 = 0$ (Real). |

---

## 4. Usage Example
To solve $x^3 - 6x^2 + 11x - 6 = 0$, input the coefficients from the **lowest degree to the highest**:
```python
coeffs = [-6, 11, -6, 1]
roots = root(coeffs)
# Output: [1, 2, 3] (approximate)
```

## 5. Technical Requirements

To ensure the `root(c)` function executes correctly, the following dependencies and environmental factors must be considered:

* **NumPy Library:** The algorithm relies heavily on `numpy` for:
    * **Matrix Manipulation:** Creating the $n \times n$ zero matrix and injecting the identity matrix.
    * **Linear Algebra Suite:** Utilizing `np.linalg.eigvals` to perform the complex iterative calculations required to find eigenvalues.
* **Complex Number Support:** * Since polynomials like $x^2 + 1 = 0$ do not have real roots, the output will often be returned as Python `complex` types (e.g., `0+1j`).
    * Numerical solvers often return tiny "imaginary" parts (like `1.2e-16j`) even for real roots due to floating-point precision; these should be interpreted as zero.
* **Computational Complexity:**
    * The eigenvalue approach generally has a complexity of $O(n^3)$. 
    * While highly stable for medium-sized polynomials, extremely high-degree polynomials may encounter numerical stability issues inherent to the Companion Matrix structure.


---

### Installation
Ensure you have the required dependency installed via pip:

```bash
pip install numpy
```


---

## General Polynomial Solving: The Companion Matrix (Alternative Formula)

While specific formulas exist for quadratic and cubic equations, solving higher-degree polynomials (degree 5 and above) often requires numerical linear algebra because no general radical formula exists (Abel-Ruffini Theorem).

### The Math: Companion Matrix Method
To find the roots of a polynomial $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$, the `np.roots` function constructs a **Companion Matrix** $C$:



$$C = \begin{bmatrix} 
-\frac{a_{n-1}}{a_n} & -\frac{a_{n-2}}{a_n} & \dots & -\frac{a_0}{a_n} \\
1 & 0 & \dots & 0 \\
0 & 1 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & 1 & 0 
\end{bmatrix}$$

The **eigenvalues** of this matrix are exactly the roots of the polynomial. By finding these eigenvalues, the code can solve polynomials of any degree, including those with complex roots like $x^2 + 1 = 0$.

---

## 📊 Final Master Summary: Computational Mathematics

This repository now provides a full suite of mathematical tools ranging from theoretical limits to practical numerical solvers.

| Topic | Concept | Method Used | Key Python Tool |
| :--- | :--- | :--- | :--- |
| **Information Theory** | Data Limits | Entropy & Shannon-Hartley | `math.log2` |
| **Statistics** | Hypothesis Testing | Z/T-Stats & P-Values | `np.std`, `math.erf` |
| **Calculus** | Rate of Change/Area | FTC & Riemann Sums | Step iteration ($h$) |
| **Basic Algebra** | Degree 2 & 3 | Quadratic & Cardano | `cmath` |
| **Linear Algebra** | Higher Degree | Companion Matrix | `np.roots` |

### Why use `np.roots` over `root2` or `root3`?
1. **Scalability:** `np.roots` can solve a polynomial of degree 10 or 100, whereas formulas only work for low degrees.
2. **Stability:** Numerical methods in NumPy are optimized to handle precision issues that manual formulas might struggle with in extreme cases.
3. **Versatility:** It automatically handles real and complex roots simultaneously.

---

## 🛠️ Installation & Requirements
To run the code in this repository, you will need:
* **Python 3.x**
* **NumPy:** Install via `pip install numpy`

```bash
# Example usage for polynomial solving
python your_script_name.py