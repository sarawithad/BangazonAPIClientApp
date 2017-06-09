# Bangazon Rest API
### An open API for Banazon to give customers access to the Bangazon data
---
# Installations and other requirements for running the app
* First fork this project to your repo and then clone it down to your machine. 
* If you do not have Django and Django rest framework you will need `pip install django` and `pip install djangorestframework`
* Then, run the following commands in your terminal:
'''
python manage.py makmigrations
python manage.py migrate
python manage.py createsuperuser (follow promps to generate login credentials)
python manage.py runserver
'''
* To navigate to the API type `localhost:8000` in your browser to get to the user interface.

---
# Purpose of the app

> The purpose is to meet all the requirements that are set for this restful API by the product owner. The company had no way to share important company data, but building this API solves that issue. To learn more information about Bangazon and what we're about click [here](http://bangazon.com/).
