import time

start = time.time()
list1 = []
for i in range(100000):
    list1.append(i ** 2)
    list1
end = time.time()
# print(end-start)

# consiste à  intégrer un for dans une liste vide
start = time.time()
list2 = [i ** 2 for i in range(100000)]
list2
end = time.time()
# print(end-start)

# nested list: une liste dans une liste
# list3 = [i for i in range(3)] #[0, 1, 2]
list3 = [[i for i in range(3)] for j in range(3)]   #[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# print(list3)

# dictionnaire comprehension
dictionnaire = {
    '0': "Valérie",    
    '1': "Bilal",
    '2': "Nawal",
    '3': "roucky"
}

prenoms = ["Valérie", "Bilal", "Nawal","roucky"]

dico = {k:v for k, v in enumerate(prenoms)}
print(dico) #{0: 'Valérie', 1: 'Bilal', 2: 'Nawal', 3: 'roucky'}
print(dico.keys(), dico.values(), len(dico),"éléments")

ages = [49,21,19,13]
dico_2 = {prenoms:ages for prenoms,ages in zip(prenoms,ages)} 
# print(dico_2)   #{'Valérie': 49, 'Bilal': 21, 'Nawal': 19, 'roucky': 13}


# inclure des conditions après le for
dico_2 = {prenoms:ages for prenoms,ages in zip(prenoms,ages) if ages > 30 } 
print(dico_2)  #{'Valérie': 49}


# tupples comprehension
# tuple1 = (i**2 for i in range(10))
# print(tuple1)   #crée un générateur: <generator object <genexpr> at 0x0000026305DD4040>

tuple1 = tuple(i**2 for i in range(10))
print(tuple1)   #(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
