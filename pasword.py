import random
import string

ultima_contraseña = None

def nueva_cont():
    global ultima_contraseña
    
    mayus = input("¿Incluir mayúsculas? (S/N): ").lower()
    num = input("¿Incluir números? (S/N): ").lower()
    espe = input("¿Incluir caracteres especiales? (S/N): ").lower()
    while True:
        try:
            longitud = int(input("¿De cuántos caracteres desea la contraseña? "))
            if longitud > 0:
                break
            else:
                print("Por favor, ingrese un número positivo mayor a 0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    
    caracteres = string.ascii_lowercase 
    if mayus == "s":
        caracteres += string.ascii_uppercase
    if num == "s":
        caracteres += string.digits
    if espe == "s":
        caracteres += string.punctuation

    
    if not caracteres:
        print("Debe seleccionar al menos un tipo de carácter.")
        return

    
    ultima_contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print("Contraseña generada:", ultima_contraseña)

def mostrar_ultima():
    if ultima_contraseña:
        print("Última contraseña generada:", ultima_contraseña)
    else:
        print("No se ha generado ninguna contraseña aún.")


while True:
    print("\nMenú:")
    print("1. Crear nueva contraseña")
    print("2. Ver la última contraseña creada")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nueva_cont()
    elif opcion == "2":
        mostrar_ultima()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")