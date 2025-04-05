comps = trocas = passd = None 

def quick_sort40k(lista, ini=0, fim=None):
    global comps, trocas, passd 

    if fim is None:
        fim = len(lista) - 1
        comps = trocas = passd = 0 

    tamanho = fim - ini + 1
    aux = [None] * tamanho
    pos = -1
    pos = pos + 1
    aux[pos] = ini
    pos = pos + 1
    aux[pos] = fim

    while pos >= 0:
        passd += 1  

        fim = aux[pos]
        pos = pos - 1
        ini = aux[pos]
        pos = pos - 1

        i = ini - 1
        x = lista[fim]

        for j in range(ini, fim):
            comps += 1  
            if lista[j] <= x:
                i = i + 1
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1  

        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        trocas += 1  

        pivot = i + 1

        if pivot - 1 > ini:
            pos = pos + 1
            aux[pos] = ini
            pos = pos + 1
            aux[pos] = pivot - 1

        if pivot + 1 < fim:
            pos = pos + 1
            aux[pos] = pivot + 1
            pos = pos + 1
            aux[pos] = fim

from time import time
def format_number(num):
    return "{:,}".format(num).replace(",", ".")

import sys, tracemalloc
sys.dont_write_bytecode = True  
from data.vehicles40k import vehicles40k

passd = comps = trocas = 0  

tracemalloc.start()     
tempo_inicio = time()
quick_sort40k(vehicles40k)
tempo_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles40k)
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