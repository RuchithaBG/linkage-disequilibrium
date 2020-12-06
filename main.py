# LD

import random as rn

recom = 0.1
n_mates = 1
n_offsprings = 2 #  no. of offsprings per mating

# To be deleted later
F = ['A','B']
M_list = [['A','B'],['A','b'],['a','B'],['a','b']]

def mate(F, M_list, recom, n_mates, n_offsprings):
    z = []
    for i in range(n_mates):
        M = rn.choice(M_list)
        for j in range(n_offsprings):
            if rn.random() < recom:
                if rn.random() < 0.5:
                    z.append([F[0],M[1]])
                else:
                    z.append([M[0],F[1]])
            else:
                if rn.random() < 0.5:
                    z.append(F)
                else:
                    z.append(M)
    return(z, M)

print(mate(F, M_list, recom, n_mates, n_offsprings))
