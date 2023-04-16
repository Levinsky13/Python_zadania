print("Aby poznać sumę wszystkich liczb od 0 do n, wprowadź wartość n")
print("")
n = int(input("Wprowadź wartość n: "))
i = 0
suma = 0
while i <= n:
    suma = suma + i
    i += 1
print(f"Suma wszystkich liczb od 0 do {n}, jest równa: {suma}")
