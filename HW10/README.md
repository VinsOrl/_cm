# Fourier Transform: Theory and Principles

This project implements the mathematical transformations required to transition between the Time Domain and the Frequency Domain.

## 1. The Mathematical Foundation

The project is built upon the two core equations for the Fourier Transform:

### Forward Fourier Transform
Used to decompose a signal into its constituent frequencies (the "analysis" step).
$$F(\omega) = \int_{-\infty}^{\infty} f(x) e^{-i\omega x} dx$$



### Inverse Fourier Transform
Used to reconstruct the original signal by summing up all the frequency components (the "synthesis" step).
$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega x} d\omega$$

---

## 2. Conceptual Summary

To understand how the transformation works, we can categorize the components as follows:

| Concept | Description |
| :--- | :--- |
| **$f(x)$** | **The "Input"** — The raw signal (e.g., sound or light). |
| **$e^{-i\omega x}$** | **The "Probe"** — A complex wave used to scan for specific frequencies. |
| **$F(\omega)$** | **The "Recipe"** — A list of how much of each frequency is needed. |
| **The Integral** | **The "Totaling"** — Summing up all contributions to find the final value. |

---

## 3. Variable Breakdown

Based on the assignment requirements, the variables are defined as:

* **$f(x)$**: The original function or signal in the **Time Domain**.
* **$F(\omega)$**: The resulting function in the **Frequency Domain**.
* **$e^{-i\omega x}$**: The complex exponential term that represents the frequency "spinning" in the complex plane.
* **$\omega$**: The angular frequency.
* **$1/2\pi$**: The normalization factor required for the Inverse Transform to return the signal to its original scale.



---

## 4. Key Logic & Verification

The project follows a three-step validation process:

1.  **Forward Transform (`dft`)**: Transform a sample function $f$ into its frequency representation $F(\omega)$.
2.  **Inverse Transform (`idft`)**: Apply the inverse formula to $F(\omega)$ to attempt to recover the original function.
3.  **Verification**: Confirm that the recovered function is identical to the original input $f$.