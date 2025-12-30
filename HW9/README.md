# Linear Algebra Lab: Concepts and Implementations

This project implements core Linear Algebra algorithms from scratch and provides a theoretical framework for understanding matrix transformations and decompositions.

---

## 📑 Table of Contents
1. [Fundamental Concepts](#1-fundamental-concepts)
2. [Geometric Transformations](#2-geometric-transformations)
3. [Determinants & LU Decomposition](#3-determinants--lu-decomposition)
4. [Eigen-Decomposition & QR Algorithm](#4-eigen-decomposition--qr-algorithm)
5. [SVD & PCA](#5-svd--pca)
6. [License & Contact](#6-license--contact)

---

## 1. Fundamental Concepts

* **Linear (線性):** Refers to operations satisfying Additivity $f(x+y) = f(x) + f(y)$ and Homogeneity $f(cx) = cf(x)$.
* **Algebra (代數):** The study of mathematical symbols and the rules for manipulating them to solve systems of equations.
* **Vector Space (向量空間):** A set where you can add vectors and multiply by scalars without leaving the set. It is a "space" because it defines the boundaries of possible movement.

---

## 2. Geometric Transformations

Matrices act as functions that transform vectors. Common 2D transformations include:

* **Scaling**
  $$\begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}$$

* **Rotation**
  $$\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

* **Translation**
  Requires Homogeneous Coordinates to remain a linear operation:
  $$\begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} = \begin{bmatrix} x + t_x \\ y + t_y \\ 1 \end{bmatrix}$$

## 3. Determinants & LU Decomposition

* **Determinant ($\det(A)$)**
  Geometrically, this is the signed volume scaling factor.

* **Recursive Calculation**
  Uses cofactor expansion (Laplace expansion):
  $$\det(A) = \sum_{j=1}^{n} (-1)^{1+j} a_{1,j} M_{1,j}$$

* **LU Decomposition**
  Factoring a matrix into $A = LU$.
  * **Determinant via LU:** $$\det(A) = \prod u_{ii}$$

---

## 4. Eigen-Decomposition & QR Algorithm

* **Eigen-Decomposition:** $A = V \Lambda V^{-1}$.
    * **Eigenvectors ($V$):** Directions that do not change during transformation.
    * **Eigenvalues ($\Lambda$):** Scaling factors along those directions.
* **QR Decomposition:** $A = QR$, where $Q$ is orthogonal ($Q^TQ = I$) and $R$ is upper triangular.
* **QR Algorithm:** Repeatedly calculating $A_k = Q_k R_k$ and then $A_{k+1} = R_k Q_k$ allows the matrix to converge to a form where eigenvalues are on the diagonal.

---

## 5. SVD & PCA

### Singular Value Decomposition (SVD)
SVD works for any $m \times n$ matrix:
$$A = U \Sigma V^T$$
* $U$: Left singular vectors (rotation in output space).
* $\Sigma$: Singular values (stretching).
* $V^T$: Right singular vectors (rotation in input space).



### Principal Component Analysis (PCA)
* **Purpose:** Dimensionality reduction by finding the axes of maximum variance.
* **SVD Connection:** PCA is equivalent to SVD performed on centered data. The principal components are the eigenvectors of the covariance matrix $C = \frac{1}{n-1} X^T X$.

---