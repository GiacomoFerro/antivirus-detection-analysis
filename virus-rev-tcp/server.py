import socket

conn = socket.socket()
conn.bind(("0.0.0.0",1996)) #apro sulla porta scelta
conn.listen(1)#inizio ad ascoltare per connessioni
client, a = conn.accept()
print ("Connesso")
while True: 
    #per tenere accesa la connessione, al limite termino con ctrl-c, 
    #ricordarsi di uccidere il processo che usa la porta (lsof -i :<porta>) 
    #e (sudo kill -9 <process-id>)
    command = raw_input("")
    client.send(command)
    output = client.recv(99999)
    print (output)