import socket
import logging

# Configurer le logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def calculate_expression(expression):
    try:
        # Évaluer l'expression mathématique
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Erreur lors du calcul : {e}"

def main():
    host = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
    port = 6767

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        logging.info(f"Serveur démarré sur {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                logging.info(f"Connexion acceptée de {client_address}")
                
                # Envoyer un message de bienvenue au client uniquement une fois au début
                client_socket.sendall("Bienvenue sur le serveur de calculatrice!".encode('utf-8'))
                
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    expression = data.decode('utf-8').strip()
                    logging.info(f"Reçu : {expression}")
                    
                    # Calculer l'expression et envoyer la réponse
                    result = calculate_expression(expression)
                    client_socket.sendall(result.encode('utf-8'))

if __name__ == '__main__':
    main()
