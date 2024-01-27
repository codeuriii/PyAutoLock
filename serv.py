import socket

# Adresse IP et port du serveur
HOST = '127.0.0.1'
PORT = 65432

# Création d'un objet socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Liaison de l'adresse et du port
server_socket.bind((HOST, PORT))
# Attente de connexion
server_socket.listen()
print("Le serveur écoute...")

while True:
    # Acceptation de la connexion
    conn, addr = server_socket.accept()
    with conn:
        print('Connecté par', addr)
        # Définition du timeout pour la réception
        conn.settimeout(5)  # Timeout de 5 secondes
        try:
            # Réception des données du client
            data = conn.recv(1024)
            if not data:
                print("Ne reçoit rien")
            else:
                print('Reçu:', data.decode())
                # Envoi d'une réponse au client
                conn.sendall(b'Donnees recues par le serveur')
        except socket.timeout:
            print("Ne reçoit rien")
