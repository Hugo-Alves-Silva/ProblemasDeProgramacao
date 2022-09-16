from xmlrpc.client import ServerProxy

client = ServerProxy("http://localhost:9999/")

saldoMedio = float(input("Informe o saldo médio: "))




credito = client.valorCredito(saldoMedio) 
if saldoMedio >= 0:
    print(f"Saldo médio: {saldoMedio:.2f} e crédito: {credito:.2f}")
else:
    print("Erro na informação do saldo.")


