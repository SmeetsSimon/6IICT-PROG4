import socket

# Verbind met de server (juiste gegevens nodig)
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hendrik zegt hallo") # b keyword zorgt ervoor dat boodschap van de klasse "bytes" wordt... COntroleer met type(variabelnaam)
    data = s.recv(1024)

print(f"{data}")

#feiohff