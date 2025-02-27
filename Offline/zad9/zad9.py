from zad9testy import runtests

#Jakub Zając

#Algorytm opiera się na algorytmie DFS i wykorzystuje podejście dynamiczne, gdyż po wywołaniu DFSa z danego wierzchołka
#zapisuje w tablicy najdłuższą możliwą ścieżkę zaczynającą się w danym wierzchołku, dzięki czemu każdy wierzchołek jest
#odwiedzany tylko raz. Po wywołaniu funkcji dfs, algorytm sprawdza potencjalną ścieżkę w 4 kierunkach, a następnie zwraca
#największy wynik. Ostateczny wynik jest największą wartością z całej tablicy tab.
#Złożoność czasowa algorytmu wynosi O(nm)


def trip(M):
    m = len(M)
    n = len(M[0])
    tab = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if tab[i][j] != -1:
            return tab[i][j]
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        maxlen = 1
        for x, y in directions:
            if 0<=i+x<m and 0<=j+y<n and M[i+x][j+y]>M[i][j]:
                maxlen = max(maxlen, 1+dfs(i+x, j+y))
                
        tab[i][j] = maxlen
        return maxlen
    
    result = 0
    for x in range(m):
        for y in range(n):
            result = max(result, dfs(x, y))
    return result
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
