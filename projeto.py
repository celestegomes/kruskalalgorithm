#cria-se uma classe para as arestas que vai conter os vertices que ela interliga e o seu peso
class Aresta:
    def __init__ (self, vertices, peso): #recebe vertices em formato de lista com 2 itens e peso em formato de inteiro
        self.vertices = vertices
        self.peso = peso

#cria-se uma classe de vertices
class Vertices:
    def __init__(self, lista):
        self.indice = 0
        self.adjacentes = lista

#cria-se uma classe para o grafo
class Grafo:
    def __init__(self):
        #inerente a essa classe, temos a lista de arestas desordenadas e as ordenadas
        self.lista_arestas = []
        self.lista_vertices = []
        self.menor_grafo = []
        self.quantidade_arestas = 0
        self.caminho = []
    
    #um criador de arestas
    def cria_aresta(self, u, v, w): #recebe os inteiros na ordem: vertice que inicia, vertice que termina e o peso
        vertices = [u, v]
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
            while lista[i].peso > pivo.peso and aux2:
                if i >= high:
                    aux2 = False
                else:
                    i += 1
            aux2 = True
            j -= 1
            while lista[j].peso < pivo.peso and aux2:
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
                if aresta.vertices[0] not in lista_vertices:
                    lista_vertices.append(aresta.vertices[0])
                if aresta.vertices[1] not in lista_vertices:
                    lista_vertices.append(aresta.vertices[1])
    
    #agora vamos criar algo para achar o menor caminho entre os vértices dados
    def cria_vertices(self):
        for aresta in self.menor_grafo:
            #separo os vertices que a aresta recebe
            x = int(aresta.vertices[0])
            y = int(aresta.vertices[1])
            #tento atribuir y como adjacente a x
            try :
                verticex = self.lista_vertices[x]
                verticex.indice = x
            except:
                falta = (x - len(self.lista_vertices)) + 1
                for i in range (falta):
                    vertice = Vertices([])
                    self.lista_vertices.append(vertice)
                verticex = self.lista_vertices[x]
                verticex.indice = x
            try:
                verticey = self.lista_vertices[y]
                verticey.indice = y
            except:
                falta = (y - len(self.lista_vertices))+1
                for i in range (falta):
                    vertice = Vertices([])
                    self.lista_vertices.append(vertice)
                verticey = self.lista_vertices[y]
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
        
        for node in comeco.adjacentes:
            if node.indice not in caminho:
                novos_caminhos = self.busca_caminhos(node, final, caminho)
                if novos_caminhos != None:
                    for p in novos_caminhos:
                        self.caminho.append(p)
        
    #um metodo simples só para atribuir algumas variaveis e retornar meu resultado. recebe os dois pontos em numeros inteiros
    def cria_caminho(self, x, y):
        verticex = self.lista_vertices[x]
        verticey = self.lista_vertices[y]
        self.caminho = []
        self.busca_caminhos(verticex, verticey)

    #metodo que faz o print, usando o metodo cria caminho para receber a lista do caminho
    def imprime(self, x, y):
        self.cria_caminho(x, y)
        print(f"O menor caminho do ponto {x} até o ponto {y} é {self.caminho}.")

grafokruskal = Grafo()

#loop para criar as arestas
start = True
dados = open('reachability.txt', 'r')
while start:
    try:
        for i in dados:
            entrada1 = i.split(" ")
            u = int(entrada1[0])
            v = int(entrada1[1])
            w = int(entrada1[2])
            grafokruskal.cria_aresta(u, v, w)
        start = False

    except EOFError:
        start = False

grafokruskal.quantidade_arestas = len(grafokruskal.lista_arestas)
grafokruskal.quickSort(grafokruskal.lista_arestas, 0, grafokruskal.quantidade_arestas - 1)
grafokruskal.kruskal()
grafokruskal.cria_vertices()

#input do caminho que queremos fazer, atribuindo x ao começo e y ao final
x_y = input("Insira dois números inteiros separados por - onde o primeiro é o ponto inicial e o segundo o ponto final:\n").split("-")
x = int(x_y[0])
y = int(x_y[1])

#printa o menor caminho
grafokruskal.imprime(x, y)
