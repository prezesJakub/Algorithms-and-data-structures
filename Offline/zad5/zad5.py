from zad5testy import runtests
from queue import PriorityQueue

#Jakub Zając

#Rozwiązanie opiera się na algorytmie Dijkstry. Puszczam 2 razy algorytm Dijkstry. Pierw zaczynam od wierzchołka a,
#a za drugim razem od wierzchołka b. Następnie przechodzę po wszystkich punktach z tablicy S. Obliczam minimalny czas dotarcia
#do dowolnego z portali, zarówno z punktu A, jak i B. Wynik będzie minimum z czasu dotarcia z A i B (bez korzystania z portali)
#oraz sumy minimalnego czasu dotarcia z dowolnego z portali do punktu A i B.
#Złożoność wynosi O(E*logV)

def newtab(L, n):
    tab=[[] for i in range(n)]
    for el in L:
        tab[el[0]].append([el[1], el[2]])
        tab[el[1]].append([el[0], el[2]])
    return tab

def dijkstra(Q, dys, a, tab):
    Q.put((0, a))
    while not Q.empty():
        pom=Q.get()[1]
        for v in tab[pom]:
            if dys[v[0]]>dys[pom]+v[1]:
                dys[v[0]]=dys[pom]+v[1]
                Q.put((dys[v[0]], v[0]))

def spacetravel( n, E, S, a, b ):
    tab=newtab(E, n)
    dystansA=[float('inf')]*len(tab)
    dystansB=[float('inf')]*len(tab)
    mina, minb=float('inf'), float('inf')
    dystansA[a], dystansB[b]=0,0
    Q=PriorityQueue()
    dijkstra(Q, dystansA, a, tab)
    dijkstra(Q, dystansB, b, tab)
    for v in S:
        mina=min(mina, dystansA[v])
        minb=min(minb, dystansB[v])
    wynik=min(mina+minb, dystansA[b])
    if wynik==float('inf'):
        return None
    else:
        return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
