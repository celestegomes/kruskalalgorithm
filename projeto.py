#cria-se uma classe para as arestas que vai conter os vertices que ela interliga e o seu peso
class Aresta:
    def __init__ (self, vertices, peso): #recebe vertices em formato de lista com 2 itens e peso em formato de inteiro
        self.vertices = vertices
        self.peso = peso

#cria-se uma classe de vertices
class Vertices:
    def __init__(self):
        self.indice = 0
        self.adjacentes = []

#cria-se uma classe para o grafo
class Grafo:
    def __init__(self):
        #inerente a essa classe, temos a lista de arestas desordenadas e as ordenadas
        self.lista_arestas = []
        self.lista_vertices = []
        self.menor_grafo = []
        self.quantidade_arestas = 0
    
    #um criador de arestas
    def cria_aresta(self, x, y, w): #recebe os inteiros na ordem: vertice que inicia, vertice que termina e o peso
        vertices = [x, y]
        aresta = Aresta(vertices, w)
        self.lista_arestas.append(aresta)
    
    
    #agora se ordena a lista de arestas fazendo um quicksort
    def quickSort(self, lista, low, high):
        if low < high:
            pi = self.pedaco(lista, low, high)
            self.quickSort(lista, low, pi-1)
            self.quickSort(lista, pi+1 , high)

    def pedaco(self, lista, low, high):
        pivo = lista[low]
        i = low
        j = high +1
        aux = True
        while aux:
            i += 1
            aux2 = True
            while lista[i].peso < pivo.peso and aux2:
                if i >= high:
                    aux2 = False
                else:
                    i += 1
            aux2 = True
            j -= 1
            while lista[j].peso > pivo.peso and aux2:
                if j <= low:
                    aux2 = False
                else:
                    j -= 1
            if i >= j:
                aux = False
            else:
                lista[i], lista[j] = lista[j], lista[i]
        lista[low], lista[j] = lista[j], lista[low]
        return j
    
    #agora que a lista de arestas já está ordenada, aplicamos a ideia do kruskal em si
    def kruskal(self):
        lista_vertices = []
        for aresta in self.lista_arestas:
            if aresta.vertices[0] in lista_vertices and aresta.vertices[1] in lista_vertices:
                pass
            else:
                self.menor_grafo.append(aresta)
                if aresta[0] not in lista_vertices:
                    lista_vertices.append(aresta[0])
                if aresta[1] not in lista_vertices:
                    lista_vertices.append(aresta[1])
    
    #agora vamos criar algo para achar o menor caminho entre os vértices dados
    def cria_vertices(self):
        for aresta in self.menor_grafo:
            #separo os vertices que a aresta recebe
            x = int(aresta.vertices[0])
            y = int(aresta.vertices[1])
            #tento atribuir y como adjacente a x
            try :
                verticex = self.lista_vertices[x]
            except:
                falta = x - len(self.lista_vertices)
                self.lista_vertices.append(Vertices * falta)
                verticex = self.lista_vertices[x]
                verticex.indice = x
            try:
                verticey = self.lista_vertices[y]
            except:
                falta = y - len(self.lista_vertices)
                self.lista_vertices.append(Vertices * falta)
                verticey = self.lista_vertices[x]
                verticey.indice = y
            verticex.adjacentes.append(verticey)
            verticey.adjacentes.append(verticex)
    
    #agora vou criar uma recursiva pra procurar o caminho que chega de um ponto dado a outro nesse novo grafo criado
    def busca_caminhos(self, comeco, final, caminho = []):
        caminho = caminho + [comeco.indice]
        
        if comeco == final:
            return [caminho]
        
        if comeco not in self.lista_vertices:
            return []
        
        caminhos = []
        
        for node in comeco.caminhos:
            if node.nome not in caminho:
                novos_caminhos = self.busca_caminhos(node, final, caminho)
                if novos_caminhos != None:
                    for p in novos_caminhos:
                        caminhos.append(p)
        
        return caminhos
        
    #um metodo simples só para atribuir algumas variaveis e retornar meu resultado. recebe os dois pontos em numeros inteiros
    def cria_caminho(self, x, y):
        verticex = self.lista_vertices[x]
        verticey = self.lista_vertices[y]
        caminho = self.busca_caminhos(verticex, verticey)
        return caminho #esse metodo retorna uma lista com menor caminho de acordo com o algoritmo de kruskal
    
    #aqui dentro maria cria o metodo que faz o print, usando o metodo cria caminho para receber a lista do caminho

grafokruskal = Grafo()
#aqui maria adiciona o loop para criar as arestas
grafokruskal.quantidade_arestas = len(grafokruskal.lista_arestas)
grafokruskal.quickSort(grafokruskal.lista_arestas, 0, grafokruskal.quantidade_arestas - 1, 0)
#aqui maria cria o recebimento do input do caminho que queremos fazer, atribuindo x ao começo e y ao final
#aqui maria chama o metodo que faz o print para printar o menor caminho
