# 🔍 Comparativo de Algoritmos de Ordenação

![Sorting Algorithms](https://img.shields.io/badge/ANÁLISE_DE_EFICIÊNCIA-00bfbf?style=for-the-badge) 
![Java](https://img.shields.io/badge/Linguagem-Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Data Size](https://img.shields.io/badge/Dados-10k→80k_elementos-00bfbf?style=for-the-badge)

Análise comparativa do desempenho dos principais algoritmos de ordenação com diferentes tamanhos de datasets.

## 📊 Algoritmos Analisados

| Algoritmo        | Tipo          | Complexidade (Pior Caso) |
|------------------|---------------|--------------------------|
| Bubble Sort      | Iterativo     | O(n²)                    |
| Selection Sort   | Iterativo     | O(n²)                    |
| Merge Sort       | Recursivo     | O(n log n)               |
| Merge Sort       | Iterativo     | O(n log n)               |
| Quick Sort       | Recursivo     | O(n²)                    |
| Quick Sort       | Iterativo     | O(n²)                    |

## � Métricas de Análise

<div align="center">
  <img src="https://img.shields.io/badge/Tempo_de_Execução-00bfbf?style=flat-square">
  <img src="https://img.shields.io/badge/Uso_de_Memória-00bfbf?style=flat-square">
  <img src="https://img.shields.io/badge/Passadas-00bfbf?style=flat-square">
  <img src="https://img.shields.io/badge/Comparações-00bfbf?style=flat-square">
  <img src="https://img.shields.io/badge/Trocas-00bfbf?style=flat-square">
</div>

## 📌 Principais Insights

### 🏆 Melhor Performance Geral
![Merge Sort](https://img.shields.io/badge/Merge_Sort-6DB33F?style=for-the-badge)
- **Tempo de execução**: Mais eficiente com grandes volumes (10k-80k elementos)
- **Complexidade consistente**: O(n log n) em todos os casos

### ⚡ Algoritmo Mais Eficiente em Operações
![Quick Sort](https://img.shields.io/badge/Quick_Sort_Iterativo-FF6F00?style=for-the-badge)
- Menor número de passadas e comparações
- Performance próxima ao Merge Sort em tempo de execução

### 💾 Economia em Trocas
![Selection Sort](https://img.shields.io/badge/Selection_Sort-00599C?style=for-the-badge)
- Número de trocas significativamente menor
- Apesar da complexidade O(n²)

### 📉 Menor Performance
![Bubble Sort](https://img.shields.io/badge/Bubble_Sort-DD0031?style=for-the-badge)
- Piores resultados em tempo de execução
- Maior número de trocas
- **Vantagem**: Baixo consumo de memória

## 📈 Resultados Detalhados

```java
// Exemplo de cabeçalho de saída do programa
[INFO] Dataset: 50.000 elementos
| Algoritmo        | Tempo (ms) | Memória (MB) | Trocas  | Comparações |
|------------------|------------|--------------|---------|-------------|
| MergeSortRec     | 120        | 45           | 245,112 | 1,043,221   |
| QuickSortIter    | 115        | 40           | 310,455 | 892,334     |
| SelectionSort    | 2,450      | 38           | 49,999  | 1,249,975   |
| BubbleSort       | 3,210      | 35           | 624,332 | 1,249,975   |
