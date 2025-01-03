
# PROJET DE MISE EN PLACE D'UNE PIPELINE CI-CD

## A) Deploiement des serveur sur AZURE : 

### 1.Configuration de  CLI Azure

### Déploiement des trois serveurr Azure

Pour le deploiementdes trois VM voir la configutation dans le dossier Terraform.


## PLAN : 

![image](https://github.com/user-attachments/assets/7e3850a4-00a9-4b41-bfaa-b222ef486c34)






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
