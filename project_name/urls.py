from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.views import defaults as default_views
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

admin.site.site_header = '{{ project_name }} administration'

sitemaps = {

}

urlpatterns = [
    path('/', TemplateView.as_view(template_name='home.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps, }, name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception("Permissin Denied")}),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        path('500/', default_views.server_error),
        path('admin/', admin.site.urls),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('{{ project_name }}admin/', admin.site.urls),
    ]

