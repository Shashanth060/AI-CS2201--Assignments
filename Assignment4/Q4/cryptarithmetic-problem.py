from itertools import permutations

def solve_cryptarithmetic():
    digits = range(10)
    letters = ['T', 'W', 'O', 'F', 'U', 'R']

    solutions = []

    for perm in permutations(digits, len(letters)):
        T, W, O, F, U, R = perm

        if T == 0 or F == 0:
            continue

    
        TWO = 100*T + 10*W + O
        FOUR = 1000*F + 100*O + 10*U + R

        
        if TWO + TWO == FOUR:
            solutions.append({
                'T': T, 'W': W, 'O': O,
                'F': F, 'U': U, 'R': R
            })

    return solutions


solutions = solve_cryptarithmetic()

for sol in solutions:
    print("Solution:", sol)
    T, W, O, F, U, R = sol.values()
    print(f"{100*T + 10*W + O} + {100*T + 10*W + O} = {1000*F + 100*O + 10*U + R}")