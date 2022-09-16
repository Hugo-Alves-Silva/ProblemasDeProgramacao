from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

nome = input("Informe o nome: ")
sexo = input("O sexo: ")
idade = int(input("Idade: "))
tempo = int(input("Tempo: "))


aposentadoria = client.podeAposentar(sexo, idade, tempo) 



if aposentadoria:
    print(f"{nome} já pode se aposentar.")
else:
    print(f"{nome} não pode se aposentar.")

