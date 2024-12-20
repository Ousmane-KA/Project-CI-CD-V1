## Mise en place de Jenkins avec Dockerfile et Docker-Compose
## Mise en place de Sonarqube avec Docker compose
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

![image](https://github.com/user-attachments/assets/e7fde1bd-0aa6-449f-8b38-7d34fb49829b)





configuration de Sonarqube
Configuration de github
