# Calculatrice Réseau

## Description
Un serveur et un client pour effectuer des calculs arithmétiques à distance.

### Contenu
- `server.py` : Serveur pour les calculs
- `client.py` : Client pour interagir avec le serveur
- `Dockerfile` : Image Docker pour le serveur
- `docker-compose.yml` : Automatisation du déploiement avec Docker Compose

### Commandes

Construire l'image Docker :
docker build -t calc .

Lancer avec Docker Compose :
docker-compose up --build -d

Changer le port :
docker run -e CALC_PORT=6767 -d calc

Vérifier que le conteneur est lancé : 
Docker ps

Puis lancer le fichier python client.py

