# devops-docker-cours

### Le dossier "Exo" comporte les exercices fait en cours.

### Tout les autres dossiers sont pour le fonctionnement du projet suivant :

Dans ce projet vous devrez packager et déployer une application web simple en production sur une VM via docker. 

## Partie 1 - construction manuelle de l'image

Faire en sorte de packager une application web que vous avez déjà développée ou un petit web service simple avec docker. 

Connectez vous à la machine virtuelle mise à disposition  et déployer un conteneur de votre application. Pour cela vous pourrez faire un docker build sur la machine. 

Vous pourrez lancer le conteneur avec docker-compose. 

Pour récupérer le code de votre projet sur la VM, utiliser git

## Partie 2 - Construction de l'image dans une CI

On utiliser une CI/CD pour : 

lancer un petit test unitaire simple
si le test unitaire passe, créer une image docker qui sera push sur le registry dockerhub
Ensuite pour déployer le conteneur sur la VM cible, vous n'aurez qu'à faire un docker pull / et lancer le conteneur sans avoir à build vous même l'image qui aura été build par la CI

## Partie 3 

faire en sorte que votre application web se connecter à une base de donnée comme Mysql, Postgre ou Mongo et packager à nouveau l'application. Il faudra un conteneur pour le web service et un conteneur pour la base. Les deux conteneurs devront pouvoir communiquer entre eux

## Pour tester la connection entre les containers il suffit de ce rendre sur la page 'localhost:5000/fruits'