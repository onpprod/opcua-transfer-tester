import asyncio
from asyncua import ua, Server
from pymongo import MongoClient

async def read_document(parent, collection, filter):
    # Conecta ao MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['Facilities']
    documents = db[collection].find(filter)

    # Cria uma variável do tipo String para armazenar o documento
    variable = await parent.add_variable(ua.NodeId('Documento'), 'Documento', '')
    
    # Lê o documento do MongoDB
    for document in documents:
        variable.set_value(str(document))

    # Encerra a conexão com o MongoDB
    client.close()

async def main():
    # Cria o servidor OPC UA
    server = Server()
    await server.init()
    
    # Configura o endereço e o nome do servidor
    server.set_endpoint("opc.tcp://0.0.0.0:4840/server")
    server.set_server_name("AsyncUA MongoDB Server")

    # Cria um objeto de nó root
    root = server.get_root_node()
    
    # Cria um objeto de nó "Objects" sob o nó root
    objects = server.get_objects_node()
    print(objects)
    
    # Cria um objeto de nó "Documents" sob o nó "Objects"
    documents = await objects.add_folder(ua.NodeId('Documents'), 'Documents')
    
    # Chama a função para ler o documento do MongoDB
    await read_document(documents, 'collection_name', {'filter_key': 'filter_value'})

    # Inicia o servidor OPC UA
    async with server:
        print("Starting server...")
        while True:
            await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
