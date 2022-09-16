from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

idade = int(input("Informe a idade: "))

categoriaNadador = client.categoria(idade)
print(f"A categoria: {categoriaNadador}")


