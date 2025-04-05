divs = juncs = comps = None

def merge_sort80k(lista):
   
    global divs, juncs, comps

    if len(lista) <= 1: return lista

    meio = len(lista) // 2

    sublista_esq = lista[:meio]
    sublista_dir = lista[meio:]
    divs += 1

    sublista_esq = merge_sort80k(sublista_esq)
    sublista_dir = merge_sort80k(sublista_dir)

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

def format_number(num):
    return "{:,}".format(num).replace(",", ".")

import sys, tracemalloc
sys.dont_write_bytecode = True    

from data.vehicles80k import vehicles80k

divs = juncs = comps = 0

tracemalloc.start()     
tempo_inicio = time()
nomes_ord = merge_sort80k(vehicles80k)
tempo_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(nomes_ord)
print("------------------------------------------------------------------------------------------------------------")
print(f"Tempo gasto: {tempo_fim - tempo_inicio:.4f} segundos")
print("------------------------------------------------------------------------------------------------------------")
print(f"Pico de memoria: {mem_pico / 1024 / 1024} MB")