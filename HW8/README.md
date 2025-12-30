# Information Theory & Coding Toolkit

This project is a comprehensive Python implementation of the core principles of Information Theory, based on the fundamental work of Claude Shannon. It covers everything from probability distributions to channel capacity limits and error-correction codes.

---

## 📋 Table of Contents
* [1. Probability & Logarithmic Scaling](#1-probability--logarithmic-scaling)
* [2. Information Metrics (Entropy & KL Divergence)](#2-information-metrics)
* [3. Shannon's Channel Coding Theorem](#3-shannons-channel-coding-theorem)
* [4. Shannon–Hartley Theorem](#4-shannon-hartley-theorem)
* [5. Forward Error Correction (Hamming 7,4)](#5-forward-error-correction)

---

## 1. Probability & Logarithmic Scaling
When dealing with long sequences of events (e.g., 10,000 coin flips), direct probability calculation results in numbers so small ($0.5^{10000}$) that computers suffer from **arithmetic underflow**.

* **Solution:** We perform calculations in "log-space."
* **Formula:** $\log(p^n) = n \cdot \log(p)$
* **Unit:** When using $\log_2$, the resulting unit is **bits**.

## 2. Information Metrics
The project implements three primary ways to measure information and the "distance" between distributions:

| Metric | Formula | Description |
| :--- | :--- | :--- |
| **Entropy $H(P)$** | $-\sum P(x) \log P(x)$ | The average uncertainty/surprise in a source. |
| **Cross-Entropy** | $-\sum P(x) \log Q(x)$ | The cost of using the "wrong" distribution $Q$ to encode $P$. |
| **KL Divergence** | $\sum P(x) \log \frac{P(x)}{Q(x)}$ | The extra bits wasted by assuming $Q$ when the truth is $P$. |

## 3. Shannon's Channel Coding Theorem
This theorem is the "Proof of Possibility." It defines the ultimate limit for reliable communication in a noisy environment.



* **The Bound:** Every channel has a capacity $C$.
* **The Rule:** As long as your transmission rate $R$ is less than $C$, you can achieve a **zero error rate** using a clever enough code.
* **Significance:** It proves that noise does not limit *accuracy*, only *speed*.

## 4. Shannon–Hartley Theorem
While the Coding Theorem says a limit exists, the Shannon-Hartley theorem calculates exactly what that limit is for a physical channel (like a Wi-Fi signal or a fiber optic cable).

### The Formula
$$C = B \log_2(1 + \frac{S}{N})$$



* **$C$ (Capacity):** Maximum theoretical bit rate.
* **$B$ (Bandwidth):** The "width" of the frequency pipe (in Hz).
* **$S/N$ (SNR):** Signal-to-Noise Ratio. 

**Real-world intuition:** If you want faster internet, you must either increase the bandwidth (wider frequency) or improve the signal strength relative to the noise.

## 5. Forward Error Correction (Hamming 7,4)
To reach the reliability promised by Shannon, we use **Error Correcting Codes (ECC)**. This project implements the **Hamming (7,4)** code.

* **How it works:** It takes 4 data bits and adds 3 parity bits to create a 7-bit block.
* **The Benefit:** If any **one bit** is flipped (corrupted) during transmission, the algorithm can detect exactly which bit is wrong and flip it back to the correct state automatically.

---

## 🛠️ Usage
1. Ensure you have `numpy` installed: `pip install numpy`.
2. Run the implementation script:
   ```bash
   python information_theory_project.py