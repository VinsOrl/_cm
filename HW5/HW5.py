class FiniteField:
    def __init__(self, value, p):
        if p <= 1:
            raise ValueError("p must be a prime number.")
        self.p = p
        self.value = value % p

    def __add__(self, other):
        self._check_same_field(other)
        return FiniteField((self.value + other.value) % self.p, self.p)

    def __sub__(self, other):
        self._check_same_field(other)
        return FiniteField((self.value - other.value) % self.p, self.p)

    def __mul__(self, other):
        self._check_same_field(other)
        return FiniteField((self.value * other.value) % self.p, self.p)

    def inverse(self):
        if self.value == 0:
            raise ZeroDivisionError("Zero has no multiplicative inverse.")
        # Use Fermat’s little theorem since p is prime
        return FiniteField(pow(self.value, self.p - 2, self.p), self.p)

    def __truediv__(self, other):
        return self * other.inverse()

    def _check_same_field(self, other):
        if self.p != other.p:
            raise ValueError("Elements must be in the same finite field.")

    def __eq__(self, other):
        return self.value == other.value and self.p == other.p

    def __repr__(self):
        return f"{self.value} (mod {self.p})"


# Example: Finite field F7
p = 7
a = FiniteField(3, p)
b = FiniteField(5, p)

print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("Inverse of a =", a.inverse())
