import asyncio
from asyncua import Client

async def main():
    # Cria o cliente OPC UA
    client = Client(url="opc.tcp://localhost:4840/server")

    # Conecta ao servidor OPC UA
    async with client:
        # Conecta ao endpoint do servidor OPC UA
        await client.connect()

        # Obtém o objeto de nó root
        root = client.get_root_node()

        # Obtém o nó com o identificador de nó desejado (i=85)
        node = await root.get_child(["0:Objects", "2:Documents", "i=85"])

        # Obtém o valor do nó
        value = await node.read_value()
        
        # Imprime o valor na tela
        print("Valor do nó i=85:", value)

if __name__ == "__main__":
    asyncio.run(main())
