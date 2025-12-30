import numpy as np

class LinearAlgebraLab:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=float)
        self.n = self.matrix.shape[0]

    # 1. Recursive Determinant (寫程式用遞迴的方式計算行列式)
    def recursive_det(self, M):
        if len(M) == 1:
            return M[0][0]
        if len(M) == 2:
            return M[0][0] * M[1][1] - M[0][1] * M[1][0]
        
        det = 0
        for c in range(len(M)):
            # Minor matrix: remove row 0 and column c
            minor = np.delete(np.delete(M, 0, axis=0), c, axis=1)
            det += ((-1)**c) * M[0][c] * self.recursive_det(minor)
        return det

    # 2. LU Decomposition and Determinant (寫程式做 LU 分解後，再計算行列式)
    def lu_decomposition(self):
        n = self.n
        L = np.eye(n)
        U = self.matrix.copy()

        for i in range(n):
            for j in range(i + 1, n):
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                U[j] -= factor * U[i]
        
        # Determinant is the product of diagonal elements of U
        det_lu = np.prod(np.diag(U))
        return L, U, det_lu

    # 3. Verification of Decompositions (寫程式驗證分解後可還原原矩陣)
    def verify_decompositions(self):
        print("--- Verification Results ---")
        
        # LU Verification
        L, U, _ = self.lu_decomposition()
        print(f"LU matches original: {np.allclose(self.matrix, L @ U)}")

        # Eigenvalue Decomposition (A = VΛV⁻¹)
        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
        V = eigenvectors
        Lambda = np.diag(eigenvalues)
        reconstructed_eigen = V @ Lambda @ np.linalg.inv(V)
        print(f"Eigen-decomposition matches original: {np.allclose(self.matrix, reconstructed_eigen)}")

        # SVD (A = UΣVᵀ)
        U_svd, s, Vt = np.linalg.svd(self.matrix)
        Sigma = np.zeros(self.matrix.shape)
        np.fill_diagonal(Sigma, s)
        reconstructed_svd = U_svd @ Sigma @ Vt
        print(f"SVD matches original: {np.allclose(self.matrix, reconstructed_svd)}")

    # 4. SVD via Eigen-decomposition (寫程式用 特徵值分解來做 SVD)
    # Based on AᵀA = VΣ²Vᵀ and AAᵀ = UΣ²Uᵀ
    def svd_via_eigen(self):
        A = self.matrix
        # 1. Compute V and Sigma from A.T @ A
        eigenvalues, V = np.linalg.eigh(A.T @ A)
        
        # Sort eigenvalues/vectors descending
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        V = V[:, idx]
        
        # Singular values are sqrt of eigenvalues
        s = np.sqrt(np.clip(eigenvalues, 0, None))
        
        # 2. Compute U = A @ V @ inv(Sigma)
        # Handle zero singular values with a small epsilon
        U = A @ V / (s + 1e-10)
        
        return U, s, V.T

    # 5. Principal Component Analysis (寫程式做 PCA 主成份分析)
    def run_pca(self, data, n_components=2):
        # Center the data
        mean = np.mean(data, axis=0)
        centered_data = data - mean
        
        # Covariance matrix
        cov_matrix = np.cov(centered_data, rowvar=False)
        
        # Eigen decomposition
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Sort and pick top components
        idx = np.argsort(eigenvalues)[::-1]
        top_eigenvectors = eigenvectors[:, idx[:n_components]]
        
        # Project data
        projected = np.dot(centered_data, top_eigenvectors)
        return projected

# --- Execution ---

# Sample Square Matrix for testing
test_matrix = [
    [4, 3, 2],
    [3, 2, 1],
    [2, 1, 3]
]

lab = LinearAlgebraLab(test_matrix)

print(f"1. Recursive Det: {lab.recursive_det(lab.matrix)}")
L, U, det_lu = lab.lu_decomposition()
print(f"2. LU Det: {det_lu}")
lab.verify_decompositions()

# PCA Example with random data
pca_data = np.random.rand(10, 3) # 10 samples, 3 features
projected_data = lab.run_pca(pca_data, n_components=2)
print(f"\n5. PCA Projection (first 2 samples):\n{projected_data[:2]}")