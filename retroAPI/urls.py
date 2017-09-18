from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'retro'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="retro/login.html"), name="loginScreen"),
    url(r'^dashboard/$', views.TeamView.as_view(),name="dashboard"),
    url(r'^dashboard/team/(?P<pk>[0-9]+)/details/$', views.TeamView.as_view(), name="teamDetails"),
    url(r'^dashboard/team/(?P<pk>[0-9]+)/new/retro/$', views.NewRetroView.as_view(), name="NewRetro"),
    url(r'^dashboard/new/team/$', TemplateView.as_view(template_name="retro/newTeam.html"), name="newTeam"),
    url(r'^authenticate/$', views.webLogin, name='login'),
    url(r'^base/$', views.BaseView.as_view(), name="base"),
    url(r'^logout/$', views.webLogout, name='logout')
]
