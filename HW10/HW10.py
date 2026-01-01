import cmath
import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    """1. Forward Transform (DFT)"""
    N = len(x)
    X = []
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            # Formula: f(x) * e^(-i * 2 * pi * k * n / N)
            angle = -2j * cmath.pi * k * n / N
            sum_val += x[n] * cmath.exp(angle)
        X.append(sum_val)
    return X

def idft(X):
    """2. Inverse Transform (IDFT)"""
    N = len(X)
    x = []
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            # Formula: F(w) * e^(i * 2 * pi * k * n / N)
            angle = 2j * cmath.pi * k * n / N
            sum_val += X[k] * cmath.exp(angle)
        # Normalization by 1/N
        x.append(sum_val / N)
    return x

# --- 3. Verification ---

# Create a sample signal f: a simple sine wave
t = np.linspace(0, 1, 100)
f_original = np.sin(2 * np.pi * 5 * t)  # 5Hz signal

# Step 1: Forward Transform
F_transformed = dft(f_original)

# Step 2: Inverse Transform
f_recovered = idft(F_transformed)

# Convert recovered signal to real numbers (imaginary parts should be near zero)
f_recovered_real = [val.real for val in f_recovered]

# Check if they are the same (Verification)
print(f"Max difference: {np.max(np.abs(f_original - f_recovered_real))}")

# Visualizing the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, f_original, label="Original Signal f(x)")
plt.title("Original Signal")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, f_recovered_real, label="Recovered Signal (IDFT(DFT(f)))", color='orange', linestyle='--')
plt.title("Verified Recovered Signal")
plt.legend()

plt.tight_layout()
plt.show()