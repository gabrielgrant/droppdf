"""ChartApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from upload import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^drop/', views.drop, name="drop"),
    url(r'^pdf/(?P<filename>.+\.pdf)/$', views.pdf, name="pdf"),
    url(r'^ocr/', views.ocr, name="ocr"),
		url(r'^csv/(?P<filename>.+)/$', views.csvAsTable, name="csv")
