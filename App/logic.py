import csv 
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st

csv.field_size_limit(2147483647)

import time

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
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
    """
    Carga los datos del reto
    """
    
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

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def ultimo_reg_año(catalog, año): #REQ 1

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
        tiempo 
        result = count, year, fecha_carga, tipo_fuente, frecuencia, estado, tipo_producto, unidad_medicion, valor_medicion 

    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    #Print tiempo, esto depende de como se desarolle el veiw
    return tiempo, result

def ultimo_reg_estado(catalog, estado): #REQ 2
    
    tiempo1 = get_time()
    size = lt.size(catalog["state_name"])
    count = 0 
    result = True
    for x in range(size):
        if lt.get_element(catalog["state_name"], x) == estado:
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

        result = count, year, fecha_carga, tipo_fuente, frecuencia, estado, tipo_producto, unidad_medicion, valor_medicion 
    tiempo2 = get_time()
    tiempo = delta_time(tiempo1, tiempo2)
    return tiempo, result

def reg_state_año(catalog, state, year_i, year_f): #REQ 3, year_i = año inicial, year_f = año final

    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    

def req_4(catalog, year_i, year_f, producto):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
   

def req_5(catalog, year_i, year_f, categoria):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    list_datos = lt.new_list()
    count_survey = 0
    count_census = 0
    pos = 0

    while pos < len(catalog["source"]):
        if catalog["year_collection"][pos] >= year_i and catalog["year_collection"][pos] <= year_f and catalog["statical_category"][pos] == categoria:
            if catalog["source"][pos] == "SURVEY":
                count_survey += 1
            else: count_census += 1
            lt.add_last(list_datos, [catalog["source"][pos], 
                                 catalog["year_collection"][pos],
                                 catalog["load_time"][pos],
                                 catalog["freq_collection"][pos],
                                 catalog["state_name"][pos],
                                 catalog["unit_measurement"][pos],
                                 catalog["commodity"][pos]])
        pos += 1
    numero_total = count_census + count_survey
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    return tiempo, numero_total, count_census, count_survey, list_datos

def req_6(catalog, fecha_i, fecha_f, departamento):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    list_datos = lt.new_list()
    count_survey = 0
    count_census = 0
    pos = 0

    while pos < len(catalog["source"]):
        if catalog["load_time"][pos] >= fecha_i and catalog["load_time"][pos] <= fecha_f and catalog["state_name"][pos] == departamento:
            if catalog["source"][pos] == "SURVEY":
                count_survey += 1
            else: count_census += 1
            lt.add_last(list_datos, [catalog["source"][pos], 
                                 catalog["year_collection"][pos],
                                 catalog["load_time"][pos],
                                 catalog["freq_collection"][pos],
                                 catalog["state_name"][pos],
                                 catalog["unit_measurement"][pos],
                                 catalog["commodity"][pos]])
        pos += 1
    numero_total = count_census + count_survey
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    return tiempo, numero_total, count_census, count_survey, list_datos


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
