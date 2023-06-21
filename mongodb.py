'''
Codigo para gerar um banco de dados Mongo

Autor : @onpprod

'''

import random
from pymongo import MongoClient
from datetime import datetime, timedelta
import numpy 
import time

#==============================
# Conectar ao servidor MongoDB
client = MongoClient("localhost",27017)

# Selecionar o banco de dados
db = client['Facilities']

# Selecionar a coleção
collection = db['empilhadeira_1']

#==============================
#time

dt_string = "01-01-2022 00:00:00"
dt_format = "%d-%m-%Y %H:%M:%S"
dt_obj = datetime.strptime(dt_string,dt_format)

#==============================
# Lista de possíveis valores para o campo 'nome'
dados_machine = {
    
    "nome":"empilhadeira1",
    "local":"facilities",
}

#checar se existe o documento
query = {"nome": "empilhadeira1"}
document_exists = collection.find_one(query) is not None
print(document_exists)

if document_exists:
    print("O documento de dados ja existe")

else:
    print("O documento de dados nao existe, inserindo...")
    collection.insert_one(dados_machine)
#==============================


for i in range(1000000):
    #checar se existe documento
    print("=========================================================")
    dt_obj_new = dt_obj + timedelta(minutes=(15*i))
    dt_string = dt_obj_new.strftime(dt_format)
    query = {"time":dt_string}
    document_exists = collection.find_one(query) is not None

    if document_exists:
        print("O documento ",i," ja existe")
    else:
        print("O documento ",i," nao existe, inserindo...")
        temp = random.randint(20,40)
        documento = {
            "time" : dt_string,
            "temp" :temp}
        result = collection.insert_one(documento)
        print("ID do documento inserido: ",result.inserted_id)

    #time.sleep(0.1)

#==============================
# Fechar a conexão com o servidor MongoDB
client.close()