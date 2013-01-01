from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app',
    # Examples:
    url(r'^$', 'views.new_bounty', name='new'),
    url(r'^set_category/(?P<id>[0-9]+)$', 'views.set_category', name='set_category'),
) + patterns('django.views.generic.simple',
    url(r'^about', 'direct_to_template', {'template': 'about.html'}, name='about'),
    url(r'^terms', 'direct_to_template', {'template': 'terms.html'}, name='terms'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
