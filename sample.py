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

def fitness(individu):
    sample_distance = [list_distances[i] for i in individu]
    jumlah = reduce(add, sample_distance, 0)
    return jumlah

def selection(populasi):
    # call fitness
    fitness_populasi = [ fitness(i) for i in populasi ]
    inverse_populasi = [ truediv(1, item_fitness) for item_fitness in fitness_populasi ]
    total_probability = reduce(add, inverse_populasi, 0)
    probabilitas_populasi = [ truediv(inverse_individu, total_probability) for inverse_individu in inverse_populasi ]
    return probabilitas_populasi

# membuat populasi baru
def roulettewheel(populasi):
    # call selection
    probabilitas_populasi = selection(populasi)
    kumulatif_probabilitas = [ reduce(add, probabilitas_populasi[:i], 0) for i in range(len(probabilitas_populasi)+1) ]
    randomnum = [random.uniform(0.0, 1.0) for p in range(0, len(probabilitas_populasi))]

    populasi_baru = []
    probabilitas_populasi_baru = []
    for j in range(len(kumulatif_probabilitas)-1):
        for k in range(len(randomnum)):
            if ((randomnum[k] > kumulatif_probabilitas[j]) and (randomnum[k] <= kumulatif_probabilitas[j+1])):
                populasi_baru.append(populasi[k])
                probabilitas_populasi_baru.append(probabilitas_populasi[k])

    # return probabilitas_populasi_baru, populasi_baru
    return populasi_baru

def crossover(swapped_populasi, pc):
    # pc = probability_of_crossover
    joined_swapped_populasi = konversi_separated_joined(swapped_populasi, startPoint)

    # dalam 1 generasi ada 2 * pc = probability_of_crossover -> menentukan berapa persen dari chromosom yang harus di crossover
    crossover_portion = int(round(2 * pc * len(swapped_populasi)))
    position_to_crossover = 2

    randomnum = []
    # pemilihan induk randomnum < pc
    for i in range(crossover_portion):
        randomnum.append(random.uniform(0.0, pc))
    for i in range(len(swapped_populasi)-crossover_portion):
        randomnum.append(random.uniform(pc, 1.0))
    random.shuffle(randomnum)

    index_joined_swapped_populasi_crossover = [i for i,v in enumerate(randomnum) if v < pc]
    for index, value in enumerate(index_joined_swapped_populasi_crossover):
        father = joined_swapped_populasi[value]

        if index < len(index_joined_swapped_populasi_crossover)-1:
            mother = joined_swapped_populasi[index_joined_swapped_populasi_crossover[index+1]]
        else:
            # jika index = maksimal dari lebar data, mother dari indeks 0
            mother = joined_swapped_populasi[index_joined_swapped_populasi_crossover[0]]

        new_individu = []
        for item in father[:position_to_crossover]:
            new_individu.append(item)

        for item in mother:
            if item not in new_individu:
                new_individu.append(item)

        joined_mutated_populasi = ''.join(new_individu)
        # replace value ke index awal
        joined_swapped_populasi[index] = joined_mutated_populasi

    return joined_swapped_populasi

def genemutation(joined_swapped_populasi, pm):
    # pm = parameter of mutation
    length_of_individu = len(joined_swapped_populasi[0])
    length_of_gene = len(joined_swapped_populasi) * length_of_individu
    number_of_genemutation = int(round(pm * length_of_gene))
    position_of_genemutation = [random.randrange(0, length_of_individu-2) for p in range(0, number_of_genemutation)]

    # proses swap gen sesuai index random yang terpilih
    for index, value in enumerate(position_of_genemutation):
        a = list(joined_swapped_populasi[index])
        temp = a[value]
        a[value] = a[value+1]
        a[value+1] = temp
        joina = ''.join(a)

        joined_swapped_populasi[index] = joina

    # print("sesudah swapping", sample_populasi_lokasi)
    return joined_swapped_populasi

def konversi_separated_joined(separated, startPoint):
    # proses dapetin huruf asli
    joined = []
    for gene in separated:
        foo = ''.join(gene)
        joined.append(''.join([j for i,j in enumerate(foo) if j not in foo[:i] and j != startPoint]))
    return joined

def konversi_joined_separated(noOfPlaces, startPoint):
    # print(noOfPlaces)
    list_places = []
    for index in range(len(noOfPlaces)):
        x = noOfPlaces[index]
        places = []
        for i in range(len(x)):
            if i == 0:
                places.append(startPoint+x[i])
            if i < (len(x)-1):
                places.append(x[i]+x[i+1])
            else:
                places.append(x[i]+startPoint)
        list_places.append(places)
    return list_places

startPoint = 'A'
noOfPlaces = 6
noOfPopulation = 80
generasi = 2000
gap_antar_generasi = 100
history_roulettewheel = []
history_populasi = []
generatepopulasi = population(noOfPopulation, startPoint, noOfPlaces)

for i in range(generasi):
    if i == 0:
        # pake sample populasi awal
        populasi = generatepopulasi
    else:
        # pake hasil iterasi
        populasi = new_populasi

    history_populasi.append(populasi)
    result_roulettewheel = roulettewheel(populasi)
    new_order_populasi = result_roulettewheel
    result_crossover = crossover(new_order_populasi, 0.25)
    result_genemutation = genemutation(result_crossover, 0.20)
    new_populasi = konversi_joined_separated(result_crossover, startPoint)

# print(history_populasi)
for i in range(0, len(history_populasi), gap_antar_generasi):
    print('generasi ke : ', int(i+gap_antar_generasi))
    hitung_fitness = [ fitness(item_history_populasi) for item_history_populasi in history_populasi[i] ]
    index = hitung_fitness.index(min(hitung_fitness))
    # print "fitness generasi : ", hitung_fitness
    print('index fitness terendah : ', hitung_fitness.index(min(hitung_fitness)))
    print('nilai fitness terendah : ', hitung_fitness[index])
    print('rute dengan fitness terendah : ', history_populasi[i][index])
    print('\n')
    # kenapa ada individu yang kota-nya < 6 bisa ter-generate oleh sistem ya?
    # tampilkan 5 rekomendasi nilai terbaik aja