from zad7testy import runtests

#Jakub Zając

#Tablica gora określa maksymalną liczbę odwiedzonych komnat po przyjściu z góry/lewej strony
#Tablica dol określa maksymalną liczbę odwiedzonych komnat po przyjściu z dołu/lewej strony
#Pierw ustawiam liczbę odwiedzonych komnat na polach z przeszkodami na -inf
#Następnie ustawiam wartości w zerowych kolumnach. W zerowych kolumnach możliwe jest przyjście
#tylko od góry, więc wartość w tablicy dol ustawiam na -inf.
#Następnie przechodzę 2 razy po tablicy, pierw od góry, aktualizując wartości przejścia od góry,
#następnie od dołu aktualizuję wartości przejścia od dołu
#Na końcu zwracam właściwy wynik.
#Złożoność algorytmu O(n^2)

def maze( L ):
    n=len(L)
    gora=[[0 for i in range(n)] for j in range(n)]
    dol=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if L[i][j]=='#':
                gora[i][j]=-float('inf')
                dol[i][j]=-float('inf')
    for i in range(1,n):
        gora[i][0]+=gora[i-1][0]+1
        dol[i][0]=-float('inf')
    for i in range(1,n):
        if L[0][i]=='.':
            gora[0][i]=max(gora[0][i-1], dol[0][i-1])+1
        for j in range(1,n):
            left=max(gora[j][i-1], dol[j][i-1])+1
            up=gora[j-1][i]+1
            if L[j][i]=='.':
                gora[j][i]=max(left, up)
        if L[n-1][i]=='.':
            dol[n-1][i]=max(dol[n-1][i-1], gora[n-1][i-1])+1
        for j in range(n-2, -1, -1):
            left=max(gora[j][i-1], dol[j][i-1])+1
            down=dol[j+1][i]+1
            if L[j][i]=='.':
                dol[j][i]=max(left, down)
    if gora[n-1][n-1]==-float('inf'):
        return -1
    else:
        return gora[n-1][n-1]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
