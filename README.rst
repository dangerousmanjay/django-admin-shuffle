django-admin-shuffle
#####################

**django-admin-shuffle** simply shuffles objects on admin changelist view.

Supports `Django`_ 2.1+ and 3.0+.

![](example.gif)

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
