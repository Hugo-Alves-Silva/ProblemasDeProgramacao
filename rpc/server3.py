from xmlrpc.server import SimpleXMLRPCServer

def calculoMedia(a, b):
    return (a+b)/2

server = SimpleXMLRPCServer(("localhost", 9999))
server.register_function(calculoMedia, "calculoMedia")
server.serve_forever()
