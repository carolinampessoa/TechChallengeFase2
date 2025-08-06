# TechChallengeFase2


# 🧠 Alocação de Tarefas com Algoritmos Genéticos

Este projeto apresenta uma solução para o **Tech Challenge da Fase 2** da **pós-graduação em Inteligência Artificial para Devs da FIAP**. O desafio consiste em resolver o problema de alocação de tarefas em máquinas de forma eficiente, minimizando o tempo total da máquina mais sobrecarregada (makespan), usando técnicas de **Algoritmos Genéticos (AG)**.

---

## 🎯 Descrição do Problema

Dado um conjunto de `n` tarefas, cada uma com um tempo de processamento, e `m` máquinas idênticas, o objetivo é **distribuir as tarefas entre as máquinas de modo que o tempo da máquina mais carregada (makespan) seja o menor possível**.

Esse é um problema clássico em contextos de:

- Escalonamento (Scheduling)
- Balanceamento de carga (Load Balancing)
- 
A complexidade é exponencial: o número de combinações possíveis de alocação é \( m^n \).

---

## 🧪 Estratégia de Solução

Utilizamos um **Algoritmo Genético (AG)** com os seguintes componentes:

- **Geração de população inicial**: aleatória ou heurística
- **Função de aptidão (fitness)** baseada no makespan
- **Operadores genéticos**:
  - Seleção
  - Crossover
  - Mutação (com taxa ajustável)
- **Elitismo**: preservação dos melhores indivíduos
- **Comparação com heurística greedy** como baseline
---

## 📈 Resultados

O notebook gera:

- **Gráfico de convergência** (evolução do melhor makespan por geração)
- **Comparações de desempenho** entre o algoritmo genético e soluções gulosas

---

## 💻 Tecnologias Utilizadas

- Python 3
- NumPy
- Matplotlib
- Jupyter Notebook

---

## ▶️ Como Executar

Execute o notebook:
Abra `TechChallengeFase2.ipynb` com Jupyter Notebook ou Jupyter Lab e execute as células em ordem.

---

## 👥 Integrantes do Grupo

- Marcelo Guedes de Barros  
- Jadson Dantas de Medeiros Junior  
- Carolina de Marco Pessoa  
- João Mário Künzle Ribeiro Magalhães  
