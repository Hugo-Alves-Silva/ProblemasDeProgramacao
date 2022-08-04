from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

nome = input("Informo o nome: ")
sexo = input("Informe o sexo: ")
idade = int(input("Informe a idade: "))


flag = client.calculo(sexo, idade)

print("")
if flag:
    print(f"{nome} é maior de idade")
else: 
    print(f"{nome} não é maior de idade.")
print("")

