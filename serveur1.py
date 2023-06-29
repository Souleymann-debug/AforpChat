import socket
import threading

# Définition de l'adresse IP et du port du serveur 2
HOST = 'localhost'
PORT = 5001

# Liste pour stocker les connexions des clients
clients = []

# Fonction pour gérer la communication avec un client
def handle_client(client_socket):
    while True:
        try:
            # Recevoir le message du client
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print(f"Message reçu : {data}")

                # Envoyer le message à tous les clients connectés
                for client in clients:
                    if client != client_socket:
                        client.send(data.encode('utf-8'))
            else:
                # Si aucune donnée n'est reçue, fermer la connexion avec le client
                client_socket.close()
                clients.remove(client_socket)
                break
        except:
            # En cas d'erreur de communication, fermer la connexion avec le client
            client_socket.close()
            clients.remove(client_socket)
            break

# Fonction principale pour démarrer le serveur
def start_server():
    # Créer un socket TCP/IP pour le serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lier le socket à l'adresse IP et au port du serveur
    server_socket.bind((HOST, PORT))

    # Mettre le serveur en mode écoute
    server_socket.listen(1)

    print("Le serveur est prêt à recevoir des connexions.")

    while True:
        # Accepter une connexion entrante
        client_socket, address = server_socket.accept()
        print(f"Connexion établie avec {address[0]}:{address[1]}")

        # Ajouter le client à la liste des clients connectés
        clients.append(client_socket)

        # Créer un thread pour gérer la communication avec le client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Démarrer le serveur
start_server()
