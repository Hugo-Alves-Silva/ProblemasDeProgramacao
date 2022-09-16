from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

altura = float(input("Informe a altura em metros: "))
sexo = input("Informe o sexo: ")

pesoIdeal = client.pesoIdeal(altura, sexo)

print(f"Peso ideal: {pesoIdeal:.2f}")

