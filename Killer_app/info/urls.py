
from django.urls import path
from . import views

#https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
#https://learndjango.com/tutorials/django-sitemap-tutorial
#xml file rendered is quiet wierd 
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from . import sitemaps
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('', views.player_contact_form, name='info-form'),
    path('success/', views.success, name='success'),
    path('select_game_mode/', views.select_game_mode, name='select_game_mode'),
    path('rules/', views.rules, name='rules'),
    path('donate/', views.donate, name='donate'),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

handler404 = 'info.views.handler404'
handler500 = 'info.views.handler500'