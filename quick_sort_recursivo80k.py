passd = comps = trocas = None

def quick_sort80k(lista, ini = 0, fim = None):

    global passd, comps, trocas

    passd += 1

    if fim is None: fim = len(lista) - 1

    if fim <= ini: return

    pivot = fim    
    div = ini - 1  

    for pos in range(ini, fim):

        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1      
       
            if pos != div:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    div += 1

    comps += 1
    if lista[pivot] < lista[div]:
        lista[div], lista[pivot] = lista[pivot], lista[div]
        trocas += 1

    quick_sort80k(lista, ini, div - 1)
    quick_sort80k(lista, div + 1, fim) 

from time import time

def format_number(num):
    return "{:,}".format(num).replace(",", ".")

import sys, tracemalloc
sys.dont_write_bytecode = True      

from data.vehicles80k import vehicles80k

passd = comps = trocas = 0

tracemalloc.start()    
tempo_inicio = time()
quick_sort80k(vehicles80k)
tempo_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles80k)
print("------------------------------------------------------------------------------------------------------------")
print(f"Comparacoes: {format_number(comps)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Trocas: {format_number(trocas)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Passadas: {format_number(passd)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Tempo gasto: {tempo_fim - tempo_inicio:.4f} segundos")
print("------------------------------------------------------------------------------------------------------------")
print(f"Pico de memoria: {mem_pico / 1024 / 1024} MB")