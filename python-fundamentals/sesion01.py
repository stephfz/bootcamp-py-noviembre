#print('Hola desde archivo')


my_int = 5
my_float = 4.5
my_boolean = False
my_string = 'Stephanie'

#print(my_float + my_int) 
#print(my_string + "otronombre")

'''
print(my_string[1])
print(len(my_string))

new_string = my_string.replace('e', 'u')
print(new_string)
'''
# Estructuras

#Listas/Arreglos
lista_numeros = [3, 6, 7]
'''
print (lista_numeros)
print (lista_numeros[2])

lista_numeros.append(23)
print (lista_numeros)
print (len(lista_numeros))
'''
#Diccionarios
my_dicc = { 'nombre': 'Stephanie', 'edad': 37, 'nacionalidad': 'Peruana' }

'''
print(my_dicc)

print(my_dicc['nombre'])

print(my_dicc.keys())
print(my_dicc.values())

my_dicc['profesion'] = 'Ingeniera'
print(my_dicc)
'''

#edad = 100
'''
if (edad > 18) and (edad < 80):  
    print('Eres mayor de edad')
    print('Busca tu carnet de identidad')

elif (edad > 10):
    print('Es mayor a 10')   
else:
    print('Cualquier otro caso')
    #print('No eres mayor de edad')
    #print('Pide asistencia')    
'''

'''
edad = 11
if (edad > 18) and (edad < 80):  
    print('Eres mayor de edad')
else:
    annios_faltantes = 18 - edad
    print('No eres mayor de edad')
    #print('Te falta: ', annios_faltantes)  
    print('Te faltan : {} años para ser mayor de edad'.format(annios_faltantes))  
'''

# Bucles

#while
'''
contador = 5
while (contador > 0): 
    print(contador)
    contador = contador - 1
'''

#for
# js -> for (i = 0; i<10; i++)

#for index in range(1,11): 
   # print(index) 

'''
nombre = 'Stephanie'
for char in nombre:
    print(char)
'''
'''
lista_numeros = [3 ,45, 57, 99]
for numero in lista_numeros:
    print(numero)
'''

'''

for index in range(10,-1,-2): 
    print(index) 

contador = 10
while (contador >= 0):
    print(contador)
    contador = contador - 2    
'''

'''def saludo():
    print('Hola desde la funcion')'''

def saludo(nombre):
    print('Hola {}'.format(nombre))
    

#saludo('Stephanie')    

def suma(a,b):
    print('Sumando')
    return a + b


#print(suma(4,465.7567356))

#a_num = 986986
#print ( 'Hola ' + str(a_num))

tiempo = 2.56
tiempo_en_str = str(tiempo)
print(tiempo_en_str)
tiempo_como_lista = tiempo_en_str.split('.')
print(tiempo_como_lista)

print('El tiempo total fue de {} min y {} segundos'.format(tiempo_como_lista[0], tiempo_como_lista[1]))

