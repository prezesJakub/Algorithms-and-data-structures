from zad8testy import runtests

#Jakub Zając

#W algorytmie tworzę tablicę o wymiarach nxm, w której na pozycji tab[i][j] przechowuję
#minimalną odległość do parkingów rozpatrując wieżowce od 0 do i oraz parkingi od 0 do j.
#Wartości aktualizuję przechodząc po tablicy i dla każdej ustawiając wartość na minimum
#z wartości komórki tab[i][j-1] (jeśli optymalny parking dla i-tego wieżowca został ustalony wcześniej)
#oraz tab[i][j-1]+[różnica odległości między i-tym wieżowcem i j-tym parkingiem] (jeśli wykorzystując j-ty
#parking dla i-tego wieżowca uzyskamy mniejszą sumę odległości). Z racji, iż podane dane są posortowane,
#nie zdarzy się nigdy sytuacja, że powinniśmy wykorzystać parking na wcześniejszej pozycji niż już wykorzystane.
#Ponieważ parking i-tego wieżowca musi znajdować się przed i-1 wieżowcem, aktualizując tablicę rozpatrujemy parkingi
#licząc od i-tego parkingu.
#Złożoność obliczeniowa algorytmu wynosi O(n*m)

def parking(X,Y):
  n=len(X)
  m=len(Y)
  tab=[[float('inf') for i in range(m)] for j in range(n)]
  for i in range(n):
    tab[0][i]=min(abs(X[0]-Y[i]), tab[0][i-1])
  for i in range(1, n):
    for j in range(i, m):
      tab[i][j]=min(tab[i][j-1], tab[i-1][j-1]+abs(X[i]-Y[j]))
  return tab[n-1][m-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
