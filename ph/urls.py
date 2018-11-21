"""ph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from .views import home_page, login_page, buy_page, Logout
from cart.views import cart_home, cart_update
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^login/$', login_page,name='login'),
    url(r'^buy/$', buy_page,name='buy'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^cart/$', cart_home, name='cart'),
    url(r'^update/$', cart_update, name='update'),
    #url(r'^logout/$', LogoutView.as_view(), name='logout', {'next_page': '/login'}),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
