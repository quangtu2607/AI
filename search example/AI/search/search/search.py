# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

FAILURE = "FAILURE"
CUT_OFF = "CUTOFF"

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    explored = []
    start = problem.getStartState()
    frontier = util.Stack()
    frontier.push((start, []))
    while frontier:
        cur = frontier.pop()
        node = cur[0]
        path = cur[1]
        if problem.isGoalState(node):
            return path
        suc = problem.getSuccessors(node)
        if node not in explored:
            explored.append(node)
            for ele in suc:
                frontier.push((ele[0], path + [ele[0]]))
    return FAILURE

def depthLimitedSearch(problem, limit):
    explored = []
    start = problem.getStartState()
    frontier = util.Stack()
    frontier.push(((start, 0), []))
    while frontier:
        cur = frontier.pop()
        node = cur[0]
        path = cur[1]
        if problem.isGoalState(node[0]):
            return path
        if node[1] > limit:
            return CUT_OFF
        suc = problem.getSuccessors(node[0])
        if node[0] not in explored:
            explored.append(node[0])
            for ele in suc:
                frontier.push(((ele[0], node[1]+1), path + [ele[0]]))
    return FAILURE

def iterativeDeepeningSearch(problem):
    limit = 0
    while True:
        result = depthLimitedSearch(problem, limit)
        if result != CUT_OFF:
            return result
        limit += 1

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    explored = []
    start = problem.getStartState()
    frontier = util.Queue()
    frontier.push((start, []))
    while frontier:
        cur = frontier.pop()
        node = cur[0]
        path = cur[1]
        if problem.isGoalState(node):
            return path
        suc = problem.getSuccessors(node)
        if node not in explored:
            explored.append(node)
            for ele in suc:
                frontier.push((ele[0], path + [ele[0]]))
    return FAILURE

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    explored = []
    start = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((start, []), 0)
    while frontier:
        cur = frontier.pop()
        node = cur[0]
        path = cur[1]
        if problem.isGoalState(node):
            return path
        suc = problem.getSuccessors(node)
        if node not in explored:
            explored.append(node)
            for ele in suc:
                frontier.push((ele[0], path + [ele[0]]), problem.getCostOfActions(path + [ele[0]]))
    return FAILURE


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    explored = []
    start = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((start, []), 0)
    while frontier:
        cur = frontier.pop()
        node = cur[0]
        path = cur[1]
        if problem.isGoalState(node):
            return path
        suc = problem.getSuccessors(node)
        if node not in explored:
            explored.append(node)
            for ele in suc:
                print(heuristic(ele[0]) + problem.getCostOfActions(path + [ele[0]]))
                frontier.push((ele[0], path + [ele[0]]), heuristic(ele[0]) + problem.getCostOfActions(path + [ele[0]]))
    return FAILURE

def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    explored = []
    start = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((start, []), 0)
    while frontier:
        cur = frontier.pop()
        node = cur[0]
        path = cur[1]
        if problem.isGoalState(node):
            return path
        suc = problem.getSuccessors(node)
        if node not in explored:
            explored.append(node)
            for ele in suc:
                frontier.push((ele[0], path + [ele[0]]), heuristic(ele[0]))
    return FAILURE


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
dls = depthLimitedSearch
ids = iterativeDeepeningSearch
astar = aStarSearch
gbfs = greedyBestFirstSearch
ucs = uniformCostSearch
