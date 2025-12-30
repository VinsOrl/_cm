# ODE-to-RISC-V Compiler: Project Documentation Explanation

## 1. The Core Objective: Why Build an ODE Compiler?
At first glance, solving an Ordinary Differential Equation (ODE) and writing a compiler seem like separate worlds. However, this project bridges the gap between **mathematical modeling** and **system architecture**.

### The "Why"
Demonstrate **Domain-Specific Languages (DSLs)**. In the real world, complex physics or control systems (like drone stabilization) need to solve ODEs in microseconds. 
* **The Math:** Solving $\lambda^2 - 3\lambda + 2 = 0$.
* **The Engineering:** Translating the result into RISC-V assembly allows the math to run directly on hardware without the overhead of a heavy interpreter like Python.

---

## 2. The Mathematical Foundation
The general form of a homogeneous ODE with constant coefficients is:
$$a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_1 y' + a_0 y = 0$$

To solve this, we assume a solution $y = e^{rt}$, leading to the **Characteristic Equation**:
$$a_n r^n + a_{n-1} r^{n-1} + \dots + a_0 = 0$$



### Solution Logic:
| Root Type | Mathematical Solution Term |
| :--- | :--- |
| **Distinct Real ($r_1, r_2$)** | $y = C_1e^{r_1t} + C_2e^{r_2t}$ |
| **Repeated Real ($r$)** | $y = C_1e^{rt} + C_2te^{rt}$ |
| **Complex ($a \pm bi$)** | $y = e^{at}(C_1\cos(bt) + C_2\sin(bt))$ |

---

## 3. The Compiler Pipeline
The flow of data from a user's string to a machine's instruction follows these stages:

1.  **Lexer (Scanner):** * **Input:** `solve_ode {1, -3, 2}`
    * **Action:** Performs pattern matching to identify numbers and symbols.
    * **Result:** Tokens like `[CONST:1, CONST:-3, CONST:2]`.

2.  **Math Engine (Semantic Analysis):**
    * **Action:** Uses the roots of the polynomial to determine the behavior of the system.
    * **Logic:** Calculates $r_1=1, r_2=2$. It identifies that these are distinct real roots.

3.  **Code Generator (The Backend):**
    * **Action:** Maps the mathematical solution to RISC-V registers and instructions.
    * **Result:** The final `.s` assembly file.



---

## 4. RISC-V Connection & Assembly Logic
The generated code ends with standard RISC-V calling conventions:

```assembly
li a0, 0    # Load Immediate: Sets the return value to 0 (Success)
ret         # Return: Jumps back to the calling function