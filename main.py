#import dictionaries
import pandas as pd
import pulp as pl
import math
import random

def covid_main():
    data = pd.read_csv("C:\\Users\\Rishi Mehdiratta\\Desktop\\Book2.csv")
    cord_c = data.loc[0:8, "Coordinates_c"]
    cord_f = data.loc[0:22, "Coordinates_f"]

    C = [i for i in range(9)]
    print(C)
    print(len(C))
    Ff = [j for j in range(23)]
    Ft = [k for k in range(9)]
    Fe = [l for l in range(14)]
    distance = {}
    for i in range(len(C)):
        for j in range(len(Ff)):
            distance[i,j] = math.dist(eval(cord_c[i]), eval(cord_f[j]))

    cap_t = 100
    cost_t = 5, 00, 000
    D_i = data.loc[0:9, "Demand"]
    cap_f = data.loc[0:23,"Capacity"]
    cap_e = data.loc[0:15, "Existing"]
    cap_t = data.loc[15:23, "Existing"]
    bigM = random.randrange(2000)
    dCost = 5
    X = {}
    for t in range(len(Ft)):
        X[t] = pl.LpVariable("X_" + str(t), cat = "Binary")
    N1 = {}
    for i in range(len(C)):
        for f in range(len(Ff)):
            N1[i,f] = pl.LpVariable("N_" + str(i) + "_" + str(f), cat = "Integer")
    N2 = {}
    for i in range(len(C)):
        for e in range(len(Fe)):
            N2[i,e] = pl.LpVariable("N_" + str(i) + "_" + str(e), cat = "Integer")
    N3 = {}
    for i in range(len(C)):
        for t in range(len(Ft)):
            N3[i,t] = pl.LpVariable("N_" + str(i) + "_" + str(t), cat = "Integer")
    Z = {}
    for t in range(len(Ft)):
        Z[t] = pl.LpVariable("Z_" + str(t), cat = "Integer")

    prob = pl.LpProblem("Covid-19-Facility-Location-Problem", pl.LpMinimize)

    aux_sum1 = 0
    for i in range(len(C)):
        for j in range(len(Ff)):
            aux_sum1 += (dCost * N1[i,f] * distance[i,f])
    aux_sum2 = 0
    for t in range(len(Ft)):
        aux_sum2 += X[t]
    aux_sum3 = aux_sum2 * cost_t
    aux_sum4 = 0
    for t in range(len(Ft)):
        aux_sum4 += Z[t]
    aux_sum = aux_sum1 + aux_sum3 + aux_sum4

    prob += aux_sum

    for c in range(len(C)):
        aux_sum5 = 0
        for f in range(len(Ff)):
            aux_sum5 += N1[i,f]
        prob+= aux_sum5 <= cap_f[f]

    for i in range(len(C)):
        aux_sum6 = 0
        for e in range(len(Fe)):
            aux_sum6 += N2[i,e]
        prob+= aux_sum6 <= cap_e[e]

    for t in range(len(Ft)):
        aux_sum7 = 0
        for i in range(len(Ft)):
            aux_sum7 += N3[i,t]
        prob+= aux_sum7 <= (cap_t[t] * X[t] + Z[t])

    print(prob)

covid_main()