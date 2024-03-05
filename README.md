# Generalized Nash Equilibrium Simulation
---
In the simulation, $P$ players make choices over $I$ iterations, each opting for one of $N$ strategies. In each iteration, a payoff matrix $M_{[N \times N]}$ is generated with random values $m \in [\xi {-}, \xi {+}]$, representing rewards or penalties for players' decisions. Each player employs an algorithm $E(M_{N \times N})$, where $E: [\xi{-}, \xi{+}]^{N \times N} \to \{ 0, 1, 2, ..., N\}$, to maximize their payoff over time. The results are accumulated during the $I$ iterations, enabling the assessment of the average performance of strategies.

This approach provides insights into the effectiveness of strategies on average, exploring variability introduced by random payoff matrices in dynamic or stochastic environments.

---

### Summary

1. [installation](/docs/installation.md)


---
## Simulation Algorithm

### Auto Tensor Payoffs

Initially, we consider player \(P_{1}\) with the payoff matrix \(A_{N \times N}\), where \( A \in [\xi{-}, \xi{+}]^{N \times N} \), and player \(P_{2}\) with the payoff matrix \(B_{N \times N}\), where \(B \in [\xi{-}, \xi{+}]^{N \times N}\). 

\[ A_{N \times N} = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n}\\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{bmatrix}, \quad B_{N \times N} = \begin{bmatrix}
b_{11} & b_{12} & \dots & b_{1n}\\
\vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & \dots & b_{nn}
\end{bmatrix}
\]

The number of rows corresponds to the number of possible strategies for the choice. If \(P_{1}\) chooses strategy \(k\) based on their payoff matrix \(A_{N \times N}\), we have:

\[ A_{1 \times N} = \begin{bmatrix} a_{k1} & a_{k2} & \dots & a_{kn} \end{bmatrix} \]

Similarly, player \(P_{2}\) chooses strategy \(j\) based on their payoff matrix \(B_{N \times N}\):

\[ B_{1 \times N} = \begin{bmatrix} b_{j1} & b_{j2} & \dots & b_{jn} \end{bmatrix} \]

It is important to note that the payoff assigned to player \(P_{1}\) due to strategy \(k\) is strictly dependent on the choice \(j\) of player \(P_{2}\). Thus, the payoff \(p\) for \(P_{1}\) and \(P_{2}\) is given by:

\[ p(P_{1}) = A_{kj}, \quad p(P_{2}) = B_{jk} \]

In the algorithm, the strategy choice is made through the function \(E(M_{N \times N})\):

\[ E:  [\xi{-}, \xi{+}]^{N \times N} \rightarrow  \{0, 1, 2, \ldots, N\} \]

Thus, to obtain the payoff \(p\) for \(P_{1}\) and \(P_{2}\):

\[ p(P_{1}) = A_{E(A) E(B)}, \quad p(P_{2}) = B_{E(B) E(A)} \]

Generalizing to a quantity \(P_{Q}\) of players, where each player has their \(Q\)-dimensional matrix represented by the tensor \(T^{Q}\):

\[ T \in [\xi{-}, \xi{+}]^{Q} \]

Thus, the strategy selection function \(E(T^{Q})\) is defined as:

\[ E:  [\xi{-}, \xi{+}]^{Q} \rightarrow  \{0, 1, 2, \ldots, N\} \]

Consequently, for each \(P_{1}, P_{2}, \dots, P_{Q}\) with tensors of payoffs \(T^{1}, T^{2}, \dots, T^{Q}\), we obtain the payoff \(p\) for player \(P_{Q}\):

\[ p(P_{Q}) = T_{E(T^{Q}) \dots E(T^{i})} \]