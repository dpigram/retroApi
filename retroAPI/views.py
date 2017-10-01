# django imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

# rest framework imports
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

#retor api imports
from retroAPI.serializers import UserSerializer, TeamSerializer, RetroSerializer, RetroItemSerializer, CategorySerializer
from models import Team, Retro, RetroItem, Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetroItemsViewSet(viewsets.ModelViewSet):
    queryset = RetroItem.objects.all()
    serializer_class = RetroItemSerializer

class RetroViewSet(viewsets.ModelViewSet):
    queryset = Retro.objects.all()
    serializer_class = RetroSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('-name')
    serializer_class = TeamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# website views
class EditRetroItemView(generic.ListView):
    template_name = 'retro/editRetroItem.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Retrun all Teams """
        return Team.objects.filter(owner=self.request.session['userid'])

    def get_context_data(self, **kwargs):
        context = super(EditRetroItemView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['item_details'] = RetroItem.objects.get(pk=self.kwargs['pk'])
            context['all_categories'] = Category.objects.all().order_by('-name')
        return context


class ManageTeamView(generic.ListView):
    template_name = 'retro/manageTeam.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Retrun all Teams """
        teams = Team.objects.filter(owner=self.request.session['userid'])
        print(teams)
        return teams

    def get_context_data(self, **kwargs):
        context = super(ManageTeamView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['team_details'] = Team.objects.get(pk=self.kwargs['pk'])
        return context;


class NewRetroItemView(generic.ListView):
    template_name = 'retro/newRetroItem.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        return Team.objects.filter(owner=self.request.session['userid'])

    def get_context_data(self, **kwargs):
        context = super(NewRetroItemView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['retro_details'] = Retro.objects.get(pk=self.kwargs['pk'])
            return context

# teams
class TeamView(generic.ListView):
    template_name = 'retro/teamDetails.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Return all teams """
        print("userId: " + str(self.request.session['userid']));
        return Team.objects.filter(owner=self.request.session['userid'])

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['team_details'] = Team.objects.get(pk=self.kwargs['pk'])
            context['team_retros'] = Retro.objects.filter(team=self.kwargs['pk'])
        print(self.kwargs)
        return context;

class BaseView(generic.ListView):
    template_name = 'retro/baseNavigation.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Return all teams """
        print("userId: " + str(self.request.session['userid']));
        return Team.objects.filter(owner=self.request.session['userid'])

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['team_details'] = Team.objects.get(pk=self.kwargs['pk'])
            context['team_retros'] = Retro.objects.filter(team=self.kwargs['pk'])
        return context

class NewRetroView(generic.ListView):
    template_name = 'retro/newRetro.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Return all teams """
        return Team.objects.filter(owner=self.request.session['userid'])

    def get_context_data(self, **kwargs):
        context = super(NewRetroView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['team_details'] = Team.objects.get(pk=self.kwargs['pk'])
        return context

class NewTeamView(generic.ListView):
    template_name = 'retro/newTeam.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Return all teams """
        return Team.objects.filter(owner=self.request.session['userid'])

class DashboardDetilaView(generic.ListView):
    template_name = 'retro/dashboard.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        return Team.objects.filter(owner=self.request.session['userid'])

class RetroDetailView(generic.ListView):
    template_name = "retro/retroDetails.html"
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Return all teams """
        return Team.objects.filter(owner=self.request.session['userid'])

    def get_context_data(self, **kwargs):
        context = super(RetroDetailView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['retro_details'] = Retro.objects.get(pk=self.kwargs['pk'])
            context['retro_items'] = RetroItem.objects.filter(retro=self.kwargs['pk'])
        return context

def getData():
    if request.is_ajax():
        return HttpResponse('OK')

def editRetroItem(request):
    item = RetroItem.objects.get(pk=request.POST['itemId'])
    item.title = request.POST['title']
    item.category = Category.objects.get(pk=request.POST['category'])
    item.save()

    return HttpResponseRedirect(request.POST.get('next', '/'))

def deleteRetroItem(request):
    RetroItem.objects.get(pk=request.POST['retroItemId']).delete()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def addNewRetroItem(request):
    retro = Retro.objects.get(pk=request.POST['retroId'])
    item = RetroItem(title=request.POST['title'], retro=retro)
    item.save()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def addNewRetro(request):
    team = Team.objects.get(pk=request.POST['teamId'])
    newRetro = Retro(title=request.POST['title'], team=team)
    newRetro.save()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def deleteRetro(request):
    Retro.objects.get(pk=request.POST['retroId']).delete()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def deleteTeam(request):
    Team.objects.get(pk=request.POST['teamId']).delete()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def addNewTeam(request):
    user = User.objects.get(pk=request.session['userid'])
    newTeam = Team(name=request.POST['teamName'], description=request.POST['teamDescription'], owner=user)
    newTeam.save()
    return HttpResponseRedirect(reverse('retro:dashboard'))

# login
@api_view(['POST'])
def webLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("Successfully Logged in")
        request.session['userid'] = user.id
        print("Session modified: " + str(request.session.modified))
        return HttpResponseRedirect(reverse('retro:dashboard'))
    else:
        print("User was not logged in")
        return render(request, 'retro/login.html', {
            'error_message': "Invalid Username and Password"
        })

#logout
def webLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('retro:loginScreen'))

@api_view(['POST'])
def loginService(request):
    print request.POST
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    serializer_context = {
		'request': request,
	}
    data = UserSerializer(instance=user, context=serializer_context)
    if user is not None:
        if user.is_active:
            return Response({'status': 'success', 'data': data.data})
        else:
            return Response({'status' : 'failure', 'message' : 'This account has been disabled'})
    else:
        # the authentication system was unable to verify the username and password
        return JsonResponse({'status': 'failure', 'message': 'The username and password were incorrect'})

@api_view(['POST'])
def getListOfTeams(request):
    teams = Team.objects.filter(owner=request.POST['userId'])
    serializer = TeamSerializer(teams, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def getListOfRetros(request):
    print(request.POST)
    retros = Retro.objects.filter(team=request.POST['teamId'])
    serializer = RetroSerializer(retros, many=True)
    return Response(serializer.data)
