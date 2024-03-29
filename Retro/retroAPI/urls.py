from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'retro'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="retro/login.html"), name="loginScreen"),
    url(r'^dashboard/$', views.DashboardDetilaView.as_view() ,name="dashboard"),
    url(r'^dashboard/team/(?P<pk>[0-9]+)/details/$', views.TeamView.as_view(), name="teamDetails"),
    url(r'^dashboard/team/(?P<pk>[0-9]+)/new/retro/$', views.NewRetroView.as_view(), name="NewRetro"),
    url(r'^dashboard/retro/(?P<pk>[0-9]+)/new/item/$', views.NewRetroItemView.as_view(), name="newRetroItem"),
    url(r'^dashboard/team/retro/(?P<pk>[0-9]+)/details/$', views.RetroDetailView.as_view(), name="retroDetails"),
    url(r'^dashboard/new/team/$', views.NewTeamView.as_view(), name="newTeam"),
    url(r'^authenticate/$', views.webLogin, name='login'),
    url(r'^base/$', views.BaseView.as_view(), name="base"),
    url(r'^logout/$', views.webLogout, name='logout'),
    url(r'^addTeam/$', views.addNewTeam, name='addNewTeam'),
    url(r'^manageTeam/(?P<pk>[0-9]+)/$', views.ManageTeamView.as_view(), name='ManageTeam'),
    url(r'^deleteTeam/$', views.deleteTeam, name='deleteTeam'),
    url(r'^addRetro/$', views.addNewRetro, name='addRetro'),
    url(r'^deleteRetro/$', views.deleteRetro, name='deleteRetro'),
    url(r'^addRetroItem/$', views.addNewRetroItem, name='addNewRetroItem'),
    url(r'^deleteRetroItem/$', views.deleteRetroItem, name='deleteRetroItem'),
    url(r'^edit/retroItem/(?P<pk>[0-9]+)/$', views.EditRetroItemView.as_view(), name='editRetroItem'),
    url(r'^save/retroItem/$', views.editRetroItem, name='editRetroItem'),
    url(r'^getData/$', views.getData, name='getData')
    
]
