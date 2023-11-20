#HARDEST ONE SO FAR
from scipy.optimize import fsolve

def equilibrium_equation(p, N):
    # Expected utility of the discrete strategy
    U_d = p * 1 + (1 - p) * (1 / N)

    # Expected utility of allocating fuel to at least two races
    U_c = (1 - p) * probability_of_winning(N, p)

    # Equate the expected utilities to find the Nash equilibrium
    return U_d - U_c

def probability_of_winning(N, p):
    # Probability of winning with at least two races
    return (1 - p) * ((1 - p) ** (N - 1))

# Solve for p in the Nash equilibrium equation
N = 8
initial_guess = 0.5  # Starting with a reasonable initial guess
p_solution = fsolve(equilibrium_equation, initial_guess, args=(N))[0]

# Print the result with 6 significant digits
print(f"The probability p is approximately: {p_solution:.6f}")
