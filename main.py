def es_primo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

num = int(input("ingrese un número: "))
if es_primo(num):
    print(f"el número {num} es primo")
else:
    print(f"el número {num} no es primo")