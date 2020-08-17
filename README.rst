django-admin-shuffle
#####################

.. image:: https://travis-ci.org/ojayyezzir/django-admin-shuffle.svg?branch=develop
    :target: https://travis-ci.org/ojayyezzir/django-admin-shuffle
.. image:: https://codecov.io/gh/ojayyezzir/django-admin-shuffle/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/ojayyezzir/django-admin-shuffle

**django-admin-shuffle** simply shuffles objects on admin changelist view.

This app supports the following combinations of Django and Python:

==========  =======================
  Django      Python
==========  =======================
2.1         3.6, 3.7, 3.8
2.2         3.6, 3.7, 3.8
3.0         3.6, 3.7, 3.8
==========  =======================

.. image:: https://raw.githubusercontent.com/ojayyezzir/django-admin-shuffle/9c8f75c043e185d4f8ee7f7ba50e775dca3b1b5b/example.gif

Installation
=====================

Add "admin_shuffle" to your INSTALLED_APPS setting like this

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'admin_shuffle',
    ]

Integration Example
=====================

Add mixin to your admin model like this

.. code-block:: python

    from admin_shuffle import AdminShuffleMixin

    class ExampleAdmin(AdminShuffleMixin, models.ModelAdmin):
        pass

Settings
=====================
- ``SHUFFLE_QS_VALUE``: Value of query string. By default, it is set to ``'SHUFFLE'``
- ``SHUFFLE_LABEL``: Label of the button that shuffles. By default, it is set to ``'SHUFFLE'``

Development / Example
=======================

1. Run ``python -m django migrate --settings=example.settings`` to migrate.

2. Run ``python -m django runserver --settings=example.settings`` to run server.
