"""

Codigo que manipula as datas necessarias para acessar o banco de dados e retorna um vetor.

Autor: @onpprod

"""

from datetime import datetime, timedelta
import time

def dataVectorGen(data_1,data_2,data_format,delta_minutes):
    data_1_obj = datetime.strptime(data_1,data_format)
    data_2_obj = datetime.strptime(data_2,data_format)
    data_list = [data_1]
    while (data_1_obj < data_2_obj):
        data_1_obj = data_1_obj + timedelta(minutes=delta_minutes)
        data_str = data_1_obj.strftime(data_format)
        data_list.append(data_str)
    return data_list

"""
# Codigo para teste

dt_string1 = "01-01-2022 00:00:00"
dt_string2 = "01-02-2022 00:00:00"
dt_format = "%d-%m-%Y %H:%M:%S"

data_list = dataVectorGen(dt_string1,dt_string2,dt_format, 15)

for i in data_list:
    print(i)
    time.sleep(1)
"""