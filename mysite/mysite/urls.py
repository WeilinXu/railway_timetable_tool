"""mysite URL Configuration

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
import os
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns # ADD: translation

# Up two folders to serve "site" content
urlpatterns = i18n_patterns(  # ADD: translation
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('', include('home.urls')),
    path('timetable_tool/', include('timetable_tool.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
)
urlpatterns += [
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
    url(r'^i18n/',include('django.conf.urls.i18n')),]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')
# NOTE: change SITE_ROOT to BASE_DIR
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns += staticfiles_urlpatterns()

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns = i18n_patterns(path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login)),) + urlpatterns
    print('Using',social_login,'as the login template')
except:
    print('Using registration/login.html as the login template')

# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include
