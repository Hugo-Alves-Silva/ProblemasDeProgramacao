from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

nome = input("Informe o nome: ")
nivel = input("Informe o nível: ")
salarioBruto = float(input("Informe o salário bruto: "))  
numDependentes = int(input("Informe o número de dependentes: "))

salarioLiquido = client.novoSalario(nivel, salarioBruto, numDependentes) 

print(f"Nome: {nome}")
print(f"Nível: {nivel}")
if salarioLiquido != -1:
    print(f"O salário líquido: {salarioLiquido:.2f}.")
else:
    print("Erro, nível inválido.")

