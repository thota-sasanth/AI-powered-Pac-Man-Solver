# multiAgents.py
# --------------


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]
    
    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        minghostdist = float('inf')  # initiliazing minimum of distance to all ghosts as infinity
        minfooddist = float('inf')  # initiliazing minimum of distance to all food dots as infinity
        fooddots = newFood.asList()   # converting newFood to list format
        

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        # minimax helper function for both ghosts & pacman based on 'turn' parameter
        def minimaxhelper(agentId, depth, currState, turn):
          actions = currState.getLegalActions(agentId)  # get all the legal actions for the current agent
          if turn =='max':  # 'max' turn is for pacman
            answer = [float('-inf'),None]
          else: # 'min' turn is for ghosts
            answer = [float('inf'),None]
            
          return answer

        # recursive function for the minimax algorithm  
        def minimax(agentId, depth, currState ):
          if agentId >= currState.getNumAgents(): # returning the turn to pacman after all ghosts turns are finished
            agentId = 0
            depth += 1
        return act # returning best possible action for the agent
          
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #
        # Adding extra alpha and beta parameters along with some logical changes to the above minimax algorithm for alpha-beta pruning algorithm
        #

        # alpha beta pruning helper function for both ghosts & pacman based on 'turn' parameter
        def alphabetahelper(agentId, depth, currState, turn, alpha, beta):
          actions = currState.getLegalActions(agentId)  # get all the legal actions for the current agent
          if turn =='max':  # 'max' turn is for pacman
            answer = [float('-inf'),None]
          else: # 'min' turn is for ghosts
            answer = [float('inf'),None]
          
              
            
          if tmp_ans is not None :
            return tmp_ans  
          return answer

        # recursive function for the alpha beta pruning algorithm  
        def alphabeta(agentId, depth, currState, alpha, beta):
          if agentId >= currState.getNumAgents(): # returning the turn to pacman after all ghosts turns are finished
            agentId = 0
            depth += 1
          
          return alphabetahelper(0, depth, currState, 'max', alpha, beta) if agentId == 0 else alphabetahelper(agentId, depth, currState, 'min', alpha, beta)

        alpha = float('-inf')
        beta = float('inf')
        # initializing the recursive alpha beta pruning function calls for pacman (agentId: 0) with depth: 0, initial gameState, initial alpha & beta values
        act = alphabeta(0, 0, gameState, alpha, beta)[1]
        return act  # returning best possible action for the agent

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #
        #  Making some logical changes to the above minimax algorithm for expectimax algorithm
        #
        
        # expectimax helper function for both ghosts & pacman based on 'turn' parameter
        def expectimaxhelper(agentId, depth, currState, turn):
          actions = currState.getLegalActions(agentId)  # get all the legal actions for the current agent
          scoreWithChance = 0
          if turn =='max':  # 'max' turn is for pacman
            answer = [float('-inf'), None]
          else: # 'min' turn is for ghosts
            answer = [float('inf'), None]
          
          return answer
        
        # recursive function for the expectimax algorithm
        def expectimax(agentId, depth, currState):
          if agentId >= currState.getNumAgents(): # returning the turn to pacman after all ghosts turns are finished
            agentId = 0
            depth += 1
          if len(currState.getLegalActions(agentId)) == 0:  # if there are no legal actions possible for the current agent (i.e., in case of leaf node)
            return [self.evaluationFunction(currState),None]  # return the current state (leaf) score directly
          
        # initializing the recursive expectimax function calls for pacman (agentId: 0) with depth: 0, initial gameState
        act = expectimax(0, 0, gameState)[1]
        return act  # returning best possible action for the agent

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

