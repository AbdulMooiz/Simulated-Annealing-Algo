# Simulated-Annealing-Algo
This Python script defines a generic simulated_annealing function (inspired by GeeksforGeeks and Brownlee’s tutorials) and then applies it to a Ludo-style optimization: tokens racing home on a linear track. The SA core uses a temperature-driven acceptance rule (Boltzmann probability), neighbor generation, and a geometric cooling schedule. The Ludo example encodes each state as a list of four token positions, uses a sum-of-distances cost function, and random dice-roll moves as neighbors. You can adapt the generic SA solver to any optimization problem by supplying your own cost_fn and neighbor_fn.
## Source Code

Full implementation in [`src/simulated_annealing.py`](src/simulated_annealing.py).
