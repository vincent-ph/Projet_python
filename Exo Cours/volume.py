def cube(x):
    return x**3


def volumesphere(r):
    pi = 3.14
    return (4/3) * pi * cube(r)


rayon = int(input("Entrez le rayon: "))
print(volumesphere(rayon))
