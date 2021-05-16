"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
   path('',views.videos,name='videos'),
   path('python/',views.python,name='python'),
   path('cpp/',views.cpp,name='cpp'),
   path('django/',views.django,name='django'),
   path('javascript/',views.javascript,name='javascript'),
   path('java/',views.java,name='java'),
   path('nodejs/',views.nodejs,name='nodejs'),
   path('reactjs/',views.reactjs,name='reactjs'),
   path('ruby/',views.ruby,name='ruby'),
]
