=============================
MiBlog
=============================

.. image:: https://badge.fury.io/py/miblog.svg
    :target: https://badge.fury.io/py/miblog

.. image:: https://travis-ci.org/robertweglarek/miblog.svg?branch=master
    :target: https://travis-ci.org/robertweglarek/miblog

.. image:: https://codecov.io/gh/robertweglarek/miblog/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/robertweglarek/miblog

A simple DjangoCMS blog app

Documentation
-------------

The full documentation is at https://miblog.readthedocs.io.

Quickstart
----------

Install MiBlog::

    pip install miblog

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'miblog.apps.MiBlogConfig',
        ...
    )

Add MiBlog's URL patterns:

.. code-block:: python

    from miblog import urls as miblog_urls


    urlpatterns = [
        ...
        url(r'^', include(miblog_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
