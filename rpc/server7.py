from operator import truediv
from xmlrpc.server import SimpleXMLRPCServer

def podeAposentar(sexo, idade, tempo):
    if sexo.lower() == 'masculino':
        if idade >= 65 and tempo >= 35:
            return True
        else: 
            return False
    else:
        if idade >= 60 and tempo >= 30:
            return True
        else: 
            return False


server = SimpleXMLRPCServer(("localhost", 9999))

server.register_function(podeAposentar, "podeAposentar")
server.serve_forever()
