
# PROJET DE MISE EN PLACE D'UNE PIPELINE CI-CD

## A) Deploiement des serveur sur AZURE : 

![image](https://github.com/user-attachments/assets/7ca050a5-110b-457d-9287-05a5038bd190)





### 1.Configuration de  CLI Azure

### Déploiement des trois serveurr Azure

Pour le deploiementdes trois VM voir la configutation dans le dossier Terraform.


## PLAN : 

![image](https://github.com/user-attachments/assets/7e3850a4-00a9-4b41-bfaa-b222ef486c34)


**************************
Voici une version corrigée et plus structurée de votre README :

---

# Mise en place de Jenkins et Sonarqube avec Dockerfile et Docker-Compose

## Configuration de Jenkins

### 1. Création du projet Jenkins
```bash
mkdir Jenkins-Projet # Création du dossier du projet Jenkins
cd Jenkins-Projet
# Ajouter le fichier `docker-compose.yml` correspondant à Jenkins ici
```

- Pour installer Jenkins :
  1. Exécutez `docker-compose up -d` pour démarrer les services.
  2. Builder l'image de Jenkins si nécessaire, puis redémarrez avec `docker-compose up -d`.

---

## Configuration de Sonarqube

### 1. Création du projet Sonarqube
```bash
mkdir Sonarqube # Création du dossier du projet SonarQube
cd Sonarqube
# Ajouter le fichier `docker-compose.yml` correspondant à SonarQube ici
```

- Pour installer SonarQube :
  - Exécutez `docker-compose up -d` pour démarrer les services.

---

## A. Configuration de Jenkins

### 1. Installation des plugins
- Installez les plugins nécessaires :
  - SSH2
  - Docker
  - SonarQube

![Plugins Jenkins](https://github.com/user-attachments/assets/bd211ba2-fea6-4bd4-a3b4-2d6b1a3a4197)

---

### 2. Installation et configuration de SonarQube

- Accédez aux **Tools** dans Jenkins pour configurer SonarQube :

![Configuration Tools](https://github.com/user-attachments/assets/ee5b6baf-95b8-4dd8-96f8-68b3bc391d09)

#### Étapes :
1. **Générer un token** depuis SonarQube et créer un projet.
2. Intégrer SonarQube dans la section **Système** de Jenkins :
   - Ajoutez l'URL de SonarQube et le token généré.

![Configuration système SonarQube](https://github.com/user-attachments/assets/8220a056-1220-4711-a94f-a61ed690c996)

---

### 3. Installation de Docker sur Jenkins

- Configurez Docker dans la section **Tools** de Jenkins.

![Configuration Tools Docker](https://github.com/user-attachments/assets/abc4cf99-2da0-4339-ad21-cf00e40c9e05)

- Intégrez Docker dans la section **Système** de Jenkins.

![Configuration système Docker](https://github.com/user-attachments/assets/4c286468-d56f-48a8-a6d5-1ab488e8c582)

---

## B. Mise en place du pipeline Jenkins

### 1. Création d’un job
- Créez un nouveau job dans Jenkins en sélectionnant un **Item**.

![Création d’un job](https://github.com/user-attachments/assets/e7fde1bd-0aa6-449f-8b38-7d34fb49829b)

---

### 2. Configuration du job

- Récupérez l’URL du dépôt GitHub et configurez le pipeline :
  - Ajoutez l'URL du dépôt GitHub et les identifiants de connexion.

![Ajout URL Git](https://github.com/user-attachments/assets/f845e986-34f1-4fb2-8466-b927e91f5808)

![Configuration GitHub Pipeline](https://github.com/user-attachments/assets/bf23aa70-7c40-4dbc-bbaa-9d0640e0496b)

![Ajout clé SonarQube](https://github.com/user-attachments/assets/4c2108c7-753e-4acd-a8c9-06b4a27e67ef)

#### Remarque : 
Ajoutez la configuration SonarQube avec le **project key** généré.

---

### 3. Utilisation de Remote Shell
- Configurez un **Remote Shell** pour effectuer un `git clone` depuis votre serveur Docker.

![Configuration Remote Shell](https://github.com/user-attachments/assets/53c3a2f7-ca83-48d1-8421-c7def37cd5fa)

- Configurez une deuxième commande pour builder l'image Docker.

![Builder une image Docker](https://github.com/user-attachments/assets/b9f0ddf8-82ee-472d-8300-2ee0463dfb29)

---

### 4. Configuration du Webhook GitHub
- Ajoutez un Webhook sur GitHub :
  - L'URL sera sous la forme : `http://<jenkins_server>/github-webhook/`

![Configuration Webhook](https://github.com/user-attachments/assets/b7a19df0-4217-4953-b4c7-f3f4286ca401)

---

#### Remarque importante :
- Le dossier `App` contient les fichiers pour tester le pipeline.
- **Ignorez le dossier `sonar-jenkins`.**

### Lancement :
- Vous pouvez maintenant démarrer votre job dans Jenkins !

---

Cette version est corrigée pour améliorer la grammaire, la lisibilité et l'organisation. Si vous voulez personnaliser davantage ou ajouter des éléments, dites-le-moi !


*************************

## Mise en place de Jenkins avec Dockerfile et Docker-Compose

mkdir Jenkins-Projet #création du dossier projet Jenkins

cd Jenkins-Projet #Puis il faudra mettre le fichier du docker compose de jenkins

- Pour l'installation de , il faudra faire un docker-compose up -d,
   

- Pour l'installation de jenkins sur le serveur, il faudra builder l'image de jenkins ensuite faire un docker-compose up -d
## Mise en place de Sonarqube avec Docker compose

mkdir Sonarqube #création du dossier projet Sonar

cd Sonarqube #Puis il faudra mettre le fichier du docker compose de Sonarqube

- Pour l'installation de sonarqube, il faudra faire un docker-compose up -d,
   
## A) Configuration de Jenkins

- Installation des plugin :

![image](https://github.com/user-attachments/assets/bd211ba2-fea6-4bd4-a3b4-2d6b1a3a4197)

SSH2, 
Docker,
Sonarqube

### 1. Installation de Sonarqube et Configuration : 

- Installation de sonarqube sur Jenkins, il faudra aller sur tools de jenkins :

![image](https://github.com/user-attachments/assets/ee5b6baf-95b8-4dd8-96f8-68b3bc391d09)

Remarque: Il faudra générer des tocken sur Sonarqube et créer un projet

- Il faudra faire l'intégration sur la partie Systeme de jenkins en ajoutant url, le token,

![image](https://github.com/user-attachments/assets/8220a056-1220-4711-a94f-a61ed690c996)

### 2. Installation de docker serveur sur jenkins :

- Installation de docker serveur sur tools :

![image](https://github.com/user-attachments/assets/abc4cf99-2da0-4339-ad21-cf00e40c9e05)

- Integration de docker serveur sur Sytème de jenkins :

![image](https://github.com/user-attachments/assets/4c286468-d56f-48a8-a6d5-1ab488e8c582)

## B) Mise en place du pipeline : 

### 1. Création d'un job : 

On peut créer des job en cliquant sur Item puis choisir l'option

![image](https://github.com/user-attachments/assets/e7fde1bd-0aa6-449f-8b38-7d34fb49829b)

### 2. Confiugration du job : 

- On recupère URL github, qu'on ajoute sur le pipeline l'option git avec les identifiant de connexion :
  
![image](https://github.com/user-attachments/assets/f845e986-34f1-4fb2-8466-b927e91f5808)

![image](https://github.com/user-attachments/assets/bf23aa70-7c40-4dbc-bbaa-9d0640e0496b)

![image](https://github.com/user-attachments/assets/4c2108c7-753e-4acd-a8c9-06b4a27e67ef)

![image](https://github.com/user-attachments/assets/e160fa73-0d0a-48f5-85d8-e4414818a6c5)

Remarque : on a ajouter la partie sonar avec le projectkey qu'on avait créer 

- On va utiliser l'option remote shell pour faire un git clone depuis notre serveur docker

  ![image](https://github.com/user-attachments/assets/53c3a2f7-ca83-48d1-8421-c7def37cd5fa)

  - On va choisir une deuxieme remote shell pour builder notre image :
 
    ![image](https://github.com/user-attachments/assets/b9f0ddf8-82ee-472d-8300-2ee0463dfb29)

- Confiugration du Webhook sur github

![image](https://github.com/user-attachments/assets/b7a19df0-4217-4953-b4c7-f3f4286ca401)

On va mettre l'url du serveur jenkins sous la forme : http://<jenkins_server>/github-webhook/

  Remarque : le dossier App permet de faire les tests de notre pipeline donne il faudra pas prendre en compte le dossier sonar-jenkins.

On peut demarrer notre Job!!!!!!
