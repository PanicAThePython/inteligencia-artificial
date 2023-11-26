import random
import numpy as np

data = np.loadtxt('cidades.mat')

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

population = []
roulette_chances = []
cities = {}
distances = {}

# Setup section

# Inicializa as cidades 
def generate_cities():
    for i in range(0, 20):
        x = data[0][i]
        y = data[1][i]
        city = City(x, y)
        cities[i+1] = city

# Inicializa a população com valores aleatórios
def generate_population():
    for _ in range(0, 20):
        gene = list(range(1,21))
        random.shuffle(gene)
        population.append(gene)

# Gera os valores da roleta   
def roulette():
    global roulette_chances
    value = 10

    for i in range(1, 11):
        for _ in reversed(range(i)):
            roulette_chances.append(value)
        value -= 1

generate_cities()
generate_population()
roulette()

# end section

def distance(city1, city2):
    return np.sqrt((city2.x - city1.x)**2+(city2.y - city2.x)**2)

def calc_distance():
    global distances
    dist = 0
    # print(population)
    for chromosome in population:
        for i in range(0, len(chromosome)):
            if i == len(chromosome) - 1:
                dist += distance(cities[chromosome[-1]], cities[chromosome[0]])
            else:
                dist += distance(cities[chromosome[i]], cities[chromosome[i+1]])
        distances[population.index(chromosome)] = dist
        dist = 0

calc_distance()

# Organiza a população com os 10 melhores cromossomos 
def sort_population():
    global population
    temp = []

    for i in sorted(distances, key=distances.get):
        temp.append(population[i])

    population = temp[0 :10]
    # for i in population:
    #     print(i)
        
# sort_population()

def swap_gene(p1, p2, index):
    gene = p1[index]
    p1[index] = p2[index]
    p2[index] = gene

    return p1, p2

def check_repeated(p1, gene, index):
    for i, el in enumerate(p1):
        if (el == gene and i != index):
            return True, i
    return False, None

def mutation(chromosome):
    index = random.sample(range(0, len(chromosome)), 2)
    gene1 = chromosome[index[0]]
    gene2 = chromosome[index[1]]

    chromosome[index[1]] = gene1
    chromosome[index[0]] = gene2

    return chromosome

def crossing_over(p1, p2):
    first_cut = random.randint(0, 9)
    p1, p2 = swap_gene(p1, p2, first_cut)

    gene_repeated, first_index = check_repeated(p1, p1[first_cut], first_cut)

    if (gene_repeated):
        while(gene_repeated):
            p1, p2 = swap_gene(p1, p2, first_index)

            gene_repeated, index = check_repeated(p1, p1[first_index], first_index)
            first_index = index

    population.append(mutation(p1))
    population.append(mutation(p2))

def choose_parents():
    i = 0
    while (i < 5):
        roulette_copy = roulette_chances[:]
        p1 = random.choice(roulette_copy)
        roulette_copy = list(filter((p1).__ne__, roulette_copy))
        p2 = random.choice(roulette_copy)

        parent1 = population[p1-1].copy()
        parent2 = population[p2-1].copy()

        crossing_over(parent1, parent2)
        i += 1

if __name__ == '__main__':
    i = 0
    print(distances)
    while (i < 20000):
        calc_distance()
        sort_population()
        choose_parents()
        i += 1 

    print(distances)

def returnTotalDistance(distances):
    total = 0
    for i in distances:
        total = total + distances[i]
    return total

def printDistances(distances):
    print('{')
    for i in distances:
        print(str(i) + ':' + str(distances[i]) + ',')
    print('}')

print('---------------------------------')
print('Tamanho da população:          '+str(len(population)))
print('Taxa de mutação:               5%')
print('Número de cidades:             '+str(len(cities)))
print('Melhor custo:  '+str(returnTotalDistance(distances)))
print('Melhor solução: ')
printDistances(distances)