import json
from pprint import pprint

nama_file = 'data.json'
# nama_file = 'jogja.json'
# nama_file = 'bandung.json'
# nama_file = 'jakarta.json'
# nama_file = 'surabaya.json'

with open(nama_file) as data_file:
    json_data = json.load(data_file)
    if json_data['status'] == 'OK':
        for place in json_data['results']:
            print(place)
            # quit()
            print('%s:' %(place['name']))
            for key in place['geometry']['location']:
                print(place['geometry']['location'][key])
            for type in place['types']:
                print('%s' %(type))

"""
# to understand reduce function
from random import randint, random
from operator import add

def fitness(individual, target):
    sum = reduce(add, individual, 0)
    print target,"-",sum
    return abs(target-sum)

pop = [[1, 3, 2, 0], [1, 3, 2, 0]]
target = 2
list = [ i for i in pop ]
print list
# summed = reduce(add, (fitness(x, target) for x in pop), 0)

sum = reduce(add, (fitness(i, target) for i in pop ), 0)
print sum
# return abs(target-sum)
"""