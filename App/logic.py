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
    result = True
    for x in range(size):
        if int(lt.get_element(catalog["year_collection"], x)) == año:
            count += 1
            elem = x

    if count == 0:
        result = None
    else:
        
        year = lt.get_element(catalog["year_collection"], elem) 
        fecha_carga = lt.get_element(catalog["load_time"], elem)
        tipo_fuente = lt.get_element(catalog["source"], elem)
        frecuencia = lt.get_element(catalog["freq_collection"], elem)
        estado = lt.get_element(catalog["state_name"], elem) 
        tipo_producto = lt.get_element(catalog["commodity"], elem)
        unidad_medicion = lt.get_element(catalog["unit_measurement"], elem)
        valor_medicion = lt.get_element(catalog["value"], elem)
        result = [[count, year, fecha_carga, tipo_fuente, frecuencia, estado, tipo_producto, unidad_medicion, valor_medicion]] 

    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")
    return result

def req_2(catalog, estado): 

    tiempo1 = get_time()
    size = lt.size(catalog["state_name"])
    count = 0 
    result = True

    for x in range(size):
        state = lt.get_element(catalog["state_name"], x)
        stateu = state.upper()
        statet = stateu.replace(" ", "")

        if  statet == estado:
            count += 1
            elem = x

    if count == 0:
        result = None
    else:
        
        year = lt.get_element(catalog["year_collection"], elem) 
        fecha_carga = lt.get_element(catalog["load_time"], elem)
        tipo_fuente = lt.get_element(catalog["source"], elem)
        frecuencia = lt.get_element(catalog["freq_collection"], elem)
        estado = lt.get_element(catalog["state_name"], elem) 
        tipo_producto = lt.get_element(catalog["commodity"], elem)
        unidad_medicion = lt.get_element(catalog["unit_measurement"], elem)
        valor_medicion = lt.get_element(catalog["value"], elem)

        result = [[count, year, fecha_carga, tipo_fuente, frecuencia, estado, tipo_producto, unidad_medicion, valor_medicion ]]
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
    lista = []
    result = True

    for i in range(size):
        year = int(lt.get_element(catalog["year_collection"], i))
        estado = lt.get_element(catalog["state_name"], i)
        estadou = estado.upper()
        estadot = estadou.replace(" ", "")
        if estadot == state and year >= year_i and year <= year_f:
            source =  lt.get_element(catalog["source"], i)
            year =  lt.get_element(catalog["year_collection"], i)
            load_time = lt.get_element(catalog["load_time"], i)
            freq_collection =  lt.get_element(catalog["freq_collection"], i)
            commodity =  lt.get_element(catalog["commodity"], i)
            unit_measurement = lt.get_element(catalog["unit_measurement"], i)

            data = [source, year, load_time, freq_collection, commodity, unit_measurement]
            lista.append(data)
            count += 1

        if lt.get_element(catalog["source"], i).upper() == "SURVEY":
            count_survey += 1
        elif lt.get_element(catalog["source"], i).upper() == "CENSUS":
            count_census += 1

    if lista == []:
        result = None
    
    elif len(lista) <= 20:
        result = [count, count_survey, count_census, lista]

    else:
        recortada = lista[:5] + lista[-5:]
        result = [count, count_survey, count_census, recortada]

   
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
    lista = []
    result = True

    for i in range(size):
        year = int(lt.get_element(catalog["year_collection"], i))
        prod = lt.get_element(catalog["commodity"], i)
        produ = prod.upper()
        prodt = produ.replace(" ", "")
        if prodt == producto and year >= year_i and year <= year_f:

            source = lt.get_element(catalog["source"], i)
            year = lt.get_element(catalog["year_collection"], i)
            load_time = lt.get_element(catalog["load_time"], i)
            freq_collection = lt.get_element(catalog["freq_collection"], i)
            state_name = lt.get_element(catalog["state_name"], i)
            unit_measurement = lt.get_element(catalog["unit_measurement"], i)
            data = [source, year, load_time, freq_collection, state_name, unit_measurement]

            lista.append(data)
            count += 1

        if lt.get_element(catalog["source"], i) == "SURVEY":
            count_survey += 1
        elif lt.get_element(catalog["source"], i) == "CENSUS":
            count_census += 1

    if lista == []:
        result = None
   
    elif len(lista) <= 20:
        result = [count, count_survey, count_census, lista]
   
    elif len(lista) > 20:
        recortada = lista[:5] + lista[-5:]

        result = [count, count_survey, count_census, recortada]
   
    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result
   

def req_5(catalog, year_i, year_f, categoria):

    start_time = get_time()
    list_datos = lt.new_list()
    count_survey = 0
    count_census = 0
    pos = 0
    result = True

    while pos < lt.size(catalog["source"]):
        if catalog["year_collection"]["elements"][pos] >= year_i and catalog["year_collection"]["elements"][pos] <= year_f and catalog["statical_category"]["elements"][pos] == categoria:
            if catalog["source"]["elements"][pos].upper() == "SURVEY":
                count_survey += 1
            else: count_census += 1
            lt.add_last(list_datos, [catalog["source"]["elements"][pos], 
                                 catalog["year_collection"]["elements"][pos],
                                 catalog["load_time"]["elements"][pos],
                                 catalog["freq_collection"]["elements"][pos],
                                 catalog["state_name"]["elements"][pos],
                                 catalog["unit_measurement"]["elements"][pos],
                                 catalog["commodity"]["elements"][pos]])
        pos += 1
    numero_total = count_census + count_survey
    
    if list_datos == []: 
        result = None

    elif lt.size(list_datos) <= 20:
        result = [[numero_total, count_census, count_survey, list_datos]] #Tiempo no va en este return porque se printea
   
    elif lt.size(list_datos) > 20:
        recortada = lt.new_list()
        for i in range(-5,5):
            lt.add_last(recortada, list_datos["elements"][i])

        result = [[numero_total, count_census, count_survey, recortada]]

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result

def req_6(catalog, fecha_i, fecha_f, departamento): # este requerimiento tiene los mismos erroes con el acceso a los datos
                                                    # para esto es mejor no usar lt.new_list() y usar listas normales
                                                    # hay muchas confusiones

    start_time = get_time()
    list_datos = lt.new_list()
    count_survey = 0
    count_census = 0
    pos = 0
    result = True

    while pos < lt.size(catalog["source"]):
        if catalog["load_time"]["elements"][pos] >= fecha_i and catalog["load_time"]["elements"][pos] <= fecha_f and catalog["state_name"]["elements"][pos] == departamento:
            if catalog["source"]["elements"][pos].upper() == "SURVEY":
                count_survey += 1
            else: count_census += 1
            lt.add_last(list_datos, [catalog["source"]["elements"][pos], 
                                 catalog["year_collection"]["elements"][pos],
                                 catalog["load_time"]["elements"][pos],
                                 catalog["freq_collection"]["elements"][pos],
                                 catalog["state_name"]["elements"][pos],
                                 catalog["unit_measurement"]["elements"][pos],
                                 catalog["commodity"]["elements"][pos]])
            
        pos += 1
    numero_total = count_census + count_survey
    if list_datos == []: 
        result = None

    elif lt.size(list_datos) <= 20:
        result = [[numero_total, count_census, count_survey, list_datos]] #Tiempo no va en este return porque se printea
   
    elif lt.size(list_datos) > 20:
        recortada = lt.new_list()
        for i in range(-5,5):
            lt.add_last(recortada, list_datos["elements"][i])
        result = [[numero_total, count_census, count_survey, recortada]]
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    print("\nTiempo: " + str(tiempo) + " ms")    
    return result


def req_7(catalog, state, year_i, year_f):

    tiempo1 = get_time()
    count = 0
    count_survey = 0
    count_census = 0
    size = lt.size(catalog["state_name"])
    menor = None
    mayor = None
    year_menor = None
    year_mayor = None
    count_no_validos = 0
    registros_mayor = 0 
    registros_menor = 0
    result = True

    for i in range(size):
        year = int(lt.get_element(catalog["year_collection"], i))
        estado = lt.get_element(catalog["state_name"], i)
        
        if estado == state and year >= year_i and year <= year_f and lt.get_element(catalog["unit_measurement"], i) == "$":
            
            if "(" not in lt.get_element(catalog["value"], i):  
                valor = float(lt.get_element(catalog["value"], i))  
                count += 1

                if menor is None or valor < menor:
                    menor = valor
                    year_menor = year
                    registros_menor = 1  
                elif valor == menor:
                    registros_menor += 1  

                if mayor is None or valor > mayor:
                    mayor = valor
                    year_mayor = year
                    registros_mayor = 1  
                elif valor == mayor:
                    registros_mayor += 1
 
            else:
                count_no_validos += 1

            if lt.get_element(catalog["source"], i) == "Survey":
                count_survey += 1
            elif lt.get_element(catalog["source"], i) == "Census":
                count_census += 1   

    
    if count == 0:
        return None
    if year_mayor == year_menor:
        result = [year_mayor, "MAYOR, MENOR", mayor, registros_mayor, count_no_validos, count_survey, count_census]
    else:
        result = [[[[year_mayor, "MAYOR", mayor, registros_mayor, count_no_validos, count_survey, count_census]],
            [[year_menor, "MENOR", menor, registros_menor, count_no_validos, count_survey, count_census]]]]
    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)

    print("\nTiempo: " + str(tiempo) + " ms" + "\n")   
    print("\nTotal registros en el filtro: " + str(count) + "\n")     
    return result

def req_71(catalog, state, year_i, year_f):

    tiempo1 = get_time()
    count = 0
    count_survey = 0
    count_census = 0
    count_periodo = 0   
    count_no_validos = 0
    menor = 0
    mayor = 0
    year_menor = 0
    year_mayor = 0
    size = lt.size(catalog["state_name"])
    result = True

    for i in range(size):
        year = int(lt.get_element(catalog["year_collection"], i))
        estado = lt.get_element(catalog["state_name"], i)
        estadou = estado.upper()
        estadot = estadou.replace(" ", "")
        
        if year >= year_i and year <= year_f:
            count_periodo += 1

        if estadot == state and year >= year_i and year <= year_f and lt.get_element(catalog["unit_measurement"], i) == "$":
            
            if "(" not in lt.get_element(catalog["value"], i):  
                valor = lt.get_element(catalog["value"], i)
                valorint = valor.replace(",", "")
                valort = float(valorint)
                count += 1

                if menor == 0  or year_menor == 0 or valort < menor:
                    menor = valort
                    year_menor = year
 

                if mayor == 0 or year_mayor == 0 or valort > mayor:
                    mayor = valort
                    year_mayor = year

            else:
                count_no_validos += 1

            if lt.get_element(catalog["source"], i) == "SURVEY":
                count_survey += 1
            elif lt.get_element(catalog["source"], i) == "CENSUS":
                count_census += 1   

    
    if count == 0:
        return None

    else:
        result_menor = [count, count_periodo, count_no_validos, count_survey, count_census, year_menor, "MENOR", menor]
        result_mayor = [count, count_periodo, count_no_validos, count_survey, count_census, year_mayor, "MAYOR", mayor]
        result = [result_menor, result_mayor]
       
    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    print("\nTiempo: " + str(tiempo) + " ms" + "\n") 

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
