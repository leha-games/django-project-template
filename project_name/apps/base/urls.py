from django.conf.urls import url, patterns
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="base/home.html"), name='home'),
)
