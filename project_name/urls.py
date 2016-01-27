from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.views.defaults import page_not_found, server_error
from django.contrib import admin

admin.site.site_header = u'Django administration'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^{{ project_name }}admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^404/$', page_not_found),
        url(r'^500/$', server_error),
        url(r'^admin/', include(admin.site.urls)),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)