from zad2testy import runtests

#Jakub Zając

#Rozwiązanie opiera się na implementacji dwóch kopców: kopca minimum i kopca maksimum.
#Kopiec minimum przechowuje k największych elementów naszego podciągu, a kopiec maksimum
#elementy k+1 i dalsze. Przesuwając się w tablicy i tym samym zmieniając przedział, sprawdzam
#w której części znajdował się i-p element (który przestaje być częścią przedziału).
#Na tej podstawie dodaję nowy element do odpowiedniego kopca. Usuwanie elementów z kopca odbywa się
#wtedy, gdy "przeterminowany" element znajduje się na wierzchołku kopca. Przy równych elementach w kopcu minimum
#i maksimum, w kopcu minimum znajdują się te o mniejszym indeksie, dzięki czemu jest zachowana stabilność sortowania.
#Szacowana złożoność czasowa algorytmu wynosi O(nlogn), gdyż n razy przechodzimy po elementach, a logn operacji jest
#wykonywane przy naprawianiu kopców. Pamięciowo O(n)

def naprawmin(A, i, n):
    l, r, mini=2*i+1, 2*i+2, i
    if l<n and A[l][0]<=A[mini][0]:
        if A[l][0]<A[mini][0] or A[l][1]<A[mini][1]:
            mini=l
    if r<n and A[r][0]<=A[mini][0]:
        if A[r][0]<A[mini][0] or A[r][1]<A[mini][1]:
            mini=r
    if mini!=i:
        A[i], A[mini]=A[mini], A[i]
        naprawmin(A, mini, n)

def naprawmax(A, i, n):
    l, r, maxi=2*i+1, 2*i+2, i
    if l<n and A[l][0]>=A[maxi][0]:
        if A[l][0]>A[maxi][0] or A[l][1]<A[maxi][1]:
            maxi=l
    if r<n and A[r][0]>=A[maxi][0]:
        if A[r][0]>A[maxi][0] or A[r][1]<A[maxi][1]:
            maxi=r
    if maxi!=i:
        A[i], A[maxi]=A[maxi], A[i]
        naprawmax(A, maxi, n)

def naprawmindod(A, i):
    r=(i-1)//2
    while r>0 and A[r][0]>=A[i][0]:
        if A[r][0]>A[i][0] or A[r][1]>A[i][1]:
            A[r], A[i]=A[i], A[r]
        i, r= r, (r-1)//2
    if A[r][0]>A[i][0] or (A[r][0]==A[i][0] and A[r][1]>A[i][1]):
        A[r], A[i]=A[i], A[r]

def naprawmaxdod(A, i):
    r=(i-1)//2
    while r>0 and A[r][0]<=A[i][0]:
        if A[r][0]<A[i][0] or A[r][1]>A[i][1]:
            A[r], A[i]=A[i], A[r]
        i, r= r, (r-1)//2
    if A[r][0]<A[i][0] or (A[r][0]==A[i][0] and A[r][1]>A[i][1]):
        A[r], A[i]=A[i], A[r]

def zbudujmin(A, n):
    for i in range((n-2)//2, -1, -1):
        naprawmin(A, i, n)

def zad2(T, k, p):
    kopmin, kopmax=[], []
    wynik=0
    for i in range(k):
        kopmin.append([T[i], i])
    zbudujmin(kopmin, k)
    for i in range(k, p, 1):
        if T[i]>kopmin[0][0]:
            kopmax.append(kopmin[0])
            kopmin[0]=[T[i], i]
            naprawmin(kopmin, 0, len(kopmin))
            naprawmaxdod(kopmax, len(kopmax)-1)
        else:
            kopmax.append([T[i], i])
            naprawmaxdod(kopmax, len(kopmax)-1)
    wynik+=kopmin[0][0]
    for i in range(p, len(T), 1):
        if T[i-p]>=kopmin[0][0]:
            if T[i]>kopmax[0][0]:
                kopmin.append([T[i], i])
                naprawmindod(kopmin, len(kopmin)-1)
            else:
                kopmin.append(kopmax[0])
                kopmax[0]=[T[i], i]
                naprawmax(kopmax, 0, len(kopmax))
                naprawmindod(kopmin, len(kopmin)-1)
        else:
            if T[i]>kopmin[0][0]:
                kopmax.append(kopmin[0])
                kopmin[0]=[T[i], i]
                naprawmaxdod(kopmax, len(kopmax)-1)
                naprawmin(kopmin, 0, len(kopmin))
            else:
                kopmax.append([T[i], i])
                naprawmaxdod(kopmax, len(kopmax)-1)
        while len(kopmin)>0 and kopmin[0][1]<=i-p:
            kopmin[0], kopmin[len(kopmin)-1]=kopmin[len(kopmin)-1], kopmin[0]
            kopmin.pop()
            naprawmin(kopmin, 0, len(kopmin))
        while len(kopmax)>0 and kopmax[0][1]<=i-p:
            kopmax[0], kopmax[len(kopmax)-1]=kopmax[len(kopmax)-1], kopmax[0]
            kopmax.pop()
            naprawmax(kopmax, 0, len(kopmax))
        while kopmax[0][0]==kopmin[0][0] and kopmax[0][1]<kopmin[0][1]:
            kopmax[0],kopmin[0]=kopmin[0],kopmax[0]
            naprawmax(kopmax, 0, len(kopmax))
            naprawmin(kopmin, 0, len(kopmin))
        wynik+=kopmin[0][0]
    return wynik

def ksum(T, k, p):
    return zad2(T, k, p)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
