from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^{{ project_name }}admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
        url(r'^admin/', include(admin.site.urls)),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
