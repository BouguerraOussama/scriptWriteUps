import socket
import math


HOST = "[challenge01.root-me.org](http://challenge01.root-me.org/)"  # The server's hostname or IP address
PORT = 52002  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	data = s.recv(1024)
	print(data)
	
	numbers = [int(s) for s in data.split() if s.isdigit()]
	print(f"nombres extrait de la chaine : {numbers}")
	
	square_root = math.sqrt(numbers[1])  * numbers[2]
	print(f"apres calcul racine(n1) * n2 = {square_root}")
	
	rounded_number = round(square_root, 2)
	
	print(f"rounded number : {rounded_number}")
	
	s.sendall((str(rounded_number) ).encode())
	data = s.recv(1024)
	print(data)
