bilangan = int(input("masukan angka: "))
faktor = []

for i in range(1, bilangan + 1):
    if bilangan % i == 0:
        faktor.append(i)

print(f"faktor dari {bilangan} adalah: ")
for f in faktor:
    print(f)
