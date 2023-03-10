n = int(input("Nombre de pair "))
i = 0
count = 0

while count < n:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1

for i in range(0, n, 2):
    print(i)

