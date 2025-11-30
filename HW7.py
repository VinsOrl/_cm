# Probability and Statistics - The Mathematical Principles Behind the Test

import numpy as np
import math

# --- 1. One-Sample Z-Test ---
def z_test_scratch(data, pop_mean, pop_std):
    n = len(data)
    sample_mean = np.mean(data)
    
    # Formula: Signal / Noise (Standard Error)
    std_error = pop_std / np.sqrt(n)
    z_stat = (sample_mean - pop_mean) / std_error
    
    # P-value from Z-score using Error Function (math.erf)
    # This calculates the two-tailed p-value
    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z_stat) / math.sqrt(2))))
    
    return z_stat, p_value

# --- 2. One-Sample T-Test ---
def t_test_one_sample_scratch(data, pop_mean):
    n = len(data)
    sample_mean = np.mean(data)
    
    # Calculate Sample Std Dev (ddof=1 for Bessel's correction)
    sample_std = np.std(data, ddof=1)
    
    std_error = sample_std / np.sqrt(n)
    t_stat = (sample_mean - pop_mean) / std_error
    
    return t_stat # P-value requires complex integration

# --- 3. Independent Two-Sample T-Test ---
def t_test_ind_scratch(data1, data2, equal_var=True):
    n1, n2 = len(data1), len(data2)
    m1, m2 = np.mean(data1), np.mean(data2)
    v1, v2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
    
    if equal_var:
        # Pooled Variance (Student's t-test)
        pooled_var = ((n1 - 1)*v1 + (n2 - 1)*v2) / (n1 + n2 - 2)
        std_error = np.sqrt(pooled_var * (1/n1 + 1/n2))
    else:
        # Unpooled Variance (Welch's t-test)
        std_error = np.sqrt(v1/n1 + v2/n2)
        
    t_stat = (m1 - m2) / std_error
    return t_stat

# --- 4. Paired T-Test ---
def t_test_paired_scratch(before, after):
    # Calculate differences
    diffs = np.array(after) - np.array(before)
    
    # This effectively becomes a One-Sample T-Test on the differences
    n = len(diffs)
    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs, ddof=1)
    
    std_error = std_diff / np.sqrt(n)
    t_stat = mean_diff / std_error
    
    return t_stat