def merge_sort_iteravivo20k(lista):

    tam_part = 1
    n = len(lista)
    
    while (tam_part < n):

        esq = 0
        while (esq < n):
            dir = min(esq + (tam_part * 2 - 1), n - 1)
            meio = (esq + dir) // 2

            if (tam_part > n // 2):
                meio = dir  - (n % tam_part)
            
            tam_esq = meio - esq + 1
            tam_dir = dir - meio
            lista_esq = [0] * tam_esq   
            lista_dir = [0] * tam_dir   
            for pos_esq in range(0, tam_esq):
                lista_esq[pos_esq] = lista[esq + pos_esq]
            for pos_esq in range(0, tam_dir):
                lista_dir[pos_esq] = lista[meio + pos_esq + 1]

            pos_esq, pos_dir, i = 0, 0, esq
            while pos_esq < tam_esq and pos_dir < tam_dir:
                if lista_esq[pos_esq] > lista_dir[pos_dir]:
                    lista[i] = lista_dir[pos_dir]
                    pos_dir += 1
                else:
                    lista[i] = lista_esq[pos_esq]
                    pos_esq += 1
                i += 1

            while pos_esq < tam_esq:
                lista[i] = lista_esq[pos_esq]
                pos_esq += 1
                i += 1

            while pos_dir < tam_dir:
                lista[i] = lista_dir[pos_dir]
                pos_dir += 1
                i += 1

            esq += tam_part * 2
        tam_part *= 2
    return lista

from time import time

def format_number(num):
    return "{:,}".format(num).replace(",", ".")

import sys, tracemalloc
sys.dont_write_bytecode = True   

from data.vehicles20k import vehicles20k

tracemalloc.start()     
tempo_inicio = time()
nomes_ord = merge_sort_iteravivo20k(vehicles20k)
tempo_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(nomes_ord)
print("------------------------------------------------------------------------------------------------------------")
print(f"Tempo gasto: {tempo_fim - tempo_inicio:.4f} segundos")
print("------------------------------------------------------------------------------------------------------------")
print(f"Pico de memoria: {mem_pico / 1024 / 1024} MB")