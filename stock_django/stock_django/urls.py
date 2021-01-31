"""stock_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from stock_django.view import page_not_found, page_error
from . import view

urlpatterns = [
    url(r'^$', view.index),
    url(r'^core$', view.core),
    url(r'^info/.*', view.info),
    url(r'^prophetparam', view.add_prophetparam),
    url(r'^setprophetparam', view.set_prophetparam),
    url(r'^xgbparam', view.add_xgbparam),
    url(r'^setxgbparam', view.set_xgbparam),
    url(r'^lstmparam', view.add_lstmparam),
    url(r'^setlstmparam', view.set_lstmparam),
    url(r'^update', view.update),
    url(r'^mark/.*', view.mark),
    url(r'^pe/.*', view.pe),
    url(r'^pb/.*', view.pb),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
]

handler404 = 'stock_django.view.page_not_found'
handler500 = 'stock_django.view.page_error'