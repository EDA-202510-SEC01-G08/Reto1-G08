import csv 
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from datetime import datetime

csv.field_size_limit(2147483647)

import time

def new_logic():

    catalog = {"source": None,
               "commodity": None,
               "statical_category": None,
               "unit_measurement": None,
               "state_name": None,
               "location": None,
               "year_collection": None,
               "freq_collection": None,
               "reference_period": None,
               "load_time": None,
               "value": None
               }
    catalog["source"] = lt.new_list()
    catalog["commodity"] = lt.new_list()
    catalog["statical_category"] = lt.new_list()
    catalog["unit_measurement"] = lt.new_list()
    catalog["state_name"] = lt.new_list()
    catalog["location"] = lt.new_list()
    catalog["year_collection"] = lt.new_list()
    catalog["freq_collection"] = lt.new_list()
    catalog["reference_period"] = lt.new_list()
    catalog["load_time"] = lt.new_list()
    catalog["value"] = lt.new_list()
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    
    with open(filename, mode = "r", encoding='utf-8') as file:

        input_file = csv.DictReader(file)
        count = 0
        año_max = 0
        año_min = 0
        last_five = []
        first_five = []

        for x in input_file:

            lt.add_last(catalog["source"], x["source"])
            lt.add_last(catalog["commodity"], x["commodity"])
            lt.add_last(catalog["statical_category"], x["statical_category"])
            lt.add_last(catalog["unit_measurement"], x["unit_measurement"])
            lt.add_last(catalog["state_name"], x["state_name"])
            lt.add_last(catalog["location"], x["location"])
            lt.add_last(catalog["year_collection"], x["year_collection"])
            lt.add_last(catalog["freq_collection"], x["freq_collection"])
            lt.add_last(catalog["reference_period"], x["reference_period"])
            lt.add_last(catalog["load_time"], x["load_time"])
            lt.add_last(catalog["value"], x["value"])
            
            if int(x["year_collection"]) > año_max or año_max == 0:
                año_max = int(x["year_collection"])
            if int(x["year_collection"]) < año_min or año_min == 0:
                año_min = int(x["year_collection"])
            count += 1

            datos_listas = {"year_collection": x["year_collection"],
                            "load_time": x["load_time"],
                            "state_name": x["state_name"],
                            "source": x["source"],
                            "unit_measurement": x["unit_measurement"],
                            "value": x["value"]}
            if count < 5:
                first_five.append(datos_listas)

            elif count >= 5:
                last_five.append(datos_listas)
                if len(last_five) > 5:
                    last_five.pop(0)

        return count, año_min, año_max, last_five, first_five

# Funciones de consulta sobre el catálogo

def req_1(catalog, año):

    tiempo1 = get_time()
    size = lt.size(catalog["year_collection"])
    count = 0
    result = lt.new_list()
    for x in range(size):
        if int(lt.get_element(catalog["year_collection"], x)) == año:
            count += 1
            elem = x

    if count == 0:
        result = None
    else:
       
        lt.add_last(result, [count,
                             lt.get_element(catalog["year_collection"], elem),
                             lt.get_element(catalog["load_time"], elem),
                             lt.get_element(catalog["source"], elem),
                             lt.get_element(catalog["freq_collection"], elem),
                             lt.get_element(catalog["state_name"], elem),
                             lt.get_element(catalog["commodity"], elem),
                             lt.get_element(catalog["unit_measurement"], elem),
                             lt.get_element(catalog["value"], elem)])
        
    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")
    return result

def req_2(catalog, estado):

    tiempo1 = get_time()
    size = lt.size(catalog["state_name"])
    count = 0
    result = lt.new_list()

    for x in range(size):
        state = lt.get_element(catalog["state_name"], x)
        stateu = state.upper()
        statet = stateu.replace(" ", "")

        if statet == estado:
            count += 1
            elem = x

    if count == 0:
        result = None
    else:
       
        lt.add_last(result, [count,lt.get_element(catalog["year_collection"], elem),
                             lt.get_element(catalog["load_time"], elem),
                             lt.get_element(catalog["source"], elem),
                             lt.get_element(catalog["freq_collection"], elem),
                             lt.get_element(catalog["state_name"], elem),
                             lt.get_element(catalog["commodity"], elem),
                             lt.get_element(catalog["unit_measurement"], elem),
                             lt.get_element(catalog["value"], elem)])

    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result

def req_3(catalog, state, year_i, year_f): 

    tiempo1 = get_time()
    count = 0
    count_survey = 0
    count_census = 0
    size = lt.size(catalog["state_name"])
    lista = lt.new_list()
    result = True

    for i in range(size):

        year = int(lt.get_element(catalog["year_collection"], i))
        estado = lt.get_element(catalog["state_name"], i)
        estadou = estado.upper()
        estadot = estadou.replace(" ", "")

        if estadot == state and year >= year_i and year <= year_f:

            lt.add_last(lista, [lt.get_element(catalog["source"], i),
                                lt.get_element(catalog["year_collection"], i),
                                lt.get_element(catalog["load_time"], i),
                                lt.get_element(catalog["freq_collection"], i),
                                lt.get_element(catalog["commodity"], i),
                                lt.get_element(catalog["unit_measurement"], i)])

            count += 1

        if lt.get_element(catalog["source"], i).upper() == "SURVEY":
            count_survey += 1
        elif lt.get_element(catalog["source"], i).upper() == "CENSUS":
            count_census += 1

    if lt.is_empty(lista):
        result = None
    
    elif lt.size(lista) <= 20:
        lt.add_first(lista, [count, count_survey, count_census])
        result = lista

    else:
        recortada = lt.new_list()
        for i in range(-5,5):
            lt.add_first(recortada, lt.get_element(lista, i))
        lt.add_first(recortada, [count, count_survey, count_census])
        result = recortada

    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result


def req_4(catalog, year_i, year_f, producto):

    tiempo1 = get_time()
    count = 0
    count_survey = 0
    count_census = 0
    size = lt.size(catalog["commodity"])
    lista = lt.new_list()
    result = True

    for i in range(size):
        year = int(lt.get_element(catalog["year_collection"], i))
        prod = lt.get_element(catalog["commodity"], i)
        produ = prod.upper()
        prodt = produ.replace(" ", "")
        
        if prodt == producto and year >= year_i and year <= year_f:

            lt.add_last(lista, [lt.get_element(catalog["source"], i),
                                lt.get_element(catalog["year_collection"], i),
                                lt.get_element(catalog["load_time"], i),
                                lt.get_element(catalog["freq_collection"], i),
                                lt.get_element(catalog["state_name"], i),
                                lt.get_element(catalog["unit_measurement"], i)])
            count += 1

        if lt.get_element(catalog["source"], i).upper() == "SURVEY":
            count_survey += 1
        elif lt.get_element(catalog["source"], i).upper() == "CENSUS":
            count_census += 1

    if lt.is_empty(lista):
        result = None
   
    elif lt.size(lista) <= 20:
        lt.add_first(lista, [count, count_survey, count_census])
        result = lista
   
    else:
        recortada = lt.new_list()
        for i in range(-5,5):
            lt.add_first(recortada, lt.get_element(lista, i))
        lt.add_first(recortada, [count, count_survey, count_census])
        result = recortada
   
    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result
   

def req_5(catalog, year_i, year_f, categoria):

    start_time = get_time()
    list_datos = lt.new_list()
    count = 0
    count_survey = 0
    count_census = 0
    pos = 0
    result = True

    while pos < lt.size(catalog["source"]):
        if int(lt.get_element(catalog["year_collection"], pos)) >= year_i and int(lt.get_element(catalog["year_collection"], pos)) <= year_f and lt.get_element(catalog["statical_category"], pos) == categoria:

            lt.add_last(list_datos, [catalog["source"]["elements"][pos], 
                                    catalog["year_collection"]["elements"][pos],
                                    catalog["load_time"]["elements"][pos],
                                    catalog["freq_collection"]["elements"][pos],
                                    catalog["state_name"]["elements"][pos],
                                    catalog["unit_measurement"]["elements"][pos],
                                    catalog["commodity"]["elements"][pos]])
            count += 1

        if lt.get_element(catalog["source"], pos).upper() == "SURVEY":
            count_survey += 1

        elif lt.get_element(catalog["source"], pos).upper() == "CENSUS":
            count_census += 1

        pos += 1

    if lt.is_empty(list_datos): 
        result = None

    elif lt.size(list_datos) <= 20:
        lt.add_first(list_datos, [count, count_survey, count_census])
        result = list_datos
   
    else:
        recortada = lt.new_list()
        for i in range(-5,5):
            lt.add_last(recortada, lt.get_element(list_datos, i))
        lt.add_first(recortada, [count, count_survey, count_census])
        result = recortada

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result

def req_6(catalog, fecha_i, fecha_f, departamento):

    tiempo1 = get_time()
    count = 0
    count_survey = 0
    count_census = 0
    size = lt.size(catalog["state_name"])
    lista = lt.new_list()

    fecha_i_dt = datetime.strptime(fecha_i, "%Y-%m-%d")
    fecha_f_dt = datetime.strptime(fecha_f, "%Y-%m-%d")

    for i in range(size):
        estado = lt.get_element(catalog["state_name"], i)
        estadou = estado.upper()
        estadot = estadou.replace(" ", "")
        fecha_carga_str = lt.get_element(catalog["load_time"], i)
        fecha_carga_dt = datetime.strptime(fecha_carga_str, "%Y-%m-%d %H:%M:%S") #En el excel no tiene este formato pero al probar con otro formato sale error

        if estadot == departamento and fecha_i_dt <= fecha_carga_dt  and fecha_carga_dt <= fecha_f_dt: 

            lt.add_last(lista, [lt.get_element(catalog["source"], i),
                                     lt.get_element(catalog["year_collection"], i),
                                     lt.get_element(catalog["load_time"], i),
                                     lt.get_element(catalog["freq_collection"], i),
                                     lt.get_element(catalog["state_name"], i),
                                     lt.get_element(catalog["unit_measurement"], i),
                                     lt.get_element(catalog["commodity"], i)])
            count += 1

        if lt.get_element(catalog["source"], i).upper() == "SURVEY":
                count_survey += 1
        elif lt.get_element(catalog["source"], i).upper() == "CENSUS":
                count_census += 1

    if lt.is_empty(lista):
        result = None

    elif lt.size(lista) <= 20:

        lt.add_first(lista, [count, count_survey, count_census])
        result = lista
    else:
        
        recortada = lt.new_list()
        for i in range(-5, 5):
            lt.add_last(recortada, lt.get_element(lista, i))
        lt.add_first(recortada, [count, count_survey, count_census])
        result = recortada

    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")
    return result

def req_7(catalog, state, year_i, year_f):

    tiempo1 = get_time()
    count_registro = 0
    count_survey = 0
    count_census = 0
    list_years = lt.new_list()
    size = lt.size(catalog["state_name"])
    result = True

    for i in range(year_i, year_f):
        suma_year = 0
        count_periodo = 0
        count_no_validos = 0
        for j in range(size):
            estado = lt.get_element(catalog["state_name"], j)
            estadou = estado.upper()
            estadot = estadou.replace(" ", "")

            if int(lt.get_element(catalog["year_collection"], j)) == i:
                count_periodo += 1

                if lt.get_element(catalog["source"], j).upper() == "SURVEY":
                    count_survey += 1
                elif lt.get_element(catalog["source"], j).upper() == "CENSUS":
                    count_census += 1

                if "(" not in lt.get_element(catalog["value"], j):
                    
                    if estadot == state: #Toda esta mano de if's por la cantidad de counts
                        valor = round(float(lt.get_element(catalog["value"], j).replace(",","")),2)
                        suma_year += valor
                        count_registro += 1
                else:
                    count_no_validos += 1
        
        if count_periodo != 0:
            lt.add_last(list_years, [i, suma_year, count_periodo, count_no_validos, count_survey, count_census])

    if lt.is_empty(list_years):
        result = None
    
    else:
        menor_valor = 0
        mayor_valor = 0
        for i in range(lt.size(list_years)):
            if lt.get_element(list_years, i)[1] < menor_valor or menor_valor == 0:
                menor_valor = lt.get_element(list_years, i)[1]
                menor = i

            if lt.get_element(list_years, i)[1] > mayor_valor or mayor_valor == 0:
                mayor_valor = lt.get_element(list_years, i)[1]
                mayor = i

        if menor == mayor:
            result = [lt.get_element(list_years, menor)]
        else:
            result = [lt.get_element(list_years, menor), lt.get_element(list_years, mayor)]

    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")

    return result

        

def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():

    return float(time.perf_counter()*1000)


def delta_time(start, end):

    elapsed = float(end - start)
    return elapsed
