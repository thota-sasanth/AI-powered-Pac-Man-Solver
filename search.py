# search.py
# ---------


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""

    # print ("Start:", problem.getStartState())
    # print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print ("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # print(problem)
    
    "*** YOUR CODE HERE ***"
    fringeList = util.Stack()          # using pre-defined stack data structure as fringe list
    actions = []
    fringeList.push([problem.getStartState(), []])     
    expandedList = []             
    while True:
        if fringeList.isEmpty():
            return None               # failure mode
        currNode = fringeList.pop()   
        if problem.isGoalState(currNode[0]):
            actions = currNode[1]
            break                     # break when we reach goal state
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    fringeList = util.Queue()     # using pre-defined queue data structure as fringe list
    actions = []
    fringeList.push([problem.getStartState(), []])
    expandedList = []
    while True:
        if fringeList.isEmpty():
            return None           
        currNode = fringeList.pop()            # currNode same as in DFS
        
        if currNode[0] not in expandedList:
            for node in problem.getSuccessors(currNode[0]):
                tmp = list(currNode[1])
            expandedList.append(currNode[0])

    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringeList = util.PriorityQueue()    # using pre-defined priority queue data structure as fringe list
    actions = []
    
    while True:
        if fringeList.isEmpty():
            return None 
        currNode = fringeList.pop()     
        if problem.isGoalState(currNode[0]):
            actions = currNode[1]
            break

            
    # util.raiseNotDefined()
    return actions

