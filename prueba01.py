import numpy as np 

a = np.array([1,4,6,9])
b = np.array([2,3,7,8])
c = np.array([12,32,16,28,35])


print("Probando Numpy:")
print(a + b)
print(a.shape)
print(b.size)
print(c.max())
d =  b * a
print(d)
print(d.mean())

#Ejercicio Numpy:
#Tienes las ventas diarias (en euros) de una tienda durante una semana:
#[120, 85, 200, 150, 95, 310, 275]
#Resuelve con NumPy:

#1 Crea el array con los datos.
#2 Calcula el total y el promedio de ventas.
#3 Encuentra el día con más y menos ventas.
#4 Filtra los días en que se vendió más de 150€.

ventas= np.array([120, 85, 200, 150, 95, 310, 275])

print("Ejercicio Numpy: Tienes las ventas diarias (en euros) de una tienda durante una semana:")
print([120, 85, 200, 150, 95, 310, 275])
print("1 Crea un array con los datos")
print(ventas)
print("2 Calcula el total y el promedio de ventas")
print("Total: ", ventas.sum() , "Promedio: " , ventas.mean())
print("3 Encuentra el día con más y menos ventas")
print("Dia con más ventas:" , ventas.max() , "Dia con menos ventas: " , ventas.min())
print("4 Filtra los días en que se vendió más de 150€")
print(ventas>150)