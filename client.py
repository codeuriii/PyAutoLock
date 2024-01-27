import socket
import time

# Adresse IP et port du serveur
HOST = '127.0.0.1'
PORT = 65432

while True:
    # Création d'un objet socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connexion au serveur
        client_socket.connect((HOST, PORT))
        # Envoi de données au serveur
        client_socket.sendall(b'Donnees envoyees par le client')
        # Réception de la réponse du serveur
        data = client_socket.recv(1024)

    print('Reçu:', data.decode())
    # Attente de 1 seconde avant d'envoyer une nouvelle fois des données
    time.sleep(1)
