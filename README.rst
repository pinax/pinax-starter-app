{{ app_name }}
========================

Welcome to the documentation for django-{{ app_name }}!


Running the Tests
------------------------------------

You can run the tests with via::

    django-admin.py test {{ app_name }}


REMOVE BELOW THIS LINE
======================

pinax-starter-app
-----------------

Quickly setup the scaffolding for your django app.

What you get:

* test infrastructure
* Travis configuration with coveralls
* documentation instrastructure
* MIT LICENSE
* setup.py


Getting Started
================

Execute:

    pip install Django
    django-admin.py startapp --template=https://github.com/pinax/pinax-starter-app/zipball/master --extension=py,rst,in,sh <project_name>
