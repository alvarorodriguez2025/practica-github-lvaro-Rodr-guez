#En este apartado estamos definiendo variables#
var1="Xaloc" #Esta  de tipo String y como puedes observar esta entre comillas" 
var2=4 #esta variable contiene un valor entero#
var3=5
var4=1.8#esta variable contiene un valor de tipo float/decimal

#este es un ejemplo de como no debo definir una variable var3="no es correcto"
print("este mensaje se visualizara por pantalla")

suma=var2+var3
print(suma)
print(var2 + var3)
print("El resultado de la suma de var2 + var3 es", suma)
print("El resultado de la suma")
print("Error de instrucción")
#a continuación hacemos uso de la funcion input, instrucción que permite capturar
#un valor introducido por el usuario vía teclado
nombre=input("Introduce tu nombre")
apellido1=input("Introduce tu primer apellido")
apellido2=input("Introduce tu segundo apellido")
#He definido una variable nombre_completo que contiene la información de otras tres variables.
nombre_completo= nombre + " " + apellido1 + " " + apellido2
#finalmente utilizamos la funcion print para visualizar por pantalla el contenido en este caso
#la variable nombre_completo
print(nombre completo)
#Estos son os ejemplos de como debo realizar una suma, resta, multiplicación o división
suma=var2+var3
print(f"La suma de (var2) + (var3) es igual a ", suma)
resta=var2-var3
print(f"La resta de (var2) - (var3) es igual a ", resta)
multiplicación=var2*var3
print(f"La division de (var2) * (var3) es igual a ", multiplicación)
modulo_division=var2%var3
print(f"El resto de la division de (var2) / (var3) es igual a ", modulo_division)
potencia=var2**var3
print(f"La potencia de (var2) ^ (var3) es igual a ", potencia)
      
