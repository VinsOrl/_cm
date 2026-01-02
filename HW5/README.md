# Finite Field Arithmetic ($GF(p)$)

This module implements a **Finite Field** class, allowing for mathematical operations within a set containing a finite number of elements. In this implementation, the field size is defined by a prime number $p$.

---

## 1. What is a Finite Field?
A Finite Field $GF(p)$ is a set of integers $\{0, 1, \dots, p-1\}$ where addition, subtraction, multiplication, and division are all performed **modulo $p$**. 

### The Mathematical Rules
1. **Closure:** Every operation results in an element already in the set.
2. **Modular Arithmetic:** Every result is reduced by the remainder of division by $p$.
    * *Example ($p=7$):* $5 + 3 = 8 \equiv 1 \pmod 7$



---

## 2. Key Implementation Details

### A. Fermat’s Little Theorem for Division
Division in a finite field is not straightforward because standard decimals do not exist. Instead, to divide by $b$, we multiply by the **multiplicative inverse** of $b$.

According to **Fermat’s Little Theorem**, for any prime $p$ and any integer $a$ not divisible by $p$:
$$a^{p-1} \equiv 1 \pmod p$$
This implies the inverse is:
$$a^{-1} \equiv a^{p-2} \pmod p$$

The code implements this efficiently using Python's 3-argument `pow(value, p-2, p)` function.

### B. Field Validation
The `_check_same_field` method ensures that you cannot perform operations between elements of different fields (e.g., trying to add an element from $GF(7)$ to an element from $GF(11)$), as the mathematical structures are incompatible.

---

## 3. Operations Table ($p=7$)

| Operation | Standard Result | Finite Field Result | Logic |
| :--- | :--- | :--- | :--- |
| **Addition** | $3 + 5 = 8$ | **1** | $8 \pmod 7$ |
| **Subtraction** | $3 - 5 = -2$ | **5** | $-2 \pmod 7$ |
| **Multiplication** | $3 \times 5 = 15$ | **1** | $15 \pmod 7$ |
| **Division** | $3 \div 5$ | **2** | $3 \times 5^{7-2} \pmod 7$ |



---

## 4. Applications
Finite fields are the "secret sauce" behind modern digital security:
* **Cryptography:** RSA, Diffie-Hellman, and AES all rely on finite field math.
* **Blockchain:** Elliptic Curve Digital Signature Algorithm (ECDSA) used in Bitcoin.
* **Error Correction:** QR codes use Reed-Solomon codes based on finite fields.

---

## 5. Usage
```python
p = 7
a = FiniteField(3, p)
b = FiniteField(5, p)

print(a + b)  # 1 (mod 7)
print(a / b)  # 2 (mod 7)
```

---

# Finite Field Arithmetic (Galois Field $GF(p)$)

This module provides a robust Python implementation of **Finite Field** arithmetic. A finite field is a set of numbers where all operations (addition, subtraction, multiplication, and division) result in a value within the same set, defined by a prime modulus $p$.

---

## 1. Theoretical Overview
In abstract algebra, a **Finite Field** (or Galois Field) denoted as $GF(p)$ consists of integers $\{0, 1, \dots, p-1\}$. These structures are the backbone of modern digital security and communication.

### Core Mathematical Rules
* **Closure:** Every result of an operation is mapped back into the field using the modulo operator ($\%$).
* **Prime Requirement:** For the division operation to be well-defined for all non-zero elements, the field size $p$ must be a prime number.



---

## 2. Technical Implementation Details

### Multiplicative Inverses (Division)
In a finite field, division $a / b$ is defined as $a \cdot b^{-1}$. Since we are working in a discrete space, we cannot use decimals. This implementation uses **Fermat's Little Theorem** to find the inverse:

$$a^{p-1} \equiv 1 \pmod p \implies a^{-1} \equiv a^{p-2} \pmod p$$

**Code Logic:** The `inverse()` method utilizes Python's modular exponentiation: `pow(value, p-2, p)`, which is computationally efficient ($O(\log p)$).

---

## 3. Class Features

| Feature | Description |
| :--- | :--- |
| **Operator Overloading** | Supports standard Python operators (`+`, `-`, `*`, `/`). |
| **Field Safety** | The `_check_same_field` method prevents operations between incompatible fields (e.g., $GF(7)$ and $GF(11)$). |
| **Bessel's Logic** | Uses modular subtraction to ensure results never fall below zero. |



---

## 4. Practical Examples ($p=7$)

| Operation | Equation | Field Result | Logic |
| :--- | :--- | :--- | :--- |
| **Addition** | $3 + 5$ | **1** | $8 \pmod 7$ |
| **Subtraction** | $3 - 5$ | **5** | $-2 \equiv 5 \pmod 7$ |
| **Multiplication** | $3 \times 5$ | **1** | $15 \pmod 7$ |
| **Division** | $3 \div 5$ | **2** | $3 \times 5^{5} \pmod 7$ |

---

## 5. Real-World Applications
Finite fields are not just theoretical; they are used in:
* **Cryptography:** AES encryption and Elliptic Curve Cryptography (ECC).
* **Error Correction:** Reed-Solomon codes used in QR codes and satellite transmissions.
* **Blockchain:** Securing transactions in Bitcoin and Ethereum.

---

## 6. Quick Start
```python
p = 7
a = FiniteField(3, p)
b = FiniteField(5, p)

print(f"Inverse of {a} is {a.inverse()}") # 5 (mod 7)
print(f"Division: {a} / {b} = {a / b}")    # 2 (mod 7)