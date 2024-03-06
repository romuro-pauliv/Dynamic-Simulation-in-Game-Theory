# Dynamic Simulation in Game Theory
---

### Summary

- [Installation](/docs/installation.md)
- [Quickstart - Run the simulation]()
    - [Algorithm Structure](/README.md#simulation-algorithm-structure)
    - [Single Tensor Payoffs (STP)](/README.md#single-tensor-payoffs-stp)
    - [Collective Tensor Payoffs (CTP)](/README.md#collective-tensor-payoffs-ctp)
    - [Arrangements](/README.md#arrangements)
    - [Algorithm Performance](/README.md#algorithm-performance)


---
In the simulation, $P$ players make choices over $I$ iterations, each opting for one of $N$ strategies. In each iteration, a payoff matrix $M_{[N \times N]}$ is generated with random values $m \in [\xi {-}, \xi {+}]$, representing rewards or penalties for players' decisions. Each player employs an algorithm $E(M_{N \times N})$, where $E: [\xi{-}, \xi{+}]^{N \times N} \to \{ 0, 1, 2, ..., N\}$, to maximize their payoff over time. The results are accumulated during the $I$ iterations, enabling the assessment of the average performance of strategies.

This approach provides insights into the effectiveness of strategies on average, exploring variability introduced by random payoff matrices in dynamic or stochastic environments.

## Simulation Algorithm Structure

### Single Tensor Payoffs (STP)

Initially, we consider player $P_{1}$ with the payoff matrix $A_{N \times N}$, where $A \in [\xi{-}, \xi{+}]^{N \times N}$, and player $P_{2}$ with the payoff matrix $B_{N \times N}$, where $B \in [\xi{-}, \xi{+}]^{N \times N}$. 

$$A_{N \times N} = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n}\\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{bmatrix}, \quad B_{N \times N} = \begin{bmatrix}
b_{11} & b_{12} & \dots & b_{1n}\\
\vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & \dots & b_{nn}
\end{bmatrix}
$$

The number of rows corresponds to the number of possible strategies for the choice. If $P_{1}$ chooses strategy $k$ based on their payoff matrix $A_{N \times N}$, we have:

$$A_{1 \times N} = \begin{bmatrix} a_{k1} & a_{k2} & \dots & a_{kn} \end{bmatrix}$$

Similarly, player $P_{2}$ chooses strategy $j$ based on their payoff matrix $B_{N \times N}$:

$$B_{1 \times N} = \begin{bmatrix} b_{j1} & b_{j2} & \dots & b_{jn} \end{bmatrix}$$

It is important to note that the payoff assigned to player $P_{1}$ due to strategy $k$ is strictly dependent on the choice $j$ of player $P_{2}$. Thus, the payoff $p$ for $P_{1}$ and $P_{2}$ is given by:

$$p(P_{1}) = A_{kj}, \quad p(P_{2}) = B_{jk}$$

In the algorithm, the strategy choice is made through the function $E(M_{N \times N})$:

$$E:  [\xi{-}, \xi{+}]^{N \times N} \rightarrow  \{0, 1, 2, \ldots, N\}$$

Thus, to obtain the payoff $p$ for $P_{1}$ and $P_{2}$:

$$p(P_{1}) = A_{E(A) E(B)}, \quad p(P_{2}) = B_{E(B) E(A)}$$

Generalizing for a quantity of $P_{Q}$ players, the payoff matrix of each player $M_{Q}$ increases in dimension as new players are included. Therefore, for a set of $Q$ players, we will have $Q$ dimensions in the payoff matrix $M_{Q}$. We can then define the tensor $T$ to represent the matrix $M_{Q}$, which is $Q$-dimensional, and whose dimension is determined by: 

```math
\Omega = \underbrace{N \times N \times \dots \times N}_{Q}
```


$$T \in [\xi{-}, \xi{+}]^{\Omega}$$

Thus, the strategy selection function $E(T^{Q})$ is defined as:

$$E:  [\xi{-}, \xi{+}]^{\Omega} \rightarrow  \{0, 1, 2, \ldots, N\}$$

Consequently, for each $P_{1}, P_{2}, \dots, P_{Q}$ with tensors of payoffs $T^{1}, T^{2}, \dots, T^{Q}$, we obtain the payoff $p$ for player $P_{Q}$:

$$p(P_{Q}) = T_{E(T^{Q}) \dots E(T^{i})}$$

### Collective Tensor Payoffs (CTP)

When the strategy decision function $E$ requires the payoff tensors from other players $E(T^{1}, T^{2}, \dots, T^{Q})$, we can define:

$$\varphi = \begin{bmatrix}T^{1} & T^{2} & \dots & T^{Q} \end{bmatrix}$$

$$\varphi \in [\xi{-}, \xi{+}]^{\Omega \times Q}$$

It is necessary to note that, for players $P_{1}$ and $P_{2}$, there exist $\varphi_{1}$ and $\varphi_{2}$ where $\varphi_{1} \neq \varphi_{2}$ due to the arrangement of elements in the matrix:

$$\begin{bmatrix} T^{1} & T^{2} & \dots & T^{Q}\end{bmatrix} \neq  \begin{bmatrix} T^{2} & T^{1} & \dots & T^{Q}\end{bmatrix}$$

So, for the function $E$ that receives $\varphi$, we define $\gamma$:

$$\gamma :  [\xi{-}, \xi{+}]^{\Omega \times Q} \rightarrow  \{0, 1, 2, \ldots, N\}$$

Therefore, to obtain the payoff for player $P_{Q}$:

```math
p(P_{Q}) = T^{Q}_{\gamma(\varphi_{Q}) \dots \gamma(\varphi_{i})}
```

### Arrangements

The goal of the simulation is to be used with various arrangements of strategy decision functions. As seen earlier, strategy decision functions are divided into two groups (STP and CTP). For each of these groups, we can have numerous different functions with distinct methods for choosing the strategy.

For example, for players $P_{1}, P_{2}, P_{3}$, we have the decision functions $E_{a}, E_{b}, \gamma_{c}$. Therefore, to obtain the payoffs of the players:

```math
p(P_{1}) = T^{1}_{E_{a}(T^{1})E_{b}(T^{2})\gamma_{c}(\varphi^{3})} \\
p(P_{2}) = T^{2}_{E_{b}(T^{2})E_{a}(T^{1})\gamma_{c}(\varphi^{3})} \\
p(P_{3}) = T^{3}_{\gamma_{c}(\varphi^{3})E_{a}(T^{1})E_{b}(T^{2})}
```


### Algorithm Performance

