from django.urls import path
from . import views
from datetime import datetime
from django.conf.urls import url
from django.views.generic.base import RedirectView
from articles.models import Article
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

info_articles = {
        'queryset': Article.objects.all(),
        'date_field': 'post_date',
    }

urlpatterns = [
    path('sitemap.xml', sitemap,
            {'sitemaps': {'aricles': GenericSitemap(info_articles, priority=0.6) , }},
            name='django.contrib.sitemaps.views.sitemap'),
    path(''        , views.index   , name='home'),
    path('about/'  , views.about   , name='about'),
    path('contact/', views.contact , name='contact'),
    path('register/', views.RegisterFormView.as_view( extra_context=
             {
                 'title': 'Реєстрація',
                 'year' : datetime.now().year,
             }) , name="register"),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/media/favicon.ico'), name='favicon'),
]