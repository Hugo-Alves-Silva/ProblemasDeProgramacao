from xmlrpc.server import SimpleXMLRPCServer

def pesoIdeal(altura, sexo):
    if sexo.lower() == 'masculino':
        return (72.7 * altura) - 58
    else:
        return  (62.1 * altura) - 44.7

server = SimpleXMLRPCServer(("localhost", 9999))

server.register_function(pesoIdeal, "pesoIdeal")
server.serve_forever()
