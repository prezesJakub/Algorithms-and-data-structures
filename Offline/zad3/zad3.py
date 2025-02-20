from zad3testy import runtests

#Jakub Zając

#W rozwiązaniu obliczam dla każdej współrzędnej X i współrzędnej Y ile jest punktów o mniejszej współrzędnej od zadanej
#Następnie przechodzę jeszcze raz po tej tablicy, aby zsumować liczbę punktów. Na końcu przechodzę przez wszystkie punkty
#i sprawdzam ile punktów jest dominowanych przez dany punkt. W tym celu sumuję ile punktów jest dominowanych przez
#dany punkt osobno ze względu na współrzędną X i Y.Otrzymana suma jest sumą |X|+|Y|, gdzie |X| to liczność zbioru
#punktów dominowanych ze wzgl. na x, a |Y| ze wzgl. na y. W zadaniu interesuje nas część wspólna. Uznajmy, że |D| to
#liczność zbioru punktów, które dominują dany punkt. Wówczas: |D|+|X|+|Y|-|X∩Y|=n-1, więc |X∩Y|-|D|=|X|+|Y|-(n-1).
#Punkt najbardziej dominujący nie będzie dominowany przez żaden z punktów, gdyż w przeciwnym wypadku punkt, który by go
#dominował dominowałby jego oraz wszystkie jego dominowane punkty, więc to on byłby dominujący. Wobec tego dla
#najbardziej dominującego punktu |D|=0, więc |X∩Y|=|X|+|Y|-(n-1).
#Złożoność algorytmu jest rzędu O(n).

def dominance(P):
	n = len(P) + 1
	result = 0
	x_dominance = [0] * (n+1)
	y_dominance = [0] * (n+1)
	for point in P:
		x_dominance[point[0]+1] += 1
		y_dominance[point[1]+1] += 1
	for i in range(1, n):
		x_dominance[i] += x_dominance[i - 1]
		y_dominance[i] += y_dominance[i - 1]
	for point in P:
		result = max(result, x_dominance[point[0]] + y_dominance[point[1]] - len(P) + 1)
	return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
