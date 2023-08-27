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
        self.lista_vertices_menor = []
        self.menor_grafo = []
        self.quantidade_arestas = 0
    
    #um criador de arestas
    def cria_aresta(self, u, v, w): #recebe os inteiros na ordem: vertice que inicia, vertice que termina e o peso
        vertices = [u, v]
        aresta = Aresta(vertices, w)
        self.lista_arestas.append(aresta)
    
    #função sort
    def sorteando(self, lista):
        def peso(e):
            return e.peso
        lista.sort(key=peso)
    
    #função sort pro menor grafo
    def sorteando(self, lista):
        def indice(e):
            return e.vertices[0]
        lista.sort(key=indice)
    
    #agora que a lista de arestas já está ordenada, aplicamos a ideia do kruskal em si
    def kruskal(self):
        lista_vertices = []
        for aresta in self.lista_arestas:
            x = aresta.vertices[0]
            y = aresta.vertices[1]
            if x in lista_vertices and y in lista_vertices:
                caminho = []
                verticex = self.lista_vertices_menor[x]
                verticey = self.lista_vertices_menor[y]
                caminho = self.acha_caminhos(verticex, verticey)
                if caminho == []:
                    self.menor_grafo.append(aresta)
                    verticex.adjacentes.append(verticey)
                    verticey.adjacentes.append(verticex)
            else:
                self.menor_grafo.append(aresta)
                self.cria_vertices(aresta, self.lista_vertices_menor)
                if x not in lista_vertices:
                    lista_vertices.append(x)
                if y not in lista_vertices:
                    lista_vertices.append(y)
    
    #agora vamos criar algo para achar o menor caminho entre os vértices dados
    def cria_vertices(self, aresta, lista):
        #separo os vertices que a aresta recebe
        x = int(aresta.vertices[0])
        y = int(aresta.vertices[1])
        #tento atribuir y como adjacente a x
        try :
            verticex = lista[x]
            verticex.indice = x
        except:
            falta = (x - len(lista)) + 1
            for i in range (falta):
                vertice = Vertices([])
                lista.append(vertice)
            verticex = lista[x]
            verticex.indice = x
        try:
            verticey = lista[y]
            verticey.indice = y
        except:
            falta = (y - len(lista))+1
            for i in range (falta):
                vertice = Vertices([])
                lista.append(vertice)
            verticey = lista[y]
            verticey.indice = y
        verticex.adjacentes.append(verticey)
        verticey.adjacentes.append(verticex)
    
    #busca caminho
    def acha_caminhos(self, comeco, final, visitados = []):
        visitados_provisorio = []
        for item in visitados:
            visitados_provisorio.append(item)
        visitados_provisorio.append(comeco)
        if final in comeco.adjacentes:
            visitados_provisorio.append(final)
            return visitados_provisorio
        else:
            passou = False
            for vertice in comeco.adjacentes:
                if vertice not in visitados_provisorio:
                    visitados_provisorio = self.acha_caminhos(vertice, final, visitados_provisorio)
                    passou = True
                if final in visitados_provisorio:
                    break
            if passou == False:
                return visitados
                
        return visitados_provisorio
        
    #um metodo simples só para imprimir o resultado
    def imprimir(self):
        self.sorteando(self.menor_grafo)
        print("O menor grafo é:")
        for aresta in self.menor_grafo:
            x = aresta.vertices[0]
            y = aresta.vertices[1]
            w = aresta.peso
            print(f'{x}<->{y} ({w})')
    


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
grafokruskal.sorteando(grafokruskal.lista_arestas)
grafokruskal.kruskal()

#printa o menor grafo
grafokruskal.imprimir()