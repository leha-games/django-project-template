from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'', include('{{ project_name }}.base.urls')),
    (r'^{{ project_name }}admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1],
                'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
            (r'^404/$', 'django.views.defaults.page_not_found'),
            (r'^500/$', 'django.views.defaults.server_error'),
            (r'^admin/', include(admin.site.urls)),
    )