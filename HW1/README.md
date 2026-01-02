## Calculus: The Fundamental Theorem (FTC)

The code implements a numerical simulation of the **Fundamental Theorem of Calculus, Part 1**. This theorem bridges the gap between the slope of a curve (differentiation) and the area under a curve (integration).

### The Math: Derivative and Integral
The code defines these operations using numerical approximation:

1. **The Derivative (Limit Definition):**
   Approximated using a small step $h$:
   $$f'(x) \approx \frac{f(x + h) - f(x)}{h}$$

2. **The Integral (Riemann Sum):**
   Approximated by summing the areas of infinite tiny rectangles:
   $$\int_{a}^{b} f(x) dx \approx \sum_{i} f(x_i) \Delta x$$



---

### The Fundamental Theorem of Calculus (Theorem 1)
The core of your `theorem1` function tests the following principle:
> If we define a function as the area under a curve, the rate at which that area grows is equal to the value of the curve itself.

Mathematically:
$$\frac{d}{dx} \left( \int_{a}^{x} f(t) dt \right) = f(x)$$

### Code Logic Explained
* **`df` function:** Calculates the instantaneous slope at point $x$.
* **`integral` function:** Uses the "Rectangle Method" to accumulate area from point $a$ to $b$.
* **`theorem1(f, x)`:** 1. It creates an "Area Function" $F(x) = \int_0^x f(t) dt$.
   2. It takes the derivative of that area function.
   3. It asserts that the result is equal to the original function $f(x)$.



### Why $h = 0.00001$?
In calculus, $h$ should approach zero ($h \to 0$). In computing, we cannot use zero (it would cause a division by zero error), so we use a very small number. This creates a **Numerical Approximation**.
* If $h$ is too large, the error is high.
* If $h$ is too small, the computer may encounter "floating-point errors."

---

## Final Summary Table: Mathematics in the Code

| Concept | Python Implementation | Mathematical Name |
| :--- | :--- | :--- |
| **Slope** | `(f(x+h)-f(x))/h` | First Principle Derivative |
| **Area** | `area += f(x)*h` | Left-hand Riemann Sum |
| **FTC** | `df(lambda x: integral(f,0,x), x)` | Fundamental Theorem of Calculus |
| **Standard Error** | `pop_std / np.sqrt(n)` | Central Limit Theorem Application |