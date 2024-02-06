# Formulaire de Connexion

Ce projet est un formulaire de connexion développé en utilisant Flask, un framework web Python.

## Prérequis

Avant de pouvoir exécuter le formulaire de connexion, assurez-vous de suivre ces étapes :

1. **Démarrer un serveur web local et MySQL** :
   - XAMPP : Téléchargez et installez XAMPP depuis [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html). Une fois installé, démarrez le serveur Apache et MySQL depuis le panneau de contrôle de XAMPP.
   - WAMP : Téléchargez et installez WAMP depuis [https://www.wampserver.com/en/](https://www.wampserver.com/en/). Après l'installation, démarrez le serveur WAMP. Assurez-vous que le service MySQL est également démarré.
   - LAMPP : Téléchargez et installez LAMPP depuis [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html). Une fois installé, démarrez le serveur Apache et MySQL en exécutant la commande `sudo /opt/lampp/lampp start`.

2. **Créer la base de données** :
   - Exécutez le fichier `database.sql` fourni avec le projet pour créer la base de données "authentification".

3. **Installer les dépendances Python** :
   - Ouvrez votre terminal et assurez-vous d'être dans le répertoire du projet.
   - Exécutez la commande suivante pour installer les dépendances requises :

     ```
     pip install -r requirements.txt
     ```

## Exécution

Après avoir satisfait aux prérequis, vous pouvez exécuter l'application en suivant ces étapes :

1. **Lancer l'application** :
   - Exécutez le fichier `app.py` en utilisant la commande suivante dans votre terminal :

     ```
     python app.py
     ```

2. **Accéder au formulaire de connexion** :
   - Ouvrez votre navigateur web et allez à l'URL suivante :

    http://127.0.0.1:5000/  (Le port par défaut est 5000 mais il se peut qu'il soit différent en fonction de votre configuration)

   - Vous devriez être redirigé vers le formulaire de connexion où vous pourrez saisir vos informations d'identification.

