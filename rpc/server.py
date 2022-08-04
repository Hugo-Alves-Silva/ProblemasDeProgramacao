from xmlrpc.server import SimpleXMLRPCServer
'''
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

''' 
def calculo(cargo, salario):
    if cargo.lower() == 'programador' or  cargo.lower() == 'programadora':
        return salario + salario * 0.18
    elif cargo.lower() == 'operador' or cargo.lower() == 'operadora':
        return salario + salario * 0.2
    else: 
        return salario

server = SimpleXMLRPCServer(("localhost", 9999))
server.register_function(calculo, "calculo")

server.serve_forever()
