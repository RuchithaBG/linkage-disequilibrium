# LD

import random as rn
import matplotlib.pyplot as plt

recom = 0.1 #  Rate of recombination
n_mates = 1 #  No. of mates per female; male mating is not limited in this code
n_offsprings = 2 #  No. of offsprings per mating
N = 100 #  Population size before mixing
NoG = 4 # excluding parent generation
NoR = 10
sample_size = 2*N # here, all eggs are collected for next generation

X = [['A','B'] for i in range(N)] #  First population
Y = [['a','b'] for i in range(N)] #  Second population
Z = X +Y  # Combined population
G = [0 if i%2==0 else 1 for i in range(2*N)]  # anatomical sex (equal ratio)

# To be deleted later
#F = ['A','B']
#M_list = [['A','B'],['A','b'],['a','B'],['a','b']]

def mate(F, M_list, recom, n_mates, n_offsprings):
    z = []
    for i in range(n_mates):
        M = rn.choice(M_list)
        for j in range(n_offsprings):
            #  Deciding whether or not recombination occurs
            if rn.random() < recom:
                #  Deciding genotype of progeny after recombination
                if rn.random() < 0.5:
                    z.append([F[0],M[1]])
                else:
                    z.append([M[0],F[1]])
            else:
                #  Deciding genotype of progeny to resemble mother or father
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
    Z = rn.sample(Z, sample_size)
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

#  To be deleted later
# reps = [[[['A','B'],['A','B'],['a','b'],['a','b']],[['A','B'],['A','B'],
#           ['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']]],
#        [[['A','b'],['a','B'],['a','b'],['a','b']],[['A','B'],['A','B'],
#          ['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']]],
#        [[['A','B'],['A','B'],['a','b'],['a','b']],[['a','B'],['A','b'],
#          ['a','b'],['a','b']],[['A','B'],['A','B'],['a','b'],['a','b']]]]

#  Calculating proportion of recombinants per generation for all replicates
CR=[] #  List to append all replicates together
CG=[] #  List of proportion of recombinants present per generation
count_g = 0
for i in range(NoR):
    for j in range(NoG+1): #  To account for parent generation
        for k in range(2*N): #  Population size after mixing is 2N
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

#print(CR)

#  Plotting
for i in range(NoR):
    plt.plot(CR[i])
plt.xlabel('generations')
plt.ylabel('ratio')
plt.show()
plt.close()
