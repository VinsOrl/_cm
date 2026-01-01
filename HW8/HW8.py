import math
import numpy as np

# 1. & 2. Probability and Logarithmic Probability
def calculate_coin_probabilities(n=10000, p=0.5):
    # Direct calculation (will likely result in 0.0 due to underflow)
    direct_prob = p**n
    
    # Log-space calculation: log(p^n) = n * log(p)
    # Using log2 for bits (common in Info Theory) or log10/ln
    log_prob = n * math.log2(p)
    
    return direct_prob, log_prob

# 3. & 4. Information Metrics
def information_metrics(p_dist, q_dist):
    p = np.array(p_dist)
    q = np.array(q_dist)
    epsilon = 1e-12  # To avoid log(0)
    
    # Entropy: H(P)
    entropy = -np.sum(p * np.log2(p + epsilon))
    
    # Cross Entropy: H(P, Q)
    cross_ent = -np.sum(p * np.log2(q + epsilon))
    
    # KL Divergence: D_KL(P || Q)
    kl_div = np.sum(p * np.log2((p + epsilon) / (q + epsilon)))
    
    return entropy, cross_ent, kl_div

# 5. Hamming (7,4) Code Implementation
class Hamming74:
    def encode(self, data_bits):
        """Encodes 4 bits into 7 bits."""
        d1, d2, d3, d4 = data_bits
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4
        return [p1, p2, d1, p3, d2, d3, d4]

    def decode(self, received):
        """Decodes 7 bits and corrects single-bit errors."""
        r = received
        s1 = r[0] ^ r[2] ^ r[4] ^ r[6]
        s2 = r[1] ^ r[2] ^ r[5] ^ r[6]
        s3 = r[3] ^ r[4] ^ r[5] ^ r[6]
        
        error_pos = s1 + (s2 * 2) + (s3 * 4)
        if error_pos != 0:
            print(f"Error detected at position: {error_pos}")
            received[error_pos - 1] ^= 1  # Correct bit
            
        return [received[2], received[4], received[5], received[6]]

# --- Execution and Demonstration ---

# Task 1 & 2
prob, log_prob = calculate_coin_probabilities()
print(f"1. Direct Probability (0.5^10000): {prob}")
print(f"2. Log Probability (log2): {log_prob} bits")

# Task 3 & 4
p = [0.5, 0.5]
q = [0.8, 0.2]
h, cross, kl = information_metrics(p, q)
h_pp, cross_pp, _ = information_metrics(p, p)

print(f"\n3. Metrics for P{p} and Q{q}:")
print(f"   Entropy H(P): {h:.4f}")
print(f"   Cross Entropy H(P, Q): {cross:.4f}")
print(f"   KL Divergence: {kl:.4f}")

print(f"\n4. Verification: H(P,P) = {cross_pp:.4f}, H(P,Q) = {cross:.4f}")
print(f"   Is H(P,P) < H(P,Q) when P != Q? {cross_pp < cross}")

# Task 5
ham = Hamming74()
original = [1, 0, 1, 1]
encoded = ham.encode(original)
# Simulate an error at index 4
encoded[4] ^= 1 
decoded = ham.decode(encoded)
print(f"\n5. Hamming (7,4): Original {original} -> Decoded {decoded}")