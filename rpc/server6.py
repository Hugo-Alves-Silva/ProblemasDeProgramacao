from xmlrpc.server import SimpleXMLRPCServer

def novoSalario(nivel, salarioBruto, numDependentes):
    if nivel == 'A':
        if numDependentes == 0:
            return salarioBruto - salarioBruto * 0.03
        else:
            return salarioBruto - salarioBruto * 0.08
    elif nivel == 'B':
        if numDependentes == 0:
            return salarioBruto - salarioBruto * 0.05
        else:
            return salarioBruto - salarioBruto * 0.1
    elif nivel == 'C':
        if numDependentes == 0:
            return salarioBruto - salarioBruto * 0.08
        else:
            return salarioBruto - salarioBruto * 0.15
    elif nivel == 'D':
        if numDependentes == 0:
            return salarioBruto - salarioBruto * 0.1
        else:
            return salarioBruto - salarioBruto * 0.17
    else: return -1 
   

server = SimpleXMLRPCServer(("localhost", 9999))

server.register_function(novoSalario, "novoSalario")
server.serve_forever()
