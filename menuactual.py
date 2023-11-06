
import os
import json

def cargar_libros():
    try:
        with open('libros.json', 'r') as file:
            libros = json.load(file)
        return libros
    except FileNotFoundError:
        return []

def guardar_libros(libros):
    with open('libros.json', 'w') as file:
        json.dump(libros, file)

def menu():
    print("""\n:::Bienvenidos a nuestra plataforma!!:::\n¿Qué desea realizar?: ")
    [1]- Entrar a la plataforma
    [2]- Salir de la plataforma\n""")

    option_str = input("Ingrese la opción deseada: \n")
    option = int(option_str)

    
    if option == 2:
        print("Ha salido de la plataforma. Hasta luego")
        

    elif option == 1:
        print("Estamos en la plataforma")

    else:
        print("Opción no válida. Seleccione una opción válida")

        while True:
            print("""\nCómo desea seguir?: 
            [1]- Agregar un libro
            [2]- Ver listado de libros
            [3]- Modificar un libro
            [4]- Borrar un libro
            [5]- Salir a la plataforma\n""")

            search_option_str = input("Ingrese la opción de búsqueda: \n")
            
            search_option = int(search_option_str)
            try:
                search_option = int(search_option_str)
            except ValueError:
                print("Ingrese un número válido.")
                continue

            if search_option == 1:
                titulo = input("Ingrese el título del libro: \n")
                libros = cargar_libros()
                libros.append({"titulo": titulo})
                print("Ha agregado el libro:", titulo)
                guardar_libros(libros)

            elif search_option == 2:
                print("Listado de libros:")
                libros = cargar_libros()
                for libro in libros:
                    print(libro['titulo'])

            elif search_option == 3:
                titulo_modificar = input("¿Cuál libro desea modificar?: \n")
                nuevo_titulo = input("Ingrese el nuevo título: \n")

                for libro in libros:
                    if libro['titulo'] == titulo_modificar:
                        libro['titulo'] = nuevo_titulo
                        print("\n Libro modificado con éxito.")
                        guardar_libros(libros)
                        break
                else:
                    print("\n Libro no encontrado.")

            elif search_option == 4:
                titulo_borrar = input("¿Cuál libro desea borrar?: \n")

                for libro in libros:
                    if libro['titulo'] == titulo_borrar:
                        libros.remove(libro)
                        print("\n Libro eliminado con éxito.")
                        guardar_libros(libros)
                        break
                else:
                    print("\n Libro no encontrado.")

            elif search_option == 5:
                print("\n Ha salido de la plataforma.")
                break

if __name__ == "__main__":
    if not os.path.exists('libros.json'):
        with open('libros.json', 'w') as file:
            file.write('[]')

    menu()import os
import json

def cargar_libros():
    try:
        with open('libros.json', 'r') as file:
            libros = json.load(file)
        return libros
    except FileNotFoundError:
        return []

def guardar_libros(libros):
    with open('libros.json', 'w') as file:
        json.dump(libros, file)

def menu():
    print("""\n:::Bienvenidos a nuestra plataforma!!:::\n¿Qué desea realizar?: ")
    [1]- Entrar a la plataforma
    [2]- Salir de la plataforma\n""")

    option_str = input("Ingrese la opción deseada: \n")
    option = int(option_str)

    
    if option == 2:
        print("Ha salido de la plataforma. Hasta luego")
        

    elif option == 1:
        print("Estamos en la plataforma")

    else:
        print("Opción no válida. Seleccione una opción válida")

        while True:
            print("""\nCómo desea seguir?: 
            [1]- Agregar un libro
            [2]- Ver listado de libros
            [3]- Modificar un libro
            [4]- Borrar un libro
            [5]- Salir a la plataforma\n""")

            search_option_str = input("Ingrese la opción de búsqueda: \n")
            
            search_option = int(search_option_str)
            try:
                search_option = int(search_option_str)
            except ValueError:
                print("Ingrese un número válido.")
                continue

            if search_option == 1:
                titulo = input("Ingrese el título del libro: \n")
                libros = cargar_libros()
                libros.append({"titulo": titulo})
                print("Ha agregado el libro:", titulo)
                guardar_libros(libros)

            elif search_option == 2:
                print("Listado de libros:")
                libros = cargar_libros()
                for libro in libros:
                    print(libro['titulo'])

            elif search_option == 3:
                titulo_modificar = input("¿Cuál libro desea modificar?: \n")
                nuevo_titulo = input("Ingrese el nuevo título: \n")

                for libro in libros:
                    if libro['titulo'] == titulo_modificar:
                        libro['titulo'] = nuevo_titulo
                        print("\n Libro modificado con éxito.")
                        guardar_libros(libros)
                        break
                else:
                    print("\n Libro no encontrado.")

            elif search_option == 4:
                titulo_borrar = input("¿Cuál libro desea borrar?: \n")

                for libro in libros:
                    if libro['titulo'] == titulo_borrar:
                        libros.remove(libro)
                        print("\n Libro eliminado con éxito.")
                        guardar_libros(libros)
                        break
                else:
                    print("\n Libro no encontrado.")

            elif search_option == 5:
                print("\n Ha salido de la plataforma.")
                break

if __name__ == "__main__":
    if not os.path.exists('libros.json'):
        with open('libros.json', 'w') as file:
            file.write('[]')

    menu()
