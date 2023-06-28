import socket
import threading

# Définition de l'adresse IP et du port du serveur
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Fonction pour recevoir et afficher les messages du serveur
def receive_messages(client_socket):
    while True:
        try:
            # Recevoir le message du serveur
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # En cas d'erreur de communication, fermer la connexion avec le serveur
            client_socket.close()
            break

# Fonction principale pour démarrer le client
def start_client():
    # Créer un socket TCP/IP pour le client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Établir la connexion avec le serveur
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connexion établie avec le serveur.")

    # Créer un thread pour recevoir les messages du serveur
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Boucle principale pour envoyer les messages au serveur
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Démarrer le client
start_client()
