from zad6testy import runtests
from queue import Queue
from queue import PriorityQueue

#Jakub Zając

#Algorytm najpierw zamienia zadaną w zadaniu tablicę na postać tablicy sąsiedztwa. Następnie tworzę tablicę sąsiedztwa
#dla możliwych ruchów przy użyciu dwumilowych butów stosując zmodyfikowany algorytm BFS. Następnie stosując zmodyfikowany
#algorytm Dijkstry obliczam minimalną odległość do każdego z punktów zaczynając od punktu s. Rozpatruję każdy wierzchołek
#dwukrotnie: w przypadku gdy do dotarcia do niego użyte zostały dwumilowe buty i w przeciwnym przypadku. W przypadku, gdy
#ostatni ruch odbył się przy użyciu dwumilowych butów, rozpatruję tylko zwyczajne ruchy z danego wierzchołka, a w przeciwnym
#przypadku rozpatruję oba warianty. Końcowy wynik jest minimum z dwóch tablic, uwzględniając dotarcie do finalnego wierzchołka
#przy pomocy dwumilowych butów lub bez nich.
#Złożoność czasowa algorytmu wynosi O(V^2 + VE)

def newtab(L, n):
    tab=[[] for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            if L[i][j]:
                tab[i].append([j, L[i][j]])
                tab[j].append([i, L[i][j]])
    return tab

def newjumptab(G, n):
    jumptab=[[] for i in range(n)]
    for s in range(n):
        Q = Queue()
        distance = [float('inf')]*n
        for v in G[s]:
            Q.put((v[0], v[1]))
        while not Q.empty():
            u, dis1 = Q.get()
            for v in G[u]:
                dis = max(dis1, v[1])
                distance[v[0]] = min(distance[v[0]], dis)
        for v in range(n):
            if distance[v] != float('inf'):
                jumptab[s].append((v, distance[v]))
    return jumptab

def dijkstra(Q, dis, jumpdis, s, tab, jumptab):
    Q.put((0, s, False))
    while not Q.empty():
        pomdis, pom, isjump = Q.get()
        for v in tab[pom]:
            if not isjump:
                if dis[v[0]] > dis[pom] + v[1]:
                    dis[v[0]] = dis[pom] + v[1]
                    Q.put((dis[v[0]], v[0], False))
            else:
                if dis[v[0]] > jumpdis[pom] + v[1]:
                    dis[v[0]] = jumpdis[pom] + v[1]
                    Q.put((dis[v[0]], v[0], False))
        if not isjump:
            for v in jumptab[pom]:
                if jumpdis[v[0]] > dis[pom] + v[1]:
                    jumpdis[v[0]] = dis[pom] + v[1]
                    Q.put((jumpdis[v[0]], v[0], True))

def jumper( G, s, w ):
    n = len(G)
    tab = newtab(G, n)
    jumptab = newjumptab(tab, n)
    dis = [float('inf')]*n
    jumpdis = [float('inf')]*n
    dis[s], jumpdis[s] = 0, 0
    Q = PriorityQueue()
    dijkstra(Q, dis, jumpdis, s, tab, jumptab)
    wynik = min(dis[w], jumpdis[w])
    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )
