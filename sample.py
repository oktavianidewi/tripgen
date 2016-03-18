import random
import string
from operator import add
# from random import randint, random, sample

huruf = string.ascii_uppercase

list_distances = {
    'AB':80, 'BA':80,
    'AC':798, 'CA':798,
    'AD':777, 'DA':777,
    'AE':25, 'EA':25,
    'AF':329, 'FA':329,
    'BC':862, 'CB':862,
    'BD':857, 'DB':857,
    'BE':95, 'EB':95,
    'BF':334, 'FB':334,
    'CD':158, 'DC':158,
    'CE':771, 'EC':771,
    'CF':529, 'FC':529,
    'DE':762, 'ED':762,
    'DF':398, 'FD':398,
    'EF':328, 'FE':328
}

def individual(startPoint, noOfPlaces):
    list_letter = [huruf[x] for x in range(1, noOfPlaces)]
    places = []
    distances = []
    # print list_letter
    x = random.sample(list_letter, len(list_letter))
    for i in range(0, len(x)):
        if i == 0:
            # print list_distances[tes]
            # places.append(startPoint+x[i])
            distances.append(list_distances[startPoint+x[i]])
        elif i < (len(x)-1):
            # places.append(x[i]+x[i+1])
            distances.append(list_distances[x[i]+x[i+1]])
        else:
            # places.append(x[i]+startPoint)
            distances.append(list_distances[x[i]+startPoint])
    # return places
    return distances

def population(noOfIndividual, startPoint, noOfPlaces):
    return [individual(startPoint, noOfPlaces) for x in xrange(noOfIndividual)]

def fitness(individual, target):
    sum = reduce(add, individual, 0)
    return abs(target-sum)

def grade(populs, target):
    # find average fitness for a population

    summed = reduce(add, (fitness(x, target) for x in populs), 0)
    return summed / (len(populs) * 1.0)

# pelajari bagian evolve ngga paham bagian iniiiii
def evolve(populs, target, retain = 0.2, random_select=0.05, mutate = 0.01):
    graded = [ (fitness(x, target), x) for x in populs ]
    graded = [ x[1] for x in sorted(graded) ]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]

    # randomly add other individuals to promote generic diversity
    for individual in graded[retain_length:]:
        if random_select > random.random():
            parents.append(individual)

    # mutate some individuals
    for individual in parents:
        if mutate > random.random():
            pos_to_mutate = random.randint(0, len(individual)-1)
            individual[pos_to_mutate] = random.randint(
                min(individual), max(individual)
            )

    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(populs) - parents_length
    children = []
    while len(children) < desired_length:
        male = random.randint(0, parents_length-1)
        female = random.randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male)/2
            child = male[:half] + female[:half]
            children.append(child)

    parents.extend(children)
    return parents

# to understand random from a list
startPoint = 'A' # endPoint = 'A'
noOfPlaces = 6
target = 100
populs = population(10, startPoint, noOfPlaces)
fitness_history = [grade(populs, target),]
for i in xrange(1):
    p = evolve(populs, target)
    fitness_history.append(grade(populs, target))

print populs
print fitness_history

# kalo udah ketemu nilai terendah,
# gimana caranya backtrack dapetin dari kota mana kemana?