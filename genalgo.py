import random
import string
from operator import add, truediv
huruf = string.ascii_uppercase

list_distances = {
    'AB':80, 'BA':80, 'AC':798, 'CA':798, 'AD':777, 'DA':777, 'AE':25, 'EA':25, 'AF':329, 'FA':329,
    'BC':862, 'CB':862, 'BD':857, 'DB':857, 'BE':95, 'EB':95, 'BF':334, 'FB':334, 'CD':158, 'DC':158,
    'CE':771, 'EC':771, 'CF':529, 'FC':529, 'DE':762, 'ED':762, 'DF':398, 'FD':398, 'EF':328, 'FE':328
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
            places.append(startPoint+x[i])
            distances.append(list_distances[startPoint+x[i]])
        elif i < (len(x)-1):
            places.append(x[i]+x[i+1])
            distances.append(list_distances[x[i]+x[i+1]])
        else:
            places.append(x[i]+startPoint)
            distances.append(list_distances[x[i]+startPoint])
    return places
    # return places, distances

def population(noOfIndividual, startPoint, noOfPlaces):
    return [individual(startPoint, noOfPlaces) for x in range(noOfIndividual)]

print(population(6, 'A', 6))