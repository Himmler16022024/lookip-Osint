DEV BY Himmler Discord <@1131256234440392817>
# lookip-Osint

🕵️‍♂️🔍 Outil de Recherche IP

Description :
Le lookip Tool est un script Python simple et efficace permettant de rechercher des informations détaillées
sur une adresse IP donnée. En interrogeant deux services API publics, IPinfo et ip-api, cet outil fournit des détails tels que la localisation, 
l'organisation, le FAI (Fournisseur d'Accès Internet), et bien plus encore.

📋 Prérequis
Assurez-vous d'avoir Python installé sur votre machine. Le script utilise la bibliothèque requests, que vous pouvez installer via pip si elle n'est pas déjà présente :

pip install requests

🛠️ Utilisation
Ouvrez un terminal.
Exécutez le script avec l'adresse IP que vous souhaitez rechercher en argument :

・python lookip.py <ADRESSE_IP>

Par exemple :

・python lookip.py 8.8.8.8

📊 Exemple de Sortie

Informations pour l'adresse IP : 8.8.8.8

Données IPinfo :
  IP: 8.8.8.8
  Nom d'hôte: dns.google
  Ville: Mountain View
  Région: California
  Pays: US
  Localisation: 37.3860,-122.0840
  Organisation: AS15169 Google LLC
  Code postal: 94035
  Fuseau horaire: America/Los_Angeles

Données ip-api :
  Pays: United States
  Région: California
  Ville: Mountain View
  Code postal: 94035
  Latitude: 37.386
  Longitude: -122.0838
  FAI: Google LLC
  Organisation: Google LLC
  AS: AS15169 Google LLC
  DNS inversé: dns.google
  Mobile: False
  Proxy: False

Himmler / discord.gg/searchhub

🧩 Fonctionnalités
🔍 Recherche d'informations détaillées sur une adresse IP.
🌐 Agrégation des données provenant de deux API (IPinfo et ip-api).
📋 Affichage clair et structuré des résultats dans le terminal avec un message personnalisé à chaque résultat.
📂 Structure du Projet
lookip.py : Le script principal pour effectuer la recherche IP.
🤝 Contributions
Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou des corrections, veuillez soumettre une pull request.

📜 License : 
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
