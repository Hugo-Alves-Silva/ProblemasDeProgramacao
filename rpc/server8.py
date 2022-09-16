from operator import truediv
from xmlrpc.server import SimpleXMLRPCServer

def valorCredito(saldoMedio):
    if saldoMedio >=0.0 and saldoMedio <= 200.0:
        return 0.0
    elif saldoMedio >= 201.0 and saldoMedio <= 400.0:
        return saldoMedio * 0.2
    elif saldoMedio >= 401.0 and saldoMedio <= 600.0:
        return saldoMedio * 0.3
    elif saldoMedio >= 601.0:
        return saldoMedio * 0.4
    else: 
        return -1

server = SimpleXMLRPCServer(("localhost", 9999))

server.register_function(valorCredito, 'valorCredito')
server.serve_forever()
