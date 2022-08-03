import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
notas = [
    [7.5, 6.5, 5.5], 
    [8.3, 7.2, 9.5],
    [0.0, 0.0, 0.0],
    [4.5, 7.9, 8.8],
    [3.2, 8.5, 7.0],
    [0.0, 0.0, 0.0],
    [9.9, 10.0, 9.8],
    [10.0, 10.0, 10.0],
    [4.5, 8.5, 10.0]
    
]
while True:
    for i in notas:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("NOTAS*" + str(i[0])+ "*"+ str(i[1]) +"*"+str(i[2]))
       
