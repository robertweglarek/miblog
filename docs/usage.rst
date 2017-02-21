=====
Usage
=====

To use MiBlog in a project, add it to your `INSTALLED_APPS`:

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
