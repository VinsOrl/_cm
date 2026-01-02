# Mathematical Foundations & Computational Algorithms

This repository contains a collection of Python implementations for fundamental principles in Information Theory, Statistics, Calculus, and Algebra.

---

## 1. Information Theory
Based on the groundbreaking work of Claude Shannon, these principles define the limits of communication.

### Key Theorems
* **Shannon's Source Coding Theorem:** Establishes **Entropy ($H$)** as the fundamental limit for lossless data compression.
* **Shannon-Hartley Theorem:** Defines the maximum capacity ($C$) of a channel given bandwidth ($B$) and noise ($N$).
    $$C = B \log_2 \left( 1 + \frac{S}{N} \right)$$

### Metrics Comparison
| Metric | Formula | Intuition |
| :--- | :--- | :--- |
| **Entropy** | $H(X) = -\sum P(x) \log P(x)$ | Average uncertainty in a distribution. |
| **KL Divergence** | $D_{KL}(P \parallel Q)$ | Bits "wasted" using the wrong distribution. |
| **Mutual Info** | $I(X;Y) = H(X) - H(X|Y)$ | Information shared between two variables. |



---

## 2. Probability & Statistics
This section implements hypothesis testing from scratch using the "Signal-to-Noise" logic.

### Implemented Tests
1.  **One-Sample Z-Test:** Used when population variance ($\sigma$) is known.
2.  **One-Sample T-Test:** Used when $\sigma$ is unknown; uses sample standard deviation with **Bessel's Correction** ($n-1$).
3.  **Independent T-Test:** Compares two different groups (supports Pooled and Welch’s methods).
4.  **Paired T-Test:** Compares "Before" and "After" states of the same group.

### The Math of Significance
All tests calculate a test statistic:
$$\text{Statistic} = \frac{\text{Observed Difference}}{\text{Standard Error}}$$
The **P-value** is derived using the Error Function (`math.erf`) for Z-tests to determine if we reject the Null Hypothesis ($H_0$).



---

## 3. Numerical Calculus
Demonstrating the **Fundamental Theorem of Calculus (FTC)** via numerical approximation.

### Differentiation & Integration
* **Derivative:** Approximated using a small step $h = 10^{-5}$.
    $$f'(x) \approx \frac{f(x + h) - f(x)}{h}$$
* **Integration:** Calculated via Riemann Sums (Area under the curve).
    $$\int_a^b f(x)dx \approx \sum f(x) \cdot h$$

### The Theorem
The code proves that $\frac{d}{dx} \int_a^x f(t)dt = f(x)$. By taking the derivative of an integral, we return to the original function.



---

## 4. Advanced Algebra: Root Finding
Analytical solutions for polynomial equations using complex number arithmetic (`cmath`).

### Quadratic Equations ($ax^2 + bx + c = 0$)
Solved using the standard Quadratic Formula. The **Discriminant** ($D = b^2 - 4ac$) determines if roots are real or complex.

### Cubic Equations ($ax^3 + bx^2 + cx + d = 0$)
Solved using **Cardano’s Method**. 
1.  The equation is "depressed" to remove the $x^2$ term.
2.  The solution utilizes the complex cube roots of unity ($\omega$).
3.  Results are shifted back to find the three final roots.



---

## 5. Summary of Implementation Tools

| Module | Python Library | Core Logic |
| :--- | :--- | :--- |
| **Statistics** | `numpy`, `math` | Bessel's correction, Error function. |
| **Calculus** | Native Python | Step-based iteration ($h=0.00001$). |
| **Algebra** | `cmath` | Complex square/cube roots, `isclose` validation. |

### Note on Floating Point Precision
Since computers cannot represent infinite decimals, we use `cmath.isclose()` to verify results. For example, instead of checking `if result == 0`, we check if `abs(result) < 1e-9`.