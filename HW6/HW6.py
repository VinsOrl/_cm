import math

# ----- BASIC OBJECTS -----
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Line:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c  # ax + by + c = 0

class Circle:
    def __init__(self, h, k, r):
        self.h, self.k, self.r = h, k, r

# ----- 1. INTERSECTION OF TWO LINES -----
def intersect_lines(L1, L2):
    D = L1.a * L2.b - L2.a * L1.b
    if D == 0:
        return None  # Parallel or identical
    x = (L2.c * L1.b - L1.c * L2.b) / D
    y = (L1.c * L2.a - L2.c * L1.a) / D
    return Point(x, y)

# ----- 2. INTERSECTION OF TWO CIRCLES -----
def intersect_circles(C1, C2):
    dx, dy = C2.h - C1.h, C2.k - C1.k
    d = math.hypot(dx, dy)
    if d > C1.r + C2.r or d < abs(C1.r - C2.r) or d == 0:
        return None  # No or infinite intersections
    a = (C1.r**2 - C2.r**2 + d**2) / (2 * d)
    h = math.sqrt(C1.r**2 - a**2)
    x2 = C1.h + a * dx / d
    y2 = C1.k + a * dy / d
    rx = -dy * (h / d)
    ry = dx * (h / d)
    return Point(x2 + rx, y2 + ry), Point(x2 - rx, y2 - ry)

# ----- 3. INTERSECTION OF LINE AND CIRCLE -----
def intersect_line_circle(L, C):
    a, b, c = L.a, L.b, L.c
    h, k, r = C.h, C.k, C.r

    # Shift line relative to circle center
    c_ = a * h + b * k + c
    x0 = -a * c_ / (a**2 + b**2) + h
    y0 = -b * c_ / (a**2 + b**2) + k
    dist = abs(c_) / math.sqrt(a**2 + b**2)

    if dist > r:
        return None  # No intersection
    elif abs(dist - r) < 1e-6:
        return (Point(x0, y0),)  # Tangent point
    else:
        d = math.sqrt(r**2 - dist**2)
        mult = d / math.sqrt(a**2 + b**2)
        return (Point(x0 + b * mult, y0 - a * mult),
                Point(x0 - b * mult, y0 + a * mult))

# ----- 4. PERPENDICULAR FROM A POINT TO A LINE -----
def perpendicular_foot(L, P):
    a, b, c = L.a, L.b, L.c
    x0, y0 = P.x, P.y
    x = (b*(b*x0 - a*y0) - a*c) / (a**2 + b**2)
    y = (a*(-b*x0 + a*y0) - b*c) / (a**2 + b**2)
    return Point(x, y)

# ----- 5. VERIFY PYTHAGOREAN THEOREM -----
def verify_pythagoras(P, foot, Q):
    a = math.hypot(P.x - foot.x, P.y - foot.y)
    b = math.hypot(Q.x - foot.x, Q.y - foot.y)
    c = math.hypot(P.x - Q.x, P.y - Q.y)
    return abs(a**2 + b**2 - c**2) < 1e-6

# ----- 6. TRIANGLE OBJECT -----
class Triangle:
    def __init__(self, A, B, C):
        self.A, self.B, self.C = A, B, C

    def translate(self, dx, dy):
        for p in [self.A, self.B, self.C]:
            p.x += dx
            p.y += dy

    def scale(self, factor):
        for p in [self.A, self.B, self.C]:
            p.x *= factor
            p.y *= factor

    def rotate(self, angle):
        rad = math.radians(angle)
        for p in [self.A, self.B, self.C]:
            x, y = p.x, p.y
            p.x = x * math.cos(rad) - y * math.sin(rad)
            p.y = x * math.sin(rad) + y * math.cos(rad)
