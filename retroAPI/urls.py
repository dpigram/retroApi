from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'retro'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="retro/login.html"))
]
