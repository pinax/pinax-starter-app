pinax-starter-app
=================


Quickly setup the scaffolding for your django app.

What you get:

* test infrastructure
* Travis configuration with coveralls
* documentation instrastructure
* MIT LICENSE
* setup.py


Getting Started
================

Execute::

    pip install Django
    django-admin.py startapp --template=https://github.com/pinax/pinax-starter-app/zipball/master --extension=py,rst,in,sh,rc <project_name>


After you are running you have a fresh app, first update this readme by removing
everything above and including this line and unindenting everything below this line. Also
remember to edit the {{{<user_or_org_name>}}} in the travis and coveralls badge/links::

    {{ app_name }}
    ========================
    
    .. image:: https://travis-ci.org/<user_or_org_name>/django-{{ app_name }}.png
        :target: https://travis-ci.org/<user_or_org_name>/django-{{ app_name }}
    
    .. image:: https://coveralls.io/repos/<user_or_org_name>/django-{{ app_name }}/badge.png
        :target: https://coveralls.io/r/<user_or_org_name>/django-{{ app_name }}
    
    .. image:: https://pypip.in/d/django-{{ app_name }}/badge.png
        :target:  https://pypi.python.org/pypi/django-{{ app_name }}/
    
    .. image:: https://pypip.in/v/django-{{ app_name }}/badge.png
        :target:  https://pypi.python.org/pypi/django-{{ app_name }}/
    
    .. image:: https://pypip.in/license/django-{{ app_name }}/badge.png
        :target:  https://pypi.python.org/pypi/django-{{ app_name }}/
    
    
    Welcome to the documentation for django-{{ app_name }}!
    
    
    Running the Tests
    ------------------------------------
    
    You can run the tests with via::
    
        python setup.py test
    
    or::
    
        make test
    
    or::
    
        make all
    
    or::
    
        python runtests.py

