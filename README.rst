Django Admin Shuffle
=======================


What it does
-------------

This package simply shuffles list of objects on admin changelist view.

Integration Example
--------------------

Add "admin_shuffle" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'admin_shuffle',
    ]

And add mixin to your admin model like this

.. code-block:: python

    from admin_shuffle import AdminShuffleMixin

    class ExampleAdmin(AdminShuffleMixin, models.ModelAdmin):
        pass

Settings
---------------------
- ``SHUFFLE_QS_VALUE``: Value of query string. By default, it is set to ``'SHUFFLE'``
- ``SHUFFLE_LABEL``: Label of the button that shuffles. By default, it is set to ``'SHUFFLE'``
