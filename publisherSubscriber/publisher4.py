import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
informacoes = [
    [1.75, 'masculino'], 
    [1.75, 'feminino'],
    [1.72, 'masculino'],
    [1.78, 'feminino'],
    [1.80, 'masculino'],
    [1.55, 'feminino'],
    [1.60, 'masculino'],
    [1.95, 'masculino'],
    [1.65, 'feminino'],
    [1.50, 'feminino']
]
while True:
    for i in informacoes:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("PESO*" + str(i[0])+ "*"+ str(i[1]))
       
