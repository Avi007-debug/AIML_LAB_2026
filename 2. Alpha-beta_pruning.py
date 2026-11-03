def minimax(depth, node, maximizingPlayer, values, alpha, beta, d):
    print("   " * depth, end="")

    if depth == d:
        print(values[node])
        return values[node]

    if maximizingPlayer:
        print("MAX")
        best = float('-inf')

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, False, values, alpha, beta, d)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        print("MIN")
        best = float('inf')

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          True, values, alpha, beta, d)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = list(map(int, input("Enter values separated by spaces: ").split()))

d = int(input("Enter depth: "))

alpha = float('-inf')
beta = float('inf')

optimal_value = minimax(0, 0, True, values, alpha, beta, d)

print("The optimal value is:", optimal_value)