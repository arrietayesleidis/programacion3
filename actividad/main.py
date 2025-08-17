from clases.animal import*

a = animal("firulay",8.40,"yesleidis","17/06/20","23/04/24")
print("El nombre del tu animal es: ", a.nombre," y el propietario es: ",a.propietario)

a.fechaCumple =input("ingrese un nuevo nombre: ")
print("nuevo nombre: ", a.nombre) 