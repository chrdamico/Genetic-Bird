import random


def generatePopulation(populationSize, encodingLength):
    """
    Generation of the initial population. Population is a vector of dictionaries with the following entries:
    - jumps: encoding of the jump vector
    - fitness
    - score
    - jump counter
    """
    IND_SIZE = encodingLength
    POP_SIZE = populationSize

    population = [0]*POP_SIZE
    for i in range(POP_SIZE):

        jumpVector = [0]*IND_SIZE
        for j in range(IND_SIZE):
            jumpVector[j] = int(random.gauss(17, 4))

        population[i] = {'jumps': jumpVector, 'fitness': 0, 'score': 0, 'jumpCounter': 0}

    return population


def select(population, stuck):
    """Selection step of the genetic algorithm"""

    # Sort the population based on fitness
    sortedPopulation = (sorted(population, key=lambda i: i['fitness'], reverse=True))

    # when stuck, replace second and third best with new ones when they all have the same fitness
    if stuck:
        for i in range(2):
            if sortedPopulation[i+1]['fitness'] == sortedPopulation[i+3]['fitness']:
                sortedPopulation[i+1] = sortedPopulation[i+3]

    return sortedPopulation[0:3]


def mutate(population, chanceOfVariation, bounds, variationWidth, stuck):
    """Mutation step of the genetic algorithm"""

    # Keep the top selected unchanged, mutate the others
    # Only useful if more than 4 players are selected
    for count, ele in enumerate(population):
        # keep the 4 best intact
        if count < 3:
            continue
        else:
            population[count]['jumps'] = addRandomness(population[count]['jumps'], chanceOfVariation, population[count]['jump_counter'], bounds, variationWidth,stuck)
            population[count]['fitness'] = 0

    # add new entries by mutating the best until population is again = populationSize
    counter = 0
    while len(population) < 10:
        newEntry = {}
        newEntry['jumps'] = addRandomness(population[counter % 3]['jumps'], chanceOfVariation, population[count]['jump_counter'], bounds, variationWidth, stuck)
        newEntry['fitness'] = 0

        # make sure that something was actually changed. If it wasn't, continue iterating. Needed since the introduction
        # of chanceOfVariation would sometimes leave players unchanged
        if newEntry['jumps'] == population[counter%3]['jumps']:
            continue
        else:
            counter += 1
            population.append(newEntry)

    return population


def addRandomness(vector, chanceOfVariation, jumpCounter, bounds, variationWidth, stuck):
    """Modifies vector according to the hyperparameters. This is used in the mutation function"""

    array = [0] * len(vector)

    # In order to avoid changing good strategies, jumpCounter is exploited as an heuristic to guess how much
    # of the action vector to keep unchanged.
    # Different modifications are applied when the algorithm is "stuck" or in normal operating condition
    if stuck:
        # Slower more robust hyperparameters that try a wider range of solutions
        unchangedJumps = 3
        lBound = 1
        uBound = bounds[1] + 5
        variationWidth += 15
        chanceOfMutation = 0.6

    else:
        # Conservative fast hyperparameters for normal usage
        unchangedJumps = 2
        lBound = bounds[0]
        uBound = bounds[1]
        chanceOfMutation = chanceOfVariation

    for index, item in enumerate(vector):

        # Keep all constant up to the some last jumps before death
        # NOTE: do not unnecessarily change the later parts of the vector
        if (index > jumpCounter - unchangedJumps and index < jumpCounter + 2):

            # Either modify the value with some chance
            if random.random() < chanceOfMutation:
                array[index] = vector[index] + random.randint(-variationWidth, variationWidth)
            # Or keep it unchanged
            else:
                array[index] = vector[index]
        else:
            array[index] = vector[index]

    return imposeBounds(array, lBound, uBound)


def imposeBounds(array, lowerBound, upperBound):
    """Imposes bound on the elments of the chromosome vector"""
    for count, ele in enumerate(array):

        if array[count] > upperBound:
            array[count] = upperBound

        elif array[count] < lowerBound:
            array[count] = lowerBound

    return array


def checkStuckCondition(fitnessHistory, patience):
    """Simple check that determines if the algorithm is stuck according to a given patience value"""

    if len(fitnessHistory) < patience+1:
        return False
    else:
        return fitnessHistory[-1] <= fitnessHistory[-patience]
