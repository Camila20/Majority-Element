def funtion(a):
    n=len(a)
    b=0
    c=0
    for i in range(n):
        cont=a.count(a[i])  # Contador del elemento en la iesima posicion
        if b<cont:              
            b=cont          # B tomará el valor mayor
            c=i             # La posición del elementó más repetido
    if cont>(n/2):          # El elemnto debe repetirse en más de la mitad
        return a[c]         # Se retorna el elemento más repetido

print(funtion([2,1,2]))
