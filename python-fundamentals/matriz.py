columnas = input('Ingrese num de columnas: ')
filas = input('Ingrese num de filas: ')

columnas = int(columnas)
filas = int(filas)

#print(type(columnas))
#print(type(filas))

for fila in range(1,filas + 1):
    print('*' * columnas)