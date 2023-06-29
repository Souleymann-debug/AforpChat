import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Definition de l'adresse IP et du port du serveur
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5002

# Fonction pour recevoir et afficher les messages du serveur
def receive_messages():
    global client_socket  # Declare client_socket as a global variable
    global text_box  # Declare text_box as a global variable
    while True:
        try:
            # Recevoir le message du serveur
            message = client_socket.recv(1024).decode('utf-8')
            text_box.tag_config("left", justify='left')
            text_box.insert(tk.END, message + '\n', "left")
        except:
            # En cas d'erreur de communication, fermer la connexion avec le serveur
            client_socket.close()
            break

# Fonction pour envoyer les messages au serveur
def send_message(event=None):  # Add event=None to handle the Enter key press event
    global client_socket  # Declare client_socket as a global variable
    global text_box  # Declare text_box as a global variable
    message = input_box.get()
    client_socket.send(message.encode('utf-8'))
    text_box.tag_config("right", justify='right')
    text_box.insert(tk.END, message + '\n', "right")
    input_box.delete(0, tk.END)

# Fonction principale pour démarrer le client
def start_client():
    global client_socket  # Declare client_socket as a global variable
    global input_box  # Declare input_box as a global variable
    global text_box  # Declare text_box as a global variable

    # Créer un socket TCP/IP pour le client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Établir la connexion avec le serveur
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connexion établie avec le serveur.")

    # Créer un thread pour recevoir les messages du serveur
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    # Créer la fenêtre Tkinter
    window = tk.Tk()
    window.title("Chat App")

    # Zone de texte pour afficher les messages
    text_box = ScrolledText(window, height=10, width=50)
    text_box.pack()

    # Champ de saisie pour envoyer les messages
    input_box = tk.Entry(window, width=50)
    input_box.pack()
    input_box.focus()  # Set focus on the input box

    # Lier l'événement de pression de la touche Enter à la fonction send_message
    window.bind("<Return>", send_message)

    # Bouton pour envoyer le message
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack()

    # Lancer la boucle principale Tkinter
    window.mainloop()

# Démarrer le client
start_client()
