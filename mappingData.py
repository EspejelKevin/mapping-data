import pandas as pd

def mapping():
    aux_cities = []
    cities = []
    states = []
    typeSettlements = []
    postalAdministrations = []
    municipalities = []
    aux_settlements = []
    settlements = []

    data = pd.read_csv("data.csv", delimiter=",", encoding="utf-8")
    for _, row in data.iterrows():
        city = (row.c_cve_ciudad, row.d_ciudad)
        state = (row.c_estado, row.d_estado)
        typeSettlement = (row.c_tipo_asenta, row.d_tipo_asenta)
        postalAdministration = (row.d_CP, row.c_oficina)
        municipality = (row.c_mnpio, row.D_mnpio, row.c_estado)
        settlement = (row.d_codigo, row.d_asenta, row.d_zona, row.id_asenta_cpcons, row.c_tipo_asenta, row.c_mnpio, row.c_cve_ciudad, row.d_CP)

        if city not in aux_cities:
            aux_cities.append(city)
        
        if state not in states:
            states.append(state)

        if typeSettlement not in typeSettlements:
            typeSettlements.append(typeSettlement)
        
        if postalAdministration not in postalAdministrations:
            postalAdministrations.append(postalAdministration)
        
        if municipality not in municipalities:
            municipalities.append(municipality)

        if settlement not in aux_settlements:
            aux_settlements.append(settlement)

    
    aux_cities = pd.DataFrame(aux_cities)
    aux_cities = aux_cities.dropna()
    for _, row in aux_cities.iterrows():
        cities.append((int(row[0]), row[1]))

    aux_settlements = pd.DataFrame(aux_settlements)
    aux_settlements = aux_settlements.astype(object).where(pd.notnull(aux_settlements), None)
    pd.options.display.max_rows
    pd.set_option("display.max_rows", None)
    for _, row in aux_settlements.iterrows():
        try:
            id_city = int(row[6])
        except:
            id_city = None
        
        settlements.append((row[1], row[0], row[2], row[3], row[4], row[5], id_city, row[7]))
    
    return settlements, typeSettlements, postalAdministrations, states, municipalities, cities

