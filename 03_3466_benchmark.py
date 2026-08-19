import AulasPraticas.AP_03_ordenacao as ap3
import sys
import random
import time
import pandas as pd
sys.setrecursionlimit(10**6)



def avg_case(N):
    my_list = []
    og = [x for x in range(N)]
    while len(og):
        random_index = random.randint(0,len(og)-1)
        my_list.append(og[random_index])
        og[random_index], og[-1] = og[-1], og[random_index]
        og.pop(-1)
    return my_list

def worst_case(N):
    return [x for x in range(N)]

def prf_algo(sort_algo,N,k,worst = False):
    times = []
    for _ in range(k):
        my_list = avg_case(N) if not worst else worst_case(N)
        start_t = time.perf_counter()
        sort_algo(my_list)
        end_t = time.perf_counter()
        times.append(end_t - start_t)
    return sum(times)/k

tempos = []
nomes = []

for i in [ap3.selection_sort,ap3.divide_and_conquer_sort,ap3.quick_sort]:
    for j in [1000,5000,10000]:
        tempos.append(prf_algo(i,j,50),prf_algo(i,j,50,True))
        nome = i.split(".")[1]
        nomes.append(nome,nome+"_worst")
        

df = pd.DataFrame()

# Add Hours column, starting trom zero, ending at 15 with step size of 5
df['Hours(n)'] = range(0,16,5)

# Calcualtion total number using hours
df['Total number'] = 200* 2**(df['Hours(n)'])

#show dataframe
print(df)