# 🕵️‍♂️🔍 Tool de Recherche IP
Le lookip Tool est codé en Python avec une utilisation simple et efficace permettant de rechercher des informations détaillées sur une adresse IP donnée.

En envoyant deux requêtes aux deux API publics, IPinfo et ip-api, ce tool donne des détails tels que la localisation, 

l'organisation, le FAI (Fournisseur d'Accès Internet), et bien plus encore.

# 📋Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Le script utilise la bibliothèque requests, que vous pouvez installer via pip si elle n'est pas déjà présente :
```
pip install requests
```
# 🛠️ Utilisation

Ouvrez un terminal.

Exécutez le script :
```
python lookip.py
```
Sélectionnez l'option souhaitée dans le menu principal :

1 pour rechercher une adresse IP.

2 pour afficher votre propre adresse IP publique.

Si vous choisissez de rechercher une adresse IP, entrez l'adresse IP lorsque vous y êtes invité.

# 📊 Exemple de sortie

Voici un exemple de sortie pour une recherche d'adresse IP :

```
==================================================
Informations pour l'adresse IP : 8.8.8.8
==================================================
🔍 Données IPinfo :
  IP: 8.8.8.8
  Nom d'hôte: dns.google
  Ville: Mountain View
  Région: Californie
  Pays: États-Unis
  Localisation: 37.3860,-122.0840
  Organisation: AS15169 Google LLC
  Code postal: 94035
  Fuseau horaire: America/Los_Angeles
==================================================
🌐 Données ip-api :
  Pays: États-Unis
  Région: Californie
  Ville: Mountain View
  Code postal: 94035
  Latitude: 37.386
  Longitude: -122.0838
  FAI: Google LLC
  Organisation: Google LLC
  AS: AS15169 Google LLC
  DNS inversé: dns.google
  Mobile: Faux
  Proxy: Faux
==================================================
Himmler / discord.gg/searchhub
```

🧩 Fonctionnalités

🔍 Recherche d'informations détaillées sur une adresse IP.

🌐 Agrégation des données provenant de deux API (IPinfo et ip-api).

📋 Affichage clair et structuré des résultats dans le terminal avec un message personnalisé à chaque résultat.

📂 Structure du Projet

lookip.py : Le script principal pour effectuer la recherche IP.

🤝 Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou des corrections, veuillez soumettre une pull request.

📜 Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
