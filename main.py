# LD

import random as rn
import matplotlib.pyplot as plt

recom = 0.1
n_mates = 1
n_offsprings = 2 #  No. of offsprings per mating
N = 100 #  Population size before mixing
NoG = 4 # excluding parent generation
NoR = 3

X = [['A','B'] for i in range(N)]
Y = [['a','b'] for i in range(N)]
Z = X +Y  # combined population
G = [0 if i%2==0 else 1 for i in range(2*N)]  # anatomical sex

# To be deleted later
#F = ['A','B']
#M_list = [['A','B'],['A','b'],['a','B'],['a','b']]

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
    return(z)

def nextgen(Z, G, recom, n_mates, n_offsprings):
    M_list = [Z[i] for i in range(len(Z)) if G[i]==0]
    F_list = [Z[i] for i in range(len(Z)) if G[i]!=0]
    Z = []
    for i in range(len(F_list)):
        Z += mate(F_list[i], M_list, recom, n_mates, n_offsprings)
    return(Z)

def timeseries(NoG, Z, G, recom, n_mates, n_offsprings):
    pop = [Z]
    for i in range(NoG):
        pop += [nextgen(Z, G, recom, n_mates, n_offsprings)]
    return(pop)

def replicates(NoR, NoG, Z, G, recom, n_mates, n_offsprings):
    reps = []
    for i in range(NoR):
        reps += [timeseries(NoG, Z, G, recom, n_mates, n_offsprings)]
    return(reps)

reps = replicates(NoR, NoG, Z, G, recom, n_mates, n_offsprings)

# reps = [[[['A','B'],['A','B'],['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']]],
#        [[['A','b'],['a','B'],['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']]],
#        [[['A','B'],['A','B'],['a','b'],['a','b']],[['a','B'],['A','b'],['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']]]]

CR=[]
CG=[]
count_g = 0
for i in range(NoR):
    for j in range(NoG+1):
        for k in range(2*N):
            if reps[i][j][k][0] == 'A' and reps[i][j][k][1] == 'b':
                count_g += 1
            elif reps[i][j][k][0] == 'a' and reps[i][j][k][1] == 'B':
                count_g += 1
            else:
                continue
        CG.append(count_g/(2*N))
        count_g = 0
    CR.append(CG)
    CG = []

print(CR)

for i in range(NoR):
    plt.plot(CR[i])
plt.show()
plt.close()
