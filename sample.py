import random
import string
from operator import add, truediv
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

sample_populasi = [['AB', 'BD', 'DE', 'ED', 'CA'],['AD', 'DB', 'BE', 'EC', 'CA'], ['AC', 'CB', 'BD', 'DE', 'EA'], ['AE', 'EB', 'BC', 'CD', 'DA'], ['AE', 'EC', 'CB', 'BD', 'DA'], ['AC', 'CD', 'DE', 'EB', 'BA']]

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
    # return places
    return places, distances

def population(noOfIndividual, startPoint, noOfPlaces):
    return [individual(startPoint, noOfPlaces) for x in xrange(noOfIndividual)]

def fitness(individu):
    sample_distance = [list_distances[i] for i in individu]
    jumlah = reduce(add, sample_distance, 0)
    return jumlah

def selection(populasi):
    fitness_populasi = [ fitness(i) for i in populasi ]
    inverse_populasi = [ truediv(1, jumlah_individu) for jumlah_individu in fitness_populasi ]
    total_inverse = reduce(add, inverse_populasi, 0)
    probabilitas_populasi = [ truediv(inverse_individu, total_inverse) for inverse_individu in inverse_populasi ]
    """
    print fitness_populasi
    print inverse_populasi
    print total_inverse
    """
    return probabilitas_populasi

# membuat populasi baru
def roulettewheel(populasi):
    chromosom = selection(populasi)
    kumulatif_chromosom = [ reduce(add, chromosom[:i], 0) for i in range(len(chromosom)+1) ]
    kumulatif_chromosom.pop(0)
    print kumulatif_chromosom

    randomnum = []
    for i in range(6):
        randomnum.append(random.uniform(0.0, 1.0))
    # print randomnum
    print 'sebelum ditukar : ', chromosom
    print 'start'
    for j in range(len(kumulatif_chromosom)-1):
        if j == 0:
            kondisi = kumulatif_chromosom[j-1] < randomnum[j] and randomnum[j] < kumulatif_chromosom[j]
        else:
            kondisi = randomnum[j] < kumulatif_chromosom[j]

        print (kumulatif_chromosom[j-1], '<', randomnum[j]), (randomnum[j] , '<', kumulatif_chromosom[j] )
        if ( kondisi ):
            print j
            current_position = j
            temp = chromosom[j]
            chromosom[j] = chromosom[j+1]
            chromosom[j+1] = temp
    print 'end'
    print 'sesudah ditukar : ', chromosom
    return chromosom

    # new population
    # bandingkan randomnum dan kumulatif_chromosom

    # print chromosom

def crossover(chromosom, pc = 0.25):
    # dalam 1 generasi ada 2 * cp = crossover probability
    randomnum = []
    selectedrandomnum = []
    selectedrandomnumindex = []

    # pemilihan induk randomnum < pc
    for i in range(6):
        randomnum.append(random.uniform(0.0, 1.0))

    for j in range(len(randomnum)):
        if i < pc:
            selectedrandomnumindex.append(j)
            selectedrandomnum.append(randomnum[j])

    # posisi crossover : bilangan acak antara 1 s.d len(lebar kromosom)-1


def mutation(pm):
    pass

def evolve():
    # manggil crossover, mutation, etc
    pass
# setelah mutasi, hitung lagi fitness nya

# to understand random from a list
startPoint = 'A' # endPoint = 'A'
noOfPlaces = 6
target = 100
# populs = population(6, startPoint, noOfPlaces)

# print selection(sample_populasi)
print roulettewheel(sample_populasi)
# kalo udah ketemu nilai terendah,
# gimana caranya backtrack dapetin dari kota mana kemana?