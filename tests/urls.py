# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from miblog.urls import urlpatterns as miblog_urls

urlpatterns = [
    url(r'^', include(miblog_urls, namespace='miblog')),
]
