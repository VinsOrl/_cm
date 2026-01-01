## Mathematics Behind the Programs

### Line–Line Intersection

We have two equations:

```
a1*x + b1*y + c1 = 0
```

```
a2*x + b2*y + c2 = 0
```

To find where they meet, we solve them simultaneously using Cramer's Rule:

```
x = (b1*c2 - b2*c1) / (a1*b2 - a2*b1)
```

```
y = (c1*a2 - c2*a1) / (a1*b2 - a2*b1)
```

If the denominator is 0, lines are parallel or identical.

---

### Circle–Circle Intersection

For two circles:

```
(x - h1)^2 + (y - k1)^2 = r1^2
```

```
(x - h2)^2 + (y - k2)^2 = r2^2
```

Steps:

1. Subtract the second equation from the first to get a line equation (common chord).
2. Find intersection points between that line and either circle.

Conditions:

* `d > r1 + r2`: no intersection
* `d = r1 + r2`: touch externally
* `|r1 - r2| < d < r1 + r2`: two points
* `d = |r1 - r2|`: touch internally
* `d < |r1 - r2|`: no intersection (one circle inside another)

---

### Line–Circle Intersection

Substitute line `y = m*x + c'` into circle `(x - h)^2 + (y - k)^2 = r^2`:

```
(1 + m^2)*x^2 + 2*(m*(c'-k) - h)*x + (h^2 + (c'-k)^2 - r^2) = 0
```

* Discriminant < 0: no intersection
* Discriminant = 0: tangent (one point)
* Discriminant > 0: two intersection points

---

### Perpendicular from a Point to a Line

Given line `ax + by + c = 0` and point `P(x0, y0)`, the foot `F(x1, y1)` is:

```
x1 = (b*(b*x0 - a*y0) - a*c)/(a^2 + b^2)
```

```
y1 = (a*(-b*x0 + a*y0) - b*c)/(a^2 + b^2)
```

This finds the projection of the point onto the line.

---

### Pythagorean Theorem Verification

Given triangle points:

* `P`: point outside the line
* `F`: foot of perpendicular
* `Q`: point on the line

Then:

```
a^2 + b^2 = c^2
```

where `a = PF`, `b = FQ`, and `c = PQ`. This verifies the right triangle relationship.

---

### Triangle Transformations

For triangle points `A, B, C`:

**Translation:**

```
x' = x + dx
```

```
y' = y + dy
```

**Scaling:**

```
x' = s*x
```

```
y' = s*y
```

Scaling preserves angles, changes size.

**Rotation (about origin):**

```
x' = x*cos(theta) - y*sin(theta)
```

```
y' = x*sin(theta) + y*cos(theta)
```

Uses rotation matrix to rotate points around the origin.

---

## Summary Table

| Operation                  | Math Concept                  | Program Part                        |
| -------------------------- | ----------------------------- | ----------------------------------- |
| Line-Line Intersection     | Solve linear equations        | intersect_lines()                   |
| Circle-Circle Intersection | Geometry of chords            | intersect_circles()                 |
| Line-Circle Intersection   | Quadratic substitution        | intersect_line_circle()             |
| Perpendicular Foot         | Projection formula            | perpendicular_foot()                |
| Pythagoras Verification    | Distance formula              | verify_pythagoras()                 |
| Transformations            | Linear algebra & trigonometry | Triangle.translate, .scale, .rotate |
