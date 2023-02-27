########################################################
#
# CMPSC 441: Homework 3
#
########################################################


student_name = 'Kannarott Nhim'
student_email = 'kvn5067@psu.edu'



########################################################
# Import
########################################################

from hw3_utils import *
from collections import deque
import math

# Add your imports here if used






##########################################################
# 1. Best-First, Uniform-Cost, A-Star Search Algorithms
##########################################################

def sortByHeuristic(N):
    return N.heuristic

def sortByPathCost(N):
    return N.path_cost

def sortByPathAndHeuristic(N):
    return N.heuristic + N.path_cost


def best_first_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = [problem.init_state]  # used as "visited"

    while len(frontier) != 0:
        N = frontier.popleft()
        N.path_cost = 0
        if problem.goal_test(N.state) == True:
            return N
        oneStepExtension = N.expand(problem)
        for N_ in oneStepExtension:
            if N_.state not in explored:
                frontier.append(N_)
                frontier = deque(sorted(frontier, key=sortByHeuristic))
                explored.append(N_.state)
    return Node(None)

def uniform_cost_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = []                    # used as "expanded" (not "visited")
    
    while len(frontier) != 0:
        N = frontier.popleft();
        if problem.goal_test(N.state) == True:
            return N
        if N.state in explored:
            continue
        explored.append(N.state)
        oneStepExtension = N.expand(problem)
        for N_ in oneStepExtension:
            if N_.state not in explored:
                if N_.path() not in frontier:
                    frontier.append(N_)
                    frontier = deque(sorted(frontier, key=sortByPathCost))
                else:
                    for n in frontier:
                        if n.state == N_.state and N_.path_cost < n.path_cost:
                            frontier.remove(n)
                            frontier.append(N_)
                            frontier = deque(sorted(frontier, key=sortByPathCost))
                            break
    return Node(None)
    
def a_star_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = []                    # used as "expanded" (not "visited")
    
    while len(frontier) != 0:
        N = frontier.popleft();
        if problem.goal_test(N.state) == True:
            return N
        if N.state in explored:
            continue
        explored.append(N.state)
        oneStepExtension = N.expand(problem)
        for N_ in oneStepExtension:
            if N_.state not in explored:
                if N_.path() not in frontier:
                    frontier.append(N_)
                    frontier = deque(sorted(frontier, key=sortByPathAndHeuristic))
                else:
                    for n in frontier:
                        if n.state == N_.state and N_.heuristic < + n.heuristic:
                            frontier.remove(n)
                            frontier.append(N_)
                            frontier = deque(sorted(frontier, key=sortByPathAndHeuristic))
                            break
    return Node(None)




##########################################################
# 2. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    """
    The implementation of the class NQueensProblem related
    to Homework 2 is given for those students who were not
    able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.

    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    """
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n
        

    def actions(self, state):
        if state[-1] != -1:   # if all columns are filled
            return []         # then no valid actions exist
        
        valid_actions = list(range(self.n))
        col = state.index(-1) # index of leftmost unfilled column
        for row in range(self.n):
            for c, r in enumerate(state[:col]):
                if self.conflict(row, col, r, c) and row in valid_actions:
                    valid_actions.remove(row)
                    
        return valid_actions

        
    def result(self, state, action):
        col = state.index(-1) # leftmost empty column
        new = list(state[:])  
        new[col] = action     # queen's location on that column
        return tuple(new)

    
    def goal_test(self, state):
        if state[-1] == -1:   # if there is an empty column
            return False;     # then, state is not a goal state

        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2):
                    return False
        return True

    
    def conflict(self, row1, col1, row2, col2):
        return row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2)

    
    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from start state to to_state via from_state.
        The path from start_state to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        return cost + 1

    def countQueenInHorizontal(self, board, r):
        count = 0
        for c in range(len(board[r])):
            if board[r][c] == True:
                for space in range(len(board[r])):
                    if board[r][space] == True and space != c:
                        count += 1
        return count

    def countQueenInNorthEast(self, board, r, c):
        count = 0
        for i in range(min(len(board[r]) - c - 1, r)):
            if board[r-1][c+1] == True:
                count += 1
            r = r - 1
            c = c + 1
        return count

    def countQueenInSouthEast(self, board, r, c):
        count = 0
        for i in range(min(len(board[r]) - c -1, len(board[r]) - r - 1)):
            if board[r+1][c+1] == True:
                count += 1
            r = r + 1
            c = c + 1
        return count

    def countQueenInSouthWest(self, board, r, c):
        count = 0
        for i in range(min(c, len(board[r]) - r - 1)):
            if board[r+1][c-1] == True:
                count += 1
            r = r + 1
            c = c - 1
        return count

    def countQueenInNorthWest(self, board, r, c):
        count = 0
        for i in range(min(c, r)):
            if board[r-1][c-1] == True:
                count += 1
            r = r - 1
            c = c - 1
        return count


    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the total number of conflicts in the given
        state as a heuristic value for the state.
        """
        
        #construct the n x n board
        board = [[True if e == i else False for e in state] for i in range(len(state))]

        #prepend to board the row containing -1
        row = [True if e <= -1 else False for e in state]
        board.insert(0, row)

        heuristic = 0
        for row in range(len(board)):
            if board[row].count(True) > 1:
                heuristic += self.countQueenInHorizontal(board, row)
            for column in range(len(board[row])):
                if board[row][column] == True:
                    heuristic += self.countQueenInNorthEast(board, row, column)
                    heuristic += self.countQueenInSouthEast(board, row, column)
                    heuristic += self.countQueenInSouthWest(board, row, column)
                    heuristic += self.countQueenInNorthWest(board, row, column)
        return heuristic



##########################################################
# 3. Graph Problem
##########################################################



class GraphProblem(Problem):
    """
    The implementation of the class GraphProblem related
    to Homework 2 is given for those students who were
    not able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.

    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    """
    
    
    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

        
    def actions(self, state):
        """Returns the list of adjacent states from the given state."""
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        """Returns the resulting state by taking the given action.
            (action is the adjacent state to move to from the given state)"""
        return action

    
    def goal_test(self, state):
        return state == self.goal_state

    
    def g(self, cost, from_state, action, to_state):
        """
        Returns the path cost from root to to_state.
        Note that the path cost from the root to from_state
        is the give cost and the given action taken at from_state
        will lead you to to_state with the cost associated with
        the action.
        """
        return self.graph.get(from_state, to_state) + cost
    

    def h(self, state):
        """
        Returns the heuristic value for the given state. Heuristic
        value of the state is calculated as follows:
        1. if an attribute called 'heuristics' exists:
           - heuristics must be a dictionary of states as keys
             and corresponding heuristic values as values
           - so, return the heuristic value for the given state
        2. else if an attribute called 'locations' exists:
           - locations must be a dictionary of states as keys
             and corresponding GPS coordinates (x, y) as values
           - so, calculate and return the straight-line distance
             (or Euclidean norm) from the given state to the goal
             state
        3. else
           - cannot find nor calculate heuristic value for given state
           - so, just return a large value (i.e., infinity)
        """
        if hasattr(self.graph, 'heuristics'):
            return self.graph.heuristics[state]
        elif hasattr(self.graph, 'locations'):
            return math.sqrt((self.graph.locations[state][0] - self.graph.locations[self.goal_state][0])**2 + (self.graph.locations[state][1] - self.graph.locations[self.goal_state][1])**2)
        else:
            return math.inf




##########################################################
# 4. Eight Puzzle
##########################################################


class EightPuzzle(Problem):
    def __init__(self, init_state, goal_state=(1,2,3,4,5,6,7,8,0)):
        super().__init__(init_state, goal_state) 
    

    def actions(self, state):
        index = -1
        for i in range(len(state)):
            if state[i] == 0:
                index = i
                break
        if index == 0:
            return ['DOWN', 'RIGHT']
        elif index == 1:
            return ['DOWN', 'LEFT', 'RIGHT']
        elif index == 2:
            return ['DOWN', 'LEFT']
        elif index == 3:
            return ['UP', 'DOWN', 'RIGHT']
        elif index == 4:
            return ['UP', 'DOWN', 'LEFT', 'RIGHT']
        elif index == 5:
            return ['UP', 'DOWN', 'LEFT']
        elif index == 6:
            return ['UP', 'RIGHT']
        elif index == 7:
            return ['UP', 'LEFT', 'RIGHT']
        elif index == 8:
            return ['UP', 'LEFT']
            

    
    def result(self, state, action):
        result = list(state)
        index = -1
        for i in range(len(state)):
            if state[i] == 0:
                index = i
                break
        if action == 'DOWN':
            result[index], result[index+3] = result[index+3], result[index]
        elif action == 'UP':
            result[index], result[index-3] = result[index-3], result[index]
        elif action == 'LEFT':
            result[index], result[index-1] = result[index-1], result[index]
        elif action == 'RIGHT':
            result[index], result[index+1] = result[index+1], result[index]
        return tuple(result)

    
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        return False
    

    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from root to to_state via from_state.
        The path from root to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        return cost + 1
    

    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the sum of the Manhattan distances of misplaced
        tiles to their final positions.
        """
        board_state = [list(state[0:3]), list(state[3:6]), list(state[6:])]

        board_goal = [list(self.goal_state[0:3]), list(self.goal_state[3:6]), list(self.goal_state[6:])]

        distances = list()
        for row in range(len(board_state)):
            for col in range(len(board_state[row])):
                if board_state[row][col] != 0:
                    for r in range(len(board_goal)):
                        for c in range(len(board_goal[r])):
                            if board_state[row][col] == board_goal[r][c]:
                                distances.append(abs(row - r) + abs(col - c))
        return sum(distances)
