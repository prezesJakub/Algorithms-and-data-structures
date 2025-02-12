from zad1testy import Node, runtests

#Jakub Zając
#W rozwiązaniu iteruję się po wszystkich elementach listy, kolejno wrzucając je na kopiec minimum. Kopiec nigdy nie przekracza k+1 elementów.
#Gdy kopiec posiada k+1 elementów, ściągam korzeń (najmniejszy element) i dodaję go do listy wynikowej. W zamian, do kopca dodaję kolejny element
#początkowej listy. Ponieważ początkowe pozycje elementów odbiegają od posortowanych pozycji o co najwyżej k, posiadając k+1 elementów, na pewno
#wśród nich znajduje się kolejny element posortowanej listy. Na koniec pozostałe elementy w kopcu sortuję i dodaję do wynikowej listy.
#Dzięki rozważaniu w kopcu jedynie k+1 elementów, algorytm ma złożoność O(nlogk).
#Dla k=O(1) złożoność wynosi O(n). Dla k=O(logn) wynosi ona O(nlog(logn)). Dla k=O(n) wynosi O(nlogn).

def napraw(A, i, n):
    l, r, mini=2*i+1, 2*i+2, i
    if l<n and A[l]<A[mini]:
        mini=l
    if r<n and A[r]<A[mini]:
        mini=r
    if mini!=i:
        A[i], A[mini]=A[mini], A[i]
        napraw(A, mini, n)

def sortheap(p, A, k):
    pom=p
    wynik=[]
    for i in range(k+1):
        if pom!=None:
            A.append(pom.val)
            pom=pom.next
    for i in range((len(A)-2)//2, -1, -1):
        napraw(A, i, len(A))
    while pom!=None:
        wynik.append(A[0])
        A[0]=pom.val
        napraw(A, 0, len(A))
        pom=pom.next
    for i in range(len(A), 0, -1):
        wynik.append(A[0])
        A[0]=A[i-1]
        napraw(A, 0, i)
    return wynik

def SortH(p,k):
    kopiec=[]
    kopiec=sortheap(p,kopiec, k)
    pom=p
    for i in range(len(kopiec)):
        if pom!=None:
            pom.val=kopiec[i]
            pom=pom.next
    return p
    pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
