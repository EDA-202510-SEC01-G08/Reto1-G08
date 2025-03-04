import sys
import tabulate as tb
from App import logic as lg
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    return lg.new_logic()

def print_menu():
    print("\nBienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    
    file = input("Ingrese el nombre del archivo a cargar: ")
    file_path = f"Data/{file}" 
    lg.load_data(control, file_path)


def print_req_1(control):

    año = int(input("\nIngrese el año a consultar: "))
    result = lg.req_1(control, año)

    if result == None:
        print(f"\nNo se encontraron registros para el año {año}")

    else:
        print(f"\nEl último registro encontrado del año {año} es: \n")
        headers = ["Count", "Year", "Load date", "Categoria", "Frecuencia", "Estado", "Producto", "U. Medición", "Valor"]  
        print(tb.tabulate(result, headers, tablefmt="pretty"))



def print_req_2(control):
    
    state_input = input("Ingrese el estado a consultar: ")
    stateu = state_input.upper()
    statet = stateu.replace(" ", "")
    result = lg.req_2(control, statet)

    if result == None:
        print(f"\nNo se encontraron registros para el estado de {state_input.title()}")

    else:
        print(f"\nEl último registro encontrado para el estado de {state_input.title()} es: ")
        headers = ["Count", "Year", "Load date", "Category", "Frecuencia", "Estado", "Producto", "U. Medición", "Valor"]  
        print(tb.tabulate(result, headers, tablefmt="pretty"))



def print_req_3(control):

    year_i = int(input("Ingrese el año inicial del rango en el cual desea revisar la información: "))
    year_f = int(input("Ingrese el año final del rango en el cual desea revisar la información: "))
    state = input("Ingrese el estado a consultar: ")
    stateu = state.upper()
    statet = stateu.replace(" ", "")

    result =lg.req_3(control, statet, year_i, year_f)
    if result == None:
        print(f"No se encontraron registros para el estado de {state.title()} en el rango de años {year_i} a {year_f}")
    else: 
        print("\nNúmero de registros encontrados: ")
        headers1 = ["Count", "Count Survey", "Count Census"]
        result1 = [[result[0], result[1], result[2]]]
        print(tb.tabulate(result1, headers1, tablefmt="pretty"))
        print(f"\nDatos de los registros encontrados para el estado de {state.title()} en el rango de años {year_i} a {year_f}: ")
        headers2 = ["Category", "Year", "Load time", "Frequency", "Product", "U. Measurement"]
        result2 = result[3]
        print(tb.tabulate(result2, headers2, tablefmt="pretty"))


def print_req_4(control):

    year_i = int(input("Ingrese el año inicial del rango en el cual desea revisar la información: "))
    year_f = int(input("Ingrese el año final del rango en el cual desea revisar la información: "))
    producto = input("Ingrese el tipo de producto a consultar: ")
    productou = producto.upper()
    productot = productou.replace(" ", "")
    result = lg.req_4(control,year_i, year_f, productot)
    if result == None:
        print(f"\nNo se encontraron registros para el producto {producto.capitalize()} en el rango de años {year_i} a {year_f}")
    else: 
        print("\nNúmero de registros encontrados: ")
        headers1 = ["Count", "Count Survey", "Count Census"]
        result1 = [[result[0], result[1], result[2]]]
        print(tb.tabulate(result1, headers1, tablefmt="pretty"))
        print(f"\nDatos de los registros encontrados para el producto {producto.capitalize()} en el rango de años {year_i} a {year_f}: ")
        headers2 = ["Category", "Year", "Load time", "Frequency", "State", "U. Measurement"]
        result2 = result[3]
        print(tb.tabulate(result2, headers2, tablefmt="pretty"))


def print_req_5(control):

    year_i = int(input("Ingrese el año inicial del rango en el cual desea revisar la información: "))
    year_f = int(input("Ingrese el año final del rango en el cual desea revisar la información: "))
    categoria = input("Ingrese la categoría estadistica que desea filtrar: ")
    categoriau = categoria.upper()
    categoriat = categoriau.replace(" ", "")

    result = lg.req_5(control, year_i, year_f, categoriat)

    if result == None:
        print(f"No se encontraron registros para la categoría {categoria.capitalize()} en el rango de años {year_i} a {year_f}")
    else: 
        headers = ["Count", "Count_Census", "Count_Survey", "Datos de cada Elemento"]
        print(tb.tabulate(result, headers, tablefmt="pretty"))


def print_req_6(control):

    fecha_i = input("Ingrese la fecha inicial desde la cual desea buscar: ")
    fecha_f = input("Ingrese la fecha final hasta la cual desea buscar: ")
    departamento = input("Ingrese el estado en el cual desea buscar los datos: ")
    result = lg.req_6(control, fecha_i, fecha_f, departamento)
    if result == None:
        print("No se encontraron datos")
    else:
        headers = ["Count", "Count_Census", "Count_Survey", "Datos de cada Elemento"]
        print(tb.tabulate(result, headers, tablefmt="pretty"))


def print_req_7(control):

    estado = input("Ingrese el estado en el cual desea buscar los datos: ")
    estadou = estado.upper()
    estadot = estadou.replace(" ", "")
    year_i = int(input("Ingrese el año inicial desde la cual desea buscar: "))
    year_f = int(input("Ingrese el año final hasta el cual desea buscar: "))
    result = lg.req_71(control, estadot, year_i, year_f)
    # OJO CON MANDAR REQ_71

    if result == None:
        print(f"No se encontraron datos para el estado de {estado.title()} en el rango de años {year_i} a {year_f}")
    else:
        print(f"\nDatos del registro con MENOR ingreso para el estado de {estado.title()} en el rango de años {year_i} a {year_f}: ")
        headers1 = ["Count", "Count periodo", "Count no validos", "Count survey", "Count census"]
        result1 = [[result[0][0], result[0][1], result[0][2], result[0][3], result[0][4]]]
        print(tb.tabulate(result1, headers1, tablefmt="pretty"))
        headers2 = ["Año", "Categoría", "Valor"]
        result2 = [[result[0][5], result[0][6], result[0][7]]]
        print(tb.tabulate(result2, headers2, tablefmt="pretty"))

        print(f"\nDatos del registro con MAYOR ingreso para el estado de {estado.title()} en el rango de años {year_i} a {year_f}: ")
        headers3 = ["Count", "Count periodo", "Count no validos", "Count survey", "Count census"]
        result3 = [[result[1][0], result[1][1], result[1][2], result[1][3], result[1][4]]]
        print(tb.tabulate(result3, headers3, tablefmt="pretty"))
        headers4 = ["Año", "Categoría", "Valor"]
        result4 = [[result[1][5], result[1][6], result[1][7]]]
        print(tb.tabulate(result4, headers4, tablefmt="pretty"))
        


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
