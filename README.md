# restaurant-site

🍽️ Le Restaurant

Le Restaurant est une version avancée de Pizza Mama, développée avec Django, HTML, et CSS. Ce projet propose une interface dynamique pour présenter les informations d’un restaurant, ses horaires d’ouverture, un système de réservation, ainsi qu’un menu détaillé (pizzas, plats, vins) organisé par catégories.

📋 Fonctionnalités
	•	Page d’accueil :
	•	Présentation du restaurant avec une description.
	•	Affichage des horaires d’ouverture.
	•	Page de menu :
	•	Organisation en catégories : Pizzas, Plats, Vins.
	•	Navigation facile entre les catégories grâce à des boutons dédiés.
	•	Page de réservation :
	•	Interface utilisateur élégante avec un design réalisé en HTML et CSS.

🛠️ Technologies utilisées
	•	Backend : Django
	•	Frontend : HTML et CSS
	•	Base de données : SQLite (par défaut, peut être remplacée en production)

⚙️ Installation

1. Clonez le dépôt

git clone https://github.com/Alioune4002/restaurant-site.git
cd site-resto

2. Créez un environnement virtuel et activez-le

python -m venv env
# Sur Windows :
env\Scripts\activate
# Sur macOS/Linux :
source env/bin/activate

3. Installez les dépendances

pip install -r requirements.txt

4. Configurez la base de données

Appliquez les migrations pour configurer la base de données :

python manage.py makemigrations
python manage.py migrate

5. Lancez le serveur local

python manage.py runserver

Le site sera accessible à l’adresse suivante : http://127.0.0.1:8000.

6. (Optionnel) Créez un super-utilisateur pour gérer les données

python manage.py createsuperuser

🖥️ Pages du site
	1.	Accueil :
	•	Présentation du restaurant.
	•	Horaires d’ouverture.
	•	Bouton pour réserver.
	2.	Menu :
	•	Navigation entre les catégories (Pizzas, Plats, Vins).
	•	Affichage des plats avec descriptions et prix.

🌟 Améliorations futures
	•	Ajouter une page pour les avis des clients.
	•	Mettre en place un système de réservation avec formulaire + envoi d’email pour confirmer les réservations.
	•	Intégrer un système de gestion de stock pour les plats du menu.
