# Student Introduction
**Student Name:** 林新興  
**Student ID:** 111210556  
**Subject:** Math and Coding

---

## HW 1 - Calculus: The Fundamental Theorem (FTC)


The code implements a numerical simulation of the **Fundamental Theorem of Calculus, Part 1**. This theorem bridges the gap between the slope of a curve (differentiation) and the area under a curve (integration).

### The Math: Derivative and Integral
The code defines these operations using numerical approximation:

1. **The Derivative (Limit Definition):** $f'(x) \approx \frac{f(x + h) - f(x)}{h}$
2. **The Integral (Riemann Sum):** $\int_{a}^{b} f(x) dx \approx \sum_{i} f(x_i) \Delta x$

### The Fundamental Theorem of Calculus (Theorem 1)
If we define a function as the area under a curve, the rate at which that area grows is equal to the value of the curve itself:
$$\frac{d}{dx} \left( \int_{a}^{x} f(t) dt \right) = f(x)$$

---

## HW 2 - Algebra: The Quadratic Formula and Complex Roots


The project solves for $x$ in the standard quadratic equation $ax^2 + bx + c = 0$.

### The Mathematics
To find the roots, we use the **Quadratic Formula**:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

* **Discriminant ($D = b^2 - 4ac$):** Determines if roots are real or complex.
* **Complex Handling:** Uses `cmath.sqrt(D)` to handle negative discriminants.
* **Numerical Validation:** Uses `cmath.isclose()` to verify results against floating-point errors.

---

## HW 3 - Mathematical Foundations & Computational Algorithms


### 1. Information Theory
Based on Shannon's principles:
* **Entropy ($H$):** The average uncertainty in a distribution.
* **Channel Capacity ($C$):** $C = B \log_2 \left( 1 + \frac{S}{N} \right)$.

### 2. Probability & Statistics
* **Tests Implemented:** One-Sample Z-Test, One-Sample T-Test, Independent T-Test, and Paired T-Test.
* **Logic:** $\text{Statistic} = \frac{\text{Observed Difference}}{\text{Standard Error}}$.

---

## HW 4 - Numerical Root Finding: The Companion Matrix Method


Generalized root finding using **Linear Algebra** for polynomials where $P(x) = 0$.

### The Companion Matrix ($C$)
The **eigenvalues** of the matrix are the roots of the equation:
$$
C = \begin{bmatrix} 
-\frac{c_{n-1}}{c_n} & -\frac{c_{n-2}}{c_n} & \dots & -\frac{c_0}{c_n} \\
1 & 0 & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots 
\end{bmatrix}
$$

---

## HW 5 - Finite Field Arithmetic (Galois Field $GF(p)$)


Arithmetic operations performed within a finite set $\{0, 1, \dots, p-1\}$ modulo a prime $p$.

### Key Operations
* **Closure:** All operations map back into the field.
* **Multiplicative Inverse:** Found via **Fermat’s Little Theorem**:
  $$a^{-1} \equiv a^{p-2} \pmod p$$
* **Applications:** Used in Cryptography (AES, RSA) and Error Correction.

---

## HW 6 - Mathematics Behind the Programs (Geometry)


### Geometric Intersections
* **Line-Line:** Solved using **Cramer's Rule**.
* **Circle-Circle:** Found by calculating the common chord line and its intersection with the circles.
* **Line-Circle:** Solved via quadratic substitution into the circle equation.

### Transformations
* **Translation:** $x' = x + dx, y' = y + dy$.
* **Scaling:** $x' = s \cdot x, y' = s \cdot y$.
* **Rotation:** $x' = x\cos\theta - y\sin\theta, y' = x\sin\theta + y\cos\theta$.

---

## HW 7 - Probability and Statistics: Principles


### Significance Testing
* **Z-Test:** Population $\sigma$ is known.
* **T-Test:** Population $\sigma$ is unknown; uses sample standard deviation $s$ with Bessel's Correction ($n-1$).
* **P-value:** Calculated using the Error Function ($\text{erf}$) to determine statistical significance.

---

## HW 8 - Information Theory & Coding Toolkit


### Coding Limits
* **Log-Space:** Calculations are done in $\log_2$ to prevent arithmetic underflow and represent data in **bits**.
* **Shannon-Hartley:** Defines the physical bit rate limit based on Bandwidth and SNR.

### Error Correction
* **Hamming (7,4):** Adds 3 parity bits to 4 data bits to detect and correct single-bit corruptions.

---

## HW 9 - Linear Algebra Lab: Concepts and Implementations


### Matrix Decompositions
* **LU Decomposition:** Factors $A = LU$ to solve systems and find determinants efficiently.
* **Eigen-Decomposition:** Decomposes a matrix into eigenvectors ($V$) and eigenvalues ($\Lambda$).
* **SVD & PCA:** $A = U \Sigma V^T$. Principal Component Analysis uses SVD on centered data for dimensionality reduction.

---

## HW 10 - Fourier Transform: Theory and Principles


### Transforming Domains
* **Forward Fourier Transform:** Decomposes a Time Domain signal $f(x)$ into Frequency Domain $F(\omega)$:
  $$F(\omega) = \int_{-\infty}^{\infty} f(x) e^{-i\omega x} dx$$
* **Inverse Fourier Transform:** Reconstructs the signal using a normalization factor of $1/2\pi$:
  $$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega x} d\omega$$

---

## HW 11 - ODE-to-RISC-V Compiler: Project Documentation Explanation


### Objective
A compiler pipeline that translates Ordinary Differential Equations (ODEs) into RISC-V assembly for high-performance hardware execution.

### The Process
1. **Lexer:** Scans input strings (e.g., `solve_ode {1, -3, 2}`) into tokens.
2. **Math Engine:** Solves the **Characteristic Equation** $a_n r^n + \dots + a_0 = 0$ to find system behavior.
3. **Code Generator:** Maps mathematical solutions (Real, Repeated, or Complex roots) directly to RISC-V assembly instructions.

---

## Technical Requirements


* **Python 3.x**
* **NumPy:** `pip install numpy`
* **Standard Libraries:** `math`, `cmath`, `os`

## References Link
* [HW 1](https://github.com/VinsOrl/_cm/blob/master/HW1/README.md) use Gemini
* [HW 2](https://github.com/VinsOrl/_cm/blob/master/HW2/README.md) use Gemini
* [HW 3](https://github.com/VinsOrl/_cm/blob/master/HW3/README.md) use Gemini
* [HW 4](https://github.com/VinsOrl/_cm/blob/master/HW4/README.md) use Gemini
* [HW 5](https://github.com/VinsOrl/_cm/blob/master/HW5/README.md) use Gemini
* [HW 6](https://github.com/VinsOrl/_cm/blob/master/HW6/README.md) use Gemini
* [HW 7](https://github.com/VinsOrl/_cm/blob/master/HW7/README.md)use Gemini
* [HW 8](https://github.com/VinsOrl/_cm/blob/master/HW8/README.md) use Gemini
* [HW 9](https://github.com/VinsOrl/_cm/blob/master/HW9/README.md) use Gemini
* [HW 10](https://github.com/VinsOrl/_cm/blob/master/HW10/README.md) use Gemini
* [HW 11](https://github.com/VinsOrl/_cm/blob/master/HW11/README.md) use Gemini

## Mid-Term Project : Implementation of Blackhole 
More about Implementation of Blackhole and docomentation
* [Python Implementation](https://github.com/VinsOrl/_cm/blob/master/MIDTERM/project.py)
* [Brief Introduction](https://github.com/VinsOrl/_cm/blob/master/MIDTERM/README.md)
* [AI Documentation](https://gemini.google.com/share/22d3f5c67f33)

---