# Generalized Nash Equilibrium Simulation
---
In the simulation, $P$ players make choices over $I$ iterations, each opting for one of $N$ strategies. In each iteration, a payoff matrix $M_{[N \times N \times P]}$ is generated with random values $p \in [\xi {-}, \xi {+}]$, representing rewards or penalties for players' decisions. Each player employs an algorithm $\alpha(M)$, where $\alpha: [\xi{-}, \xi{+}]^{m \times n} \to \mathbb{Z}$, to maximize their payoff over time. The results are accumulated during the $I$ iterations, enabling the assessment of the average performance of strategies.

This approach provides insights into the effectiveness of strategies on average, exploring variability introduced by random payoff matrices in dynamic or stochastic environments.

---

### Summary

1. [installation](/docs/installation.md)