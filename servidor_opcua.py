from opcua import Server

# Criando um servidor OPC UA
server = Server()
server.set_endpoint("opc.tcp://localhost:4840")

# Criando um espaço de nomes
uri = "urn:example:opcua:server"
idx = server.register_namespace(uri)
print("idx",idx)

# Criando um objeto no servidor OPC UA
obj = server.get_objects_node().add_object(idx, "MyObject")

# Criando uma variável no objeto
var = obj.add_variable(idx, "MyVariable", 0)
var.set_writable(True)

# Iniciando o servidor OPC UA
server.start()
print("Servidor OPC UA iniciado. Endpoint:", server.endpoint)

try:
    while True:
        # Atualizando o valor da variável
        value = input("Digite um novo valor para MyVariable (q para sair): ")
        if value.lower() == "q":
            break
        var.set_value(int(value))
finally:
    # Encerrando o servidor OPC UA
    server.stop()
