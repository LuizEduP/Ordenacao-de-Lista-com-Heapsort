# Função para reorganizar a árvore para manter a propriedade do heap
def heapify(array, n, i):
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1  # Índice do filho esquerdo
    direita = 2 * i + 2  # Índice do filho direito

    # Verifica se o filho esquerdo é maior que o nó atual
    if esquerda < n and array[esquerda] > array[maior]:
        maior = esquerda

    # Verifica se o filho direito é maior que o maior número até o momento
    if direita < n and array[direita] > array[maior]:
        maior = direita

    # Se o maior não for a raiz, realiza a troca e faz o heapify na subárvore afetada
    if maior != i:
        array[i], array[maior] = array[maior], array[i]
        heapify(array, n, maior)

# Função de ordenação usando Heapsort
def heapsort(array):
    n = len(array)

    # Construa o heap (reorganiza a árvore) de forma a garantir que o maior valor esteja no topo
    for i in range(n // 2 - 1, -1, -1):  # Percorre os nós internos do heap
        heapify(array, n, i)

    # Extrai os elementos do heap e os coloca na posição correta
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Troca o maior valor com o último valor
        heapify(array, i, 0)  # Refaz o heapify no restante da lista

    return array
