import numpy as np
from queue import PriorityQueue

class State:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def __lt__(self, other):
        return False

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def print_state(self, state):
        print(state)

    def is_goal(self, state):
        return np.array_equal(state, self.goal_state)

    def get_possible_moves(self, state):
        possible_moves = []
        r, c = np.where(state == 0)
        r, c = r[0], c[0]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = np.copy(state)
                new_state[r, c], new_state[nr, nc] = new_state[nr, nc], new_state[r, c]
                possible_moves.append(new_state)
        return possible_moves

    def heuristic(self, state):
        return np.count_nonzero(state != self.goal_state)

    def solve(self):
        queue = PriorityQueue()
        initial_state = State(self.initial_state, None)
        queue.put((0, initial_state))
        visited = {str(self.initial_state)}

        while not queue.empty():
            priority, current_state = queue.get()
            if self.is_goal(current_state.state):
                return current_state
            for move in self.get_possible_moves(current_state.state):
                key = str(move)
                if key not in visited:
                    visited.add(key)
                    move_state = State(move, current_state)
                    priority = self.heuristic(move)
                    queue.put((priority, move_state))
        return None

initial_state = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.solve()
move1 = -1

if solution is not None:
    moves = []
    while solution is not None:
        moves.append(solution.state)
        solution = solution.parent
    for move in reversed(moves):
        move1 += 1
        puzzle.print_state(move)
        print()
    print("No of moves:", move1)
else:
    print("No solution found.")