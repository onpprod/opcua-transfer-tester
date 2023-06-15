import random
from pymongo import MongoClient
from datetime import datetime, timedelta

# Conectar ao servidor MongoDB
client = MongoClient("localhost",27017)

# Selecionar o banco de dados
db = client['mydb']

# Selecionar a coleção
collection = db['machine_1']

#time

datetime_string = "01-01-2022 00:00:00"
datetime_format = "%d-%m-%Y %H:%M:%S"
datetime_obj = datetime.strptime(datetime_string,datetime_format)

print(datetime_obj)

datetime_novo = datetime_obj + timedelta(minutes=15)

print(datetime_novo)

datetime_novo_string = datetime_novo.strftime(datetime_format)

print(datetime_novo_string)


# Lista de possíveis valores para o campo 'nome'
dados_machine = {
    "nome":"empilhadeira",
    "local": "Facilities",
    "temperatura" : [{"01-01-2022 00:00:00":27}]
}

#nova_temperatura = {"temperatura" :{"01-01-2022 00-45-00":35}}
#add_novo_dado = {"$addToSet":nova_temperatura}

filtro = {"temperatura": {"$exists": True}}

collection.insert_one(dados_machine)

for i in range(20):
    temp = random.randint(20,40)
    nova_temperatura = {"temperatura" :{"01-01-2022 00-45-00":temp}}
    add_novo_dado = {"$addToSet":nova_temperatura}
    collection.update_one(filtro,add_novo_dado)

# Fechar a conexão com o servidor MongoDB
client.close()