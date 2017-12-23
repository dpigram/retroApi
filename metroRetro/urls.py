"""metroRetro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from retroAPI import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'retros', views.RetroViewSet)
router.register(r'retroItems', views.RetroItemsViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'userProfiles', views.UserProfilesViewSet)


urlpatterns = [
    url(r'^retro/', include('retroAPI.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^user/auth', views.loginService),
    url(r'^user/teams/', views.getListOfTeams),
    url(r'^team/retros/', views.getListOfRetros),
    url(r'^create/retro/item/', views.wsCreateNewRetroItem),
    url(r'^create/retro/', views.createNewRetro),
    url(r'^new/team/', views.wsAddNewTeam),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get/all/categories/', views.wsGetAllCategories),
    url(r'^register/', views.wsRegister),
    url(r'^search/users/', views.wsUserSearch),
    url(r'^add/teamMember/', views.wsAddTeamMember),
    url(r'^remove/teamMember/', views.wsRemoveTeamMember),
    url(r'^get/team/details/', views.wsTeamDetails)
]
