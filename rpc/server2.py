from xmlrpc.server import SimpleXMLRPCServer

def calculo(sexo, idade):
    if sexo.lower() == 'masculino':
        if idade >=18: 
            return True
        else: 
            return False
    else:
        if idade >= 21: 
            return True
        else: 
            return False
    

server = SimpleXMLRPCServer(("localhost", 9999))
server.register_function(calculo, "calculo")

server.serve_forever()
