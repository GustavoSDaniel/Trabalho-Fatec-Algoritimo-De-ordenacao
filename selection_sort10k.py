comps = trocas = passd = None

def selection_sort10k(lista):

    global comps, trocas, passd
    comps = trocas = passd = 0

    for pos_sel in range(len(lista) - 1):

        passd += 1
        pos_menor = pos_sel + 1

        for pos in range(pos_menor + 1, len(lista)):
 
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

from time import time

def format_time(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes} minutos e {remaining_seconds:.2f} segundos"

import sys
sys.dont_write_bytecode = True   

from data.vehicles10k import vehicles

def format_number(num):
    return "{:,}".format(num).replace(",", ".")

def format_time(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes} minutos e {remaining_seconds:.2f} segundos"

def get_memory_usage():
    try:
        import resource
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    except:
        try:
            import psutil
            process = psutil.Process()
            return process.memory_info().rss / 1024  # KB
        except:
            return 0


import sys, tracemalloc
sys.dont_write_bytecode = True  
tracemalloc.start()    

tempo_inicio = time()

selection_sort10k(vehicles)

tempo_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)
print("------------------------------------------------------------------------------------------------------------")
print(f"Comparacoes: {format_number(comps)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Trocas: {format_number(trocas)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Passadas: {format_number(passd)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Tempo gasto: {format_time(tempo_fim - tempo_inicio)}")
print("------------------------------------------------------------------------------------------------------------")
print(f"Pico de memoria: {mem_pico / 1024 / 1024} MB")