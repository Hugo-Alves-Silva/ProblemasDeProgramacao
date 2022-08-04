from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

nome = input("Informo o nome: ")
cargo = input("Informe o cargo: ")
salario = float(input("Informe o salario: "))


novoSalario = client.calculo(cargo, salario)
print("")
print(f"Nome: {nome}")
print(f"Cargo: {cargo}")
print(f"Salário: {novoSalario}")
print("")
'''
print(f"num1 + num2 = {resultadoSoma}")
print(f"num1 - num2 = {resultadoSubtracao}")
print(f"num1 * num2 = {resultadoMultiplicacao}")
'''
