import socket

HOST = "127.0.0.1"
PORT = 65432 # Poort waar de "server" op luistert. > 1023

# AF_INET: refereert naar de addres-familie IPv4
# SOCK_STREAM: refereert naar het TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) # Host zal op een specifiek IP-adres/Poort luisteren (verwacht een tuple).
    s.listen() # Log die het aantal nog-niet geaccepteerde connecties bijhoudt, vooraleer het systeem nieuwe connecties begint af te wijzen.
    conn, addr = s.accept() # connectie tot client
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # leest data die client stuurt
            if not data: # Als data leeg is heeft client de verbinding verbroken. "With" zorgt voor het automatisch sluiten van de socket.
                break
            print(data) # print data van client
            conn.sendall(data) # echo't data terug naar client