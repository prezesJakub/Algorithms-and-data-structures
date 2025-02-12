from zad4testy import runtests

#Jakub Zając

#Na początku zamieniam zadaną w zadaniu tablicę na postać tablicy sąsiedztwa.
#Następnie wywołuję przeszukiwanie grafu w wierzchołku x na wzór DFSa, z różnicą, że
#po skończeniu przeszukiwania danego wierzchołka, gdy wychodzę z niego i cofam się rekurencyjnie,
#zmieniam visited[x] na False, abym mógł dojść do tego wierzchołka inną drogą.
#minh i maxh to minimalne i maksymalne pułapy wysokości na których przebiega obecna trasa.
#Do danego wierzchołka można przejść wtedy, gdy wchodząc do niego, nadal będzie można obrać optymalny
#pułap. Jeśli nie dojdzie nigdy do wierzchołka y, funkcja zwraca False, w przeciwnym wypadku True.
#Algorytm ma złożoność O(V*E)

def newtab(L):
  n=0
  for v in L:
    n=max(n, max(v[0], v[1]))
  tab=[[] for i in range(n+1)]
  for v in L:
    tab[v[0]].append([v[1], v[2]])
    tab[v[1]].append([v[0], v[2]])
  return tab

def zad4(L,x,y,t):
  tab=newtab(L)
  visited=[False]*len(tab)
  def DFSvisit(tab, x, start, stop, minh, maxh):
    visited[x]=True
    if x==stop:
      return True
    for v in tab[x]:
      if not visited[v[0]]:
        if x==start:
          minh=v[1]
          maxh=v[1]
        minw=min(minh, v[1])
        maxw=max(maxh, v[1])
        if maxw-minw<=2*t:
          if DFSvisit(tab, v[0], start, stop, minw, maxw):
            return True
    visited[x]=False
    return False
  return DFSvisit(tab, x, x, y, 0, 0)
  

def Flight(L,x,y,t):
  return zad4(L,x,y,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
