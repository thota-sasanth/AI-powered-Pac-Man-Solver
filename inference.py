import random
import util
from bayesNet import Factor
from factorOperations import joinFactorsByVariableWithCallTracking, joinFactors
from factorOperations import eliminateWithCallTracking, normalize

def inferenceByEnumeration(bayesNet, queryVariables, evidenceDict):
    """
    An inference by enumeration implementation provided as reference.
    This function performs a probabilistic inference query that
    returns the factor:

    P(queryVariables | evidenceDict)

    bayesNet:       The Bayes Net on which we are making a query.
    queryVariables: A list of the variables which are unconditioned in
                    the inference query.
    evidenceDict:   An assignment dict {variable : value} for the
                    variables which are presented as evidence
                    (conditioned) in the inference query. 
    """
    callTrackingList = []
    joinFactorsByVariable = joinFactorsByVariableWithCallTracking(callTrackingList)
    eliminate = eliminateWithCallTracking(callTrackingList)

    # initialize return variables and the variables to eliminate
    evidenceVariablesSet = set(evidenceDict.keys())
    queryVariablesSet = set(queryVariables)
    

    # normalize so that the probability sums to one
    # the input factor contains only the query variables and the evidence variables, 
    # both as unconditioned variables
    queryConditionedOnEvidence = normalize(fullJointOverQueryAndEvidence)
    # now the factor is conditioned on the evidence variables

    # the order is join on all variables, then eliminate on all elimination variables
    return queryConditionedOnEvidence

def inferenceByVariableEliminationWithCallTracking(callTrackingList=None):

    def inferenceByVariableElimination(bayesNet, queryVariables, evidenceDict, eliminationOrder):
        """
        Question 6: Your inference by variable elimination implementation

        This function should perform a probabilistic inference query that
        returns the factor:

        P(queryVariables | evidenceDict)

        It should perform inference by interleaving joining on a variable
        and eliminating that variable, in the order of variables according
        to eliminationOrder.  See inferenceByEnumeration for an example on
        how to use these functions.

        You need to use joinFactorsByVariable to join all of the factors 
        that contain a variable in order for the autograder to 
        recognize that you performed the correct interleaving of 
        joins and eliminates.

        If a factor that you are about to eliminate a variable from has 
        only one unconditioned variable, you should not eliminate it 
        and instead just discard the factor.  This is since the 
        result of the eliminate would be 1 (you marginalize 
        all of the unconditioned variables), but it is not a 
        valid factor.  So this simplifies using the result of eliminate.

        The sum of the probabilities should sum to one (so that it is a true 
        conditional probability, conditioned on the evidence).

        bayesNet:         The Bayes Net on which we are making a query.
        queryVariables:   A list of the variables which are unconditioned
                          in the inference query.
        evidenceDict:     An assignment dict {variable : value} for the
                          variables which are presented as evidence
                          (conditioned) in the inference query. 
        eliminationOrder: The order to eliminate the variables in.

        Hint: BayesNet.getAllCPTsWithEvidence will return all the Conditional 
        Probability Tables even if an empty dict (or None) is passed in for 
        evidenceDict. In this case it will not specialize any variable domains 
        in the CPTs.

        Useful functions:
        BayesNet.getAllCPTsWithEvidence
        normalize
        eliminate
        joinFactorsByVariable
        joinFactors
        """

        # this is for autograding -- don't modify
        joinFactorsByVariable = joinFactorsByVariableWithCallTracking(callTrackingList)
        eliminate             = eliminateWithCallTracking(callTrackingList)
        
        # creating a factor by joining all factors in the above list 
        # and normalizing the created factor
        normFactVarEliminated = normalize(joinFactors(currentFactorsList))
        return normFactVarEliminated
        "*** END YOUR CODE HERE ***"


    return inferenceByVariableElimination

inferenceByVariableElimination = inferenceByVariableEliminationWithCallTracking()

def sampleFromFactorRandomSource(randomSource=None):
    if randomSource is None:
        randomSource = random.Random()

    def sampleFromFactor(factor, conditionedAssignments=None):
        """
        Sample an assignment for unconditioned variables in factor with
        probability equal to the probability in the row of factor
        corresponding to that assignment.

        factor:                 The factor to sample from.
        conditionedAssignments: A dict of assignments for all conditioned
                                variables in the factor.  Can only be None
                                if there are no conditioned variables in
                                factor, otherwise must be nonzero.

        Useful for inferenceByLikelihoodWeightingSampling

        Returns an assignmentDict that contains the conditionedAssignments but 
        also a random assignment of the unconditioned variables given their 
        probability.
        """
        if conditionedAssignments is None and len(factor.conditionedVariables()) > 0:
            raise ValueError("Conditioned assignments must be provided since \n" +
                            "this factor has conditionedVariables: " + "\n" +
                            str(factor.conditionedVariables()))

        elif conditionedAssignments is not None:
            conditionedVariables = set([var for var in conditionedAssignments.keys()])

            if not conditionedVariables.issuperset(set(factor.conditionedVariables())):
                raise ValueError("Factor's conditioned variables need to be a subset of the \n"
                                    + "conditioned assignments passed in. \n" + \
                                "conditionedVariables: " + str(conditionedVariables) + "\n" +
                                "factor.conditionedVariables: " + str(set(factor.conditionedVariables())))

            # Reduce the domains of the variables that have been
            # conditioned upon for this factor 
            newVariableDomainsDict = factor.variableDomainsDict()
            for (var, assignment) in conditionedAssignments.items():
                newVariableDomainsDict[var] = [assignment]

            # Get the (hopefully) smaller conditional probability table
            # for this variable 
            CPT = factor.specializeVariableDomains(newVariableDomainsDict)
        else:
            CPT = factor
        

    return sampleFromFactor

sampleFromFactor = sampleFromFactorRandomSource()
