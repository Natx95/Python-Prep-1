#1) Crear una variable que contenga un elemento del 
# conjunto de números enteros y luego imprimir 
# por pantalla
unElementoEntero = 10
print(unElementoEntero)

#2) Imprimir el tipo de dato de la 
# constante 8.5
constante1 = 8.5
print(constante1)

#3) 3) Imprimir el tipo de dato de la variable
# creada en el punto 1
print(type(unElementoEntero))

#4) Crear una variable que contenga tu nombre
miNombre = "Nahuel"

#5) Crear una variable que contenga un número
# complejo
numComplejo = 1 + 3j

#6) Mostrar el tipo de dato de la variable 
# creada en el punto 5
print(type(numComplejo))

#7) Crear una variable que contenga el valor
# del número Pi redondeado a 4 decimales
pi = 3.1415

#8) Crear una variable que contenga el valor 
# 'True' y otra que contenga el valor True. 
# ¿Se trata de lo mismo?
var1 = 'True'
var2 = True
# RTA : cuando en una variable se utilizan las comillas simples
# o dobles el dato se guarda en formato String, en el caso 
#de que la variable tome la palabra True, esta reservada para el 
#tipo de dato booleano. no se trata de lo mismo
#9) Imprimir el tipo de dato correspondientes 
# a las variables creadas en el punto 8
print(type(var1), type(var2))

#10) Asignar a una variable, la suma de un número entero y otro decimal
varInt = 10
varFloat = 3.14
sumVar = varInt + varFloat
print(sumVar)

#11) Realizar una operación de suma de números complejos
sumnumC1 = 1 + 1j
sumnumC2 = 1 + 2j
sumC = sumnumC1 + sumnumC2
print(sumC)

#12) Realizar una operación de suma de un número real y otro complejo
sumnumC3 = 4 + 2j
sumnumR1 = 8
sumCR = sumnumC3 + sumnumR1
print(sumCR)

#13) Realizar una operación de multiplicación
mult1 = sumnumC3 * sumnumR1
print(mult1)

#14) Mostrar el resultado de elevar 2 a la octava potencia
potencia1 = 2**8
print(potencia1)

#15) Obtener el cociente de la división de 27 entre 4 en 
# una variable y luego mostrarla
operacion2 = 27 / 4
resCosOpe2 = operacion2
print(resCosOpe2)

#16) De la división anterior solamente mostrar la parte entera
operacion3 = 27 // 4
partEntera = operacion3
print(partEntera)

#17) De la división de 27 entre 4 mostrar solamente el resto
operacion4 = 27 % 4
partResto = operacion4
print(partResto)

#18) Utilizando como operandos el número 4 y los resultados 
# obtenidos en los puntos 16 y 17. Obtener 27 como resultado
obtener27 = (4 * partEntera) + partResto
print (obtener27)

#19) Utilizar el operador "+" en una operación donde intervengan
# solo variables alfanuméricas
varalfanum1 = "asd123"
varalfanum2 = "qwe456"
print (varalfanum1 + varalfanum2)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
varStr = "2"
varInt = 2
comparacion = (varStr  == varInt)
print(comparacion) #son dos tipos de datos diferentes, por ende en la comparacion 
#el resultado da negativo a que sean iguales

#21) Utilizar las funciones de cambio de tipo de dato,
# para que la validación del punto 20 resulte verdadera
varStr2 = "2"
varInt2 = 2
comparacion2 = (int(varStr2)  == varInt2)
print(comparacion2)

varStr3 = "2"
varInt3 = 2
comparacion3 = (varStr3 == str(varInt3) )
print(comparacion3)
#22) ¿Por qué arroja error el siguiente cambio de 
# tipo de datos? a = float('3,8')
# el error esta en como se define las decimas de un valor flotante
#el simbolo para representar las decimas es el punto, la coma esta 
#reservada para las tuplas

#Crear una variable con el valor 3, y utilizar el operador '-=' 
# para modificar su contenido
varFija = 3
varFija -= 2
print(varFija)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado?
# ¿Qué es el sistema de numeración binario?
numBin = 1 << 2
print (numBin)
print("este es el numero : " + str(numBin)) #chekear por que 

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido?
# ¿Si los dos operandos serían del mismo tipo,
# siempre arrojaría el mismo resultado?

#varSum2 = 2 + "2"
#print(varSum2)

#no se puede sumar un tipo texto a un numerico, tiene que ser del mismo caracter
#si fueran numericos daria la suma el resultado 4 , en el caso de que fueran string
#daria como reultado la concatenacion mostrando el "22"
#En el caso de que fueran los dos casos mensionados si casInt= 4, CasStr="22"

#26) Realizar una operación válida entre valores de tipo entero y string
varStr4 = "buen dia"
varInt4 = 2

print(varStr4 + str(varInt4))




