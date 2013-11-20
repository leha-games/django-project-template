from django.conf.urls import url, patterns


urlpatterns = patterns('{{ project_name}}.apps.base.views',
    url(r'^$', 'home', name='home'),
)
