ConsumerAffairs
===============

ConsumerAffairs Backend Practical Test

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Deployment
----------

The following details how to deploy this application.


Instructions on Running the Web Server Locally:

0. $ cd consuemraffairs
1. python3 -m venv ENV
2. $ source ENV/bin/activate
3. $ pip install -r requirements/local.txt
4. $ python manage.py migrate
5. $ python manage.py runserver 0.0.0.0:8000
6. Go to address and create a user account
7. Click "Companies" and add a company (but please do not insert spaces - I'm working on this bug)
8. After success, click "Reviews" and select the company you entered along with data for the other fields. (The no-spaces rule applies again.)
9. Profit!!
