# dj-simple-crm

Projet : Création d'un mini crm pour l'école ipssi , pour apprendre les test d'intégration , celui çi à été réaliser en full django.

Lancement du projet :

docker-compose up --build

puis :

docker-compose exec web python manage.py migrate

access creation a la base de données : 

docker-compose exec web python manage.py createsuperuser


Se diriger vers : http://localhost:8000//contacts
acces a l'admin : http://localhost:8000/admin

Pour les test :

docker-compose exec web python manage.py test


