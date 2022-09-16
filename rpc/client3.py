from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

n1 = float(input("Informe N1: "))
n2 = float(input("Informe N2: "))

m = client.calculoMedia(n1, n2)

if m >= 7.0: 
    print("Aluno aprovado!")
elif m <= 3.0:
    print("Aluno reprovado.")
else:
    n3 = float(input("Informe a N3: "))
    if client.calculoMedia(m, n3) >= 5.0:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.") 


