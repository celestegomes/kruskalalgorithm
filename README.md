# kruskalalgorithm
Um projeto da cadeira de algoritmos para implementação de Kruskal em uma base de dados escolhida por nós contanto que ela tenha mais de 90 vertices, 100 arestas e que as arestas tenham peso.

## Contexto do problema
O desafio dado foi implementar um algoritmo Kruskal numa base de dados com mais de 90 vértices e 100 arestas que tenham pesos. A base de dados deveria ser pública e os dados coletados reais para a implementação e o output esperado um grafo com as menores arestas. Para esse problema solucionamos a base Airline Travel Reachability Network, uma base com as informações sobre a facilidade de acesso através de transporte entre cidades dos Estados Unidos e Canadá, os pesos das arestas sendo relativos ao tempo de deslocamento em relação a um limiar. A base contém 456 vértices e 71959 arestas.

## Implementação
**Algoritmo utilizado**. Kruskal.
**Desenvolvimento**. A divisão do trabalho foi uma estudante com o código base e criação do relatório, outra com a implementação da base de dados. Ambas colaboraram na parte uma da outra, contribuíram com testagem e conserto dos bugs do código.

## Conclusão
Para o código base temos 3 classes, as arestas, os vértices e o grafo em si. O primeiro passo feito é criar um grafo inicial, a partir disso chamamos a base de dados, separamos as informações em cada vértice e peso e atribuímos ao método de criação de arestas. Uma vez que todas as arestas são criadas, é hora de ordenar elas pelo peso, os menores primeiro, maiores depois. Após isso é chamado o método que cria o menor grafo, ele primeiro analisa se ambos os vértices já estão numa lista criada, se eles não estiverem, ele chama um método que cria vértices, adiciona eles tanto na lista interna do método criador de grafo quanto no self e adicionamos a aresta adicionada no grafo. Se ambas as arestas já estiverem na lista, chama-se um método buscador de caminho, se esse método encontra não encontrar um caminho entre os dois vértices, adicionamos a aresta na lista do menor grafo. Após isso, mais uma vez ordenamos as arestas do menor grafo, dessa vez em função do primeiro vértice que os liga. Por último, imprimimos todas as arestas do grafo resultante com seus pesos.
