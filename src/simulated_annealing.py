import math
import random

def simulated_annealing(initial_state, cost_fn, neighbor_fn,
                        T0=100.0, alpha=0.95, max_iter=1000):
    """
    Generic Simulated Annealing optimizer.
    
    Args:
        initial_state: starting solution (any data structure)
        cost_fn(state): returns a numeric cost to minimize
        neighbor_fn(state): returns a nearby state
        T0: initial temperature
        alpha: cooling rate (0 < alpha < 1)
        max_iter: maximum number of iterations
    
    Returns:
        best_state, best_cost
    """
    current = initial_state
    current_cost = cost_fn(current)
    best, best_cost = current, current_cost
    
    T = T0
    for i in range(1, max_iter + 1):
        # Cooling schedule: geometric cooling
        T *= alpha

        # Generate a candidate neighbor
        candidate = neighbor_fn(current)
        candidate_cost = cost_fn(candidate)

        # Acceptance condition: always accept better, else accept with Boltzmann prob.
        Δ = candidate_cost - current_cost
        if Δ <= 0 or random.random() < math.exp(-Δ / T):
            current, current_cost = candidate, candidate_cost
            # Update global best
            if current_cost < best_cost:
                best, best_cost = current, current_cost

        # Optional: progress logging
        if i % (max_iter // 10) == 0:
            print(f"Iter {i}/{max_iter}, T={T:.3f}, BestCost={best_cost:.3f}")

    return best, best_cost

# ——————————————————————————————————————————————
# Ludo Example: tokens racing home on a linear board of length 57

BOARD_LENGTH = 57  # total steps from start to home

def ludo_cost(state):
    """
    Cost = sum of distances each token still must travel to reach home.
    state: list of 4 integers in [0..BOARD_LENGTH]
    """
    return sum(BOARD_LENGTH - pos for pos in state)

def ludo_neighbor(state):
    """
    Neighbor: randomly pick one token, simulate a dice roll (1–6),
    and move it forward (capped at BOARD_LENGTH).
    """
    new_state = state.copy()
    idx = random.randrange(len(state))
    step = random.randint(1, 6)
    new_state[idx] = min(BOARD_LENGTH, new_state[idx] + step)
    return new_state

if __name__ == "__main__":
    # Initialize all tokens at start (position 0)
    init_state = [0, 0, 0, 0]
    
    best_state, best_cost = simulated_annealing(
        initial_state=init_state,
        cost_fn=ludo_cost,
        neighbor_fn=ludo_neighbor,
        T0=50.0,         # starting temperature :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}
        alpha=0.90,      # cooling rate :contentReference[oaicite:2]{index=2}
        max_iter=5000    # number of iterations :contentReference[oaicite:3]{index=3}
    )
    
    print("\n=== Result ===")
    print("Best token positions:", best_state)
    print("Total distance remaining:", best_cost)
