import streamlit as st
import random
import matplotlib.pyplot as plt

# --- Interface de Parâmetros ---
st.title("Algoritmo Genético para Alocação de Tarefas em Máquinas")

NUM_TAREFAS = st.slider("Número de Tarefas", 100, 2000, 500, 100)
NUM_MAQUINAS = st.slider("Número de Máquinas", 2, 50, 10)
TAMANHO_POPULACAO = st.slider("Tamanho da População", 10, 300, 50, 10)
GERACOES = st.slider("Número de Gerações", 10, 500, 100, 10)
TAXA_CROSSOVER = st.slider("Taxa de Crossover", 0.0, 1.0, 0.8, 0.05)
TAXA_MUTACAO = st.slider("Taxa de Mutação", 0.0, 0.5, 0.1, 0.01)
MELHORADO = st.checkbox("Usar Avaliação Melhorada (desvio balanceado)")

# --- Geração de tarefas ---
tarefas = [random.randint(1, 15) for _ in range(NUM_TAREFAS)]

# --- Criação e avaliação ---
def criar_individuo():
    return [random.randint(0, NUM_MAQUINAS - 1) for _ in range(NUM_TAREFAS)]

def avaliar_classico(individuo):
    maquinas = [0] * NUM_MAQUINAS
    for i, m in enumerate(individuo):
        maquinas[m] += tarefas[i]
    return max(maquinas)

def avaliar_melhorado(individuo):
    maquinas = [0] * NUM_MAQUINAS
    for i, m in enumerate(individuo):
        maquinas[m] += tarefas[i]
    makespan = max(maquinas)
    media = sum(maquinas) / NUM_MAQUINAS
    desvio = sum(abs(x - media) for x in maquinas) / NUM_MAQUINAS
    return makespan + 0.1 * desvio

def selecao(populacao, func_avaliar):
    a, b = random.sample(populacao, 2)
    return a if func_avaliar(a) < func_avaliar(b) else b

def aplicar_crossover(pai1, pai2):
    if random.random() < TAXA_CROSSOVER:
        p1, p2 = sorted(random.sample(range(NUM_TAREFAS), 2))
        return pai1[:p1] + pai2[p1:p2] + pai1[p2:]
    return pai1[:]

def aplicar_mutacao(individuo, guiada=False):
    num_mutacoes = int(NUM_TAREFAS * TAXA_MUTACAO)
    for _ in range(num_mutacoes):
        idx = random.randint(0, NUM_TAREFAS - 1)
        if guiada:
            cargas = [0] * NUM_MAQUINAS
            for i, m in enumerate(individuo):
                cargas[m] += tarefas[i]
            melhor_maquina = cargas.index(min(cargas))
            individuo[idx] = melhor_maquina
        else:
            individuo[idx] = random.randint(0, NUM_MAQUINAS - 1)
    return individuo

def criar_populacao():
    pop = [criar_individuo() for _ in range(TAMANHO_POPULACAO - 5)] if MELHORADO else [criar_individuo() for _ in range(TAMANHO_POPULACAO)]
    if MELHORADO:
        base = solucao_greedy()
        for _ in range(5):
            pop.append(aplicar_mutacao(base[:], guiada=True))
    return pop

def solucao_greedy():
    maquinas = [0] * NUM_MAQUINAS
    individuo = []
    for t in tarefas:
        idx = maquinas.index(min(maquinas))
        maquinas[idx] += t
        individuo.append(idx)
    return individuo

# --- EXECUTAR AG ---
if st.button("Executar Algoritmo Genético"):
    func_avaliar = avaliar_melhorado if MELHORADO else avaliar_classico
    populacao = criar_populacao()
    melhor = min(populacao, key=func_avaliar)
    historico = [func_avaliar(melhor)]

    for ger in range(GERACOES):
        nova_pop = [melhor]
        while len(nova_pop) < TAMANHO_POPULACAO:
            p1 = selecao(populacao, func_avaliar)
            p2 = selecao(populacao, func_avaliar)
            filho = aplicar_crossover(p1, p2)
            filho = aplicar_mutacao(filho, guiada=MELHORADO)
            nova_pop.append(filho)
        populacao = nova_pop
        melhor_atual = min(populacao, key=func_avaliar)
        if func_avaliar(melhor_atual) < func_avaliar(melhor):
            melhor = melhor_atual
        historico.append(func_avaliar(melhor))

    st.success(f"Melhor Fitness Final: {func_avaliar(melhor):.2f}")

    st.line_chart(historico, height=400)

    st.write("**Última geração (melhor indivíduo):**")
    st.json(melhor[:50])  # Exibir parte do vetor (pode ser grande)
