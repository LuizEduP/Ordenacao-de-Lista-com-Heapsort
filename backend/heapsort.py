def heapify(array, n, i):
    maior = i      #inicializa com o maior numero como raiz
    esquerda = 2 * i + 1  # filho da esquerda
    direita = 2 * i + 2  #filho da direita

   #verifica se o numero da esquerda e maior do que a raiz
    if esquerda < n and array[esquerda] > array[maior]:
        maior = esquerda

    #verifica se o numero da esquerda e maior que o maior numero ate o momento
    if direita < n and array[direita] > array[maior]:
        maior = direita
   

    # Se o maior não for a raiz
    if maior != i:
        array[i], array[maior] = array[maior], array[i] # troca a raiz
        heapify(array, n, maior)  # Heapify a subárvore afetada

def heapsort(array):
    
    n = len(array)

     # Constrói o heap (reorganiza o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i] # troca
        heapify(array, i, 0)
        
    return array
    
#colocar a lista de numeros da requisicão http no array