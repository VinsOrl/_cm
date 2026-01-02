# Probability and Statistics: The Mathematical Principles

This document explains the mathematical formulas and logic used in the accompanying Python implementation of fundamental statistical tests.

---

## 1. One-Sample Z-Test
The Z-test is used to determine whether a sample mean is significantly different from a known population mean when the **population standard deviation ($\sigma$) is known**.

### The Math
The Z-statistic represents the "Signal-to-Noise" ratio.
$$z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$$

| Symbol | Definition |
| :--- | :--- |
| $\bar{x}$ | Sample Mean |
| $\mu$ | Population Mean |
| $\sigma$ | Population Standard Deviation |
| $n$ | Sample Size |

**Note on P-value:** In the code, we use the error function (`math.erf`) to calculate the area under the Normal Distribution curve.

---

## 2. One-Sample T-Test
Used when the **population standard deviation is unknown**. We estimate it using the sample standard deviation ($s$).

### The Math
$$t = \frac{\bar{x} - \mu}{s / \sqrt{n}}$$

Where $s$ is calculated using **Bessel's Correction** ($n-1$) to ensure an unbiased estimate:
$$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}$$



---

## 3. Independent Two-Sample T-Test
Used to compare the means of two independent groups (e.g., Treatment vs. Control).

### Case A: Equal Variance (Student's T-Test)
If we assume both groups have the same variance, we calculate a **Pooled Variance** ($s_p^2$):
$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

The test statistic is:
$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2 (\frac{1}{n_1} + \frac{1}{n_2})}}$$

### Case B: Unequal Variance (Welch's T-Test)
If variances are unequal, we do not pool them:
$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

---

## 4. Paired T-Test
Used when comparing the same group at two different times (e.g., Before vs. After treatment).

### The Math
This test is mathematically equivalent to a **One-Sample T-test performed on the differences ($d$)** between pairs.

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$

Where:
* $d_i = x_{after, i} - x_{before, i}$
* $\bar{d}$ is the average difference.
* $s_d$ is the standard deviation of the differences.

---

## Summary Table: Which test to use?

| Scenario | Known Population $\sigma$? | Test Type |
| :--- | :--- | :--- |
| Single group vs. Constant | Yes | **Z-Test** |
| Single group vs. Constant | No | **One-Sample T-Test** |
| Two independent groups | No | **Independent T-Test** |
| Same group (Before/After) | No | **Paired T-Test** |

---

## 5. Interpreting the Results: Hypothesis Testing

Statistical tests are designed to help us choose between two competing statements:

1.  **Null Hypothesis ($H_0$):** There is no effect or no difference (e.g., the sample mean equals the population mean).
2.  **Alternative Hypothesis ($H_1$):** There is a significant difference.

### The P-Value Logic
The P-value is the probability of obtaining results at least as extreme as the observed results, assuming the Null Hypothesis is **true**.

* **$P \le \alpha$ (usually 0.05):** Reject $H_0$. The result is "Statistically Significant."
* **$P > \alpha$:** Fail to reject $H_0$. The result is not significant.

### Visualizing the Rejection Region
In your `z_test_scratch` function, the `p_value` is calculated for a **two-tailed test**. This means we are checking for differences in both directions (much higher OR much lower).

---

## 6. Mathematical Implementation Details

### Why use `math.erf`?
In your code, you use:
`p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z_stat) / math.sqrt(2))))`

This is the mathematical way to calculate the area under the **Normal Distribution** curve. Because the Normal Distribution has no simple algebraic integral, we use the **Error Function (erf)**, which is defined as:
$$\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt$$

### Degrees of Freedom (df)
While your Z-test uses the standard normal curve, the T-tests rely on the **T-distribution**. The shape of this distribution changes based on the "Degrees of Freedom":
* **One-Sample/Paired T-test:** $df = n - 1$
* **Independent T-test (Equal Var):** $df = n_1 + n_2 - 2$



As $df$ increases (sample size gets larger), the T-distribution becomes identical to the Z-distribution (Normal distribution).