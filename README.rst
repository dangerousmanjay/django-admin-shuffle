# django-admin-shuffle


What it does
-----------

This package simply shuffles list of objects on admin changelist view.


Quick start
-----------

Add "cxm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'admin_shuffle',
    ]


Settings
---------------------
- ``SHUFFLE_QS_VALUE``: Value of query string. By default, it is set to ``'SHUFFLE'``
- ``SHUFFLE_LABEL``: Label of the button that shuffles. By default, it is set to ``'SHUFFLE'``
