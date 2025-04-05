divs = juncs = comps = None

def merge_sort40k(lista):

    global divs, juncs, comps

    if len(lista) <= 1: return lista

    meio = len(lista) // 2

    sublista_esq = lista[:meio]
    sublista_dir = lista[meio:]
    divs += 1

    sublista_esq = merge_sort40k(sublista_esq)
    sublista_dir = merge_sort40k(sublista_dir)

    pos_esq = pos_dir = 0

    ordenada, sobra = [], []

    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        comps += 1
    
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1

    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
    else: sobra = sublista_dir[pos_dir:]

    juncs += 1
    return ordenada + sobra

from time import time

import sys, tracemalloc
sys.dont_write_bytecode = True     

from data.vehicles40k import vehicles40k

divs = juncs = comps = 0

tracemalloc.start()    
tempo_inicio = time()
nomes_ord = merge_sort40k(vehicles40k)
tempo_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(nomes_ord)
print("------------------------------------------------------------------------------------------------------------")
print(f"Tempo gasto: {tempo_fim - tempo_inicio:.4f} segundos")
print("------------------------------------------------------------------------------------------------------------")
print(f"Pico de memoria: {mem_pico / 1024 / 1024} MB")