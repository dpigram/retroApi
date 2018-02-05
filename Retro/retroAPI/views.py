# django imports
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

# rest framework imports
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#retor api imports
from retroAPI.serializers import UserSerializer, TeamSerializer, RetroSerializer, RetroItemSerializer, CategorySerializer, OrganizationSerializer, UserProfileSerializer
from models import Team, Retro, RetroItem, Category, Organization, UserProfile

class UserProfilesViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

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
            context['all_categories'] = Category.objects.all().order_by('-name')
        return context

# teams
class TeamView(generic.ListView):
    template_name = 'retro/teamDetails.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
         # Get the user
        user  = User.objects.get(id=self.request.session['userid'])
        # Get the user's profile
        profile = UserProfile.objects.get(user=user)
        teams = Team.objects.filter(organization=profile.organization)
        return teams

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['team_details'] = Team.objects.get(pk=self.kwargs['pk'])
            context['team_retros'] = Retro.objects.filter(team=self.kwargs['pk']).order_by('-created_date')
        return context;

class BaseView(generic.ListView):
    template_name = 'retro/baseNavigation.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        """ Return all teams """
        user  = User.objects.get(id=self.request.session['userid'])
        # Get the user's profile
        profile = UserProfile.objects.get(user=user)
        teams = Team.objects.filter(organization=profile.organization)
        return teams

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
        user  = User.objects.get(id=self.request.session['userid'])
        # Get the user's profile
        profile = UserProfile.objects.get(user=user)
        teams = Team.objects.filter(organization=profile.organization)
        return teams

    def get_context_data(self, **kwargs):
        context = super(NewRetroView, self).get_context_data(**kwargs)
        if bool(self.kwargs):
            context['team_details'] = Team.objects.get(pk=self.kwargs['pk'])
        return context

class NewTeamView(generic.ListView):
    template_name = 'retro/newTeam.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        user  = User.objects.get(id=self.request.session['userid'])
        # Get the user's profile
        profile = UserProfile.objects.get(user=user)
        teams = Team.objects.filter(organization=profile.organization)
        return teams

class DashboardDetilaView(generic.ListView):
    template_name = 'retro/dashboard.html'
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        user  = User.objects.get(id=self.request.session['userid'])
        # Get the user's profile
        profile = UserProfile.objects.get(user=user)
        teams = Team.objects.filter(organization=profile.organization)
        return teams

class RetroDetailView(generic.ListView):
    template_name = "retro/retroDetails.html"
    context_object_name = 'all_teams_list'

    def get_queryset(self):
        user  = User.objects.get(id=self.request.session['userid'])
        # Get the user's profile
        profile = UserProfile.objects.get(user=user)
        teams = Team.objects.filter(organization=profile.organization)
        return teams

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
    return HttpResponseRedirect(reverse('retro:retroDetails', args=(item.retro.id,)))

def deleteRetroItem(request):
    RetroItem.objects.get(pk=request.POST['retroItemId']).delete()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def addNewRetroItem(request):
    retro = Retro.objects.get(pk=request.POST['retroId'])
    item = RetroItem(title=request.POST['title'], retro=retro)
    item.category = Category.objects.get(pk=request.POST['category'])
    item.save()
    return HttpResponseRedirect(reverse('retro:retroDetails', args=(retro.id,)))

def addNewRetro(request):
    # Get all retros where current == True and set to False
    currentRetros = Retro.objects.filter(current=True, team=request.POST['teamId'])
    currentRetros.update(current=False);

    # Creat and set the current retro to True
    team = Team.objects.get(pk=request.POST['teamId'])
    newRetro = Retro(title=request.POST['title'], team=team, current=True)
    newRetro.save()
    return HttpResponseRedirect(reverse('retro:teamDetails', args=(team.id,)))

def deleteRetro(request):
    Retro.objects.get(pk=request.POST['retroId']).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def deleteTeam(request):
    Team.objects.get(pk=request.POST['teamId']).delete()
    return HttpResponseRedirect(reverse('retro:dashboard'))

def addNewTeam(request):
    user = User.objects.get(pk=request.session['userid'])
    profile = UserProfile.objects.get(user=user);
    newTeam = Team(name=request.POST['teamName'], description=request.POST['teamDescription'], owner=user, organization=profile.organization)
    newTeam.save()
    newTeam.members.add(request.session['userid'])
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
    
    user  = User.objects.get(id=request.POST['userId'])
    # Get the user's profile
    profile = UserProfile.objects.get(user=user)
    print(profile.organization)
    teams = Team.objects.filter(organization=profile.organization)
    serializer = TeamSerializer(teams, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def getListOfRetros(request):
    print(request.POST)
    retros = Retro.objects.filter(team=request.POST['teamId'])
    serializer = RetroSerializer(retros, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createNewRetro(request):
    team = Team.objects.get(pk=request.POST['teamId'])
    newRetro = Retro(title=request.POST['title'], team=team)
    newRetro.save()
    return JsonResponse({'status': 'success'})

@api_view(['POST'])
def wsDeleteRetro(request):
    Retro.objects.get(pk=request.POST['retroId']).delete()
    return JsonResponse({'status': 'success'})

@api_view(['POST'])
def wsAddNewTeam(request):
    user = User.objects.get(pk=request.session['userid'])
    newTeam = Team(name=request.POST['teamName'], description=request.POST['teamDescription'], owner=user)
    newTeam.save()
    return JsonResponse({'status':'success'})

@api_view(['POST'])
def wsCreateNewRetroItem(request):
    retro = Retro.objects.get(pk=request.POST['retroId'])
    item = RetroItem(title=request.POST['title'], retro=retro)
    item.category = Category.objects.get(pk=request.POST['category'])
    item.save()
    return JsonResponse({'status':'success'})

@api_view(['GET'])
def wsGetAllCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def wsRegister(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        org = Organization(name=request.POST['company_name'])
        org.save()
        print("user data")
        print(serialized.data['username'])

        user = User.objects.get(username=serialized.data['username'])
        print(user)
        profile = UserProfile(user=user, organization=org)
        profile.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        print("bad request")
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def wsUserSearch(request):
    team = Team.objects.get(pk=request.GET['teamId'])
    members = team.members.all()
    users = User.objects.filter(first_name__icontains=request.GET['member_search']).exclude(id__in=members)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def wsAddTeamMember(request):
    print(request.POST)
    team = Team.objects.get(pk=request.POST["teamId"])
    team.members.add(request.POST["userId"])
    user = User.objects.get(pk=request.POST["userId"])
    # send_mail("Team Access", "You have been added to " + team.name, "terell.pigram@gmail.com", [user.email], fail_silently=False)
    return JsonResponse({'status': 'success'})

@api_view(['POST'])
def wsRemoveTeamMember(request):
    team = Team.objects.get(pk=request.POST["teamId"])
    team.members.remove(request.POST["userId"])
    return JsonResponse({'status':'success'})

@api_view(['POST'])
def wsTeamDetails(request):
    team = Team.objects.get(pk=request.POST["teamId"])
    serializer = TeamSerializer(team)
    return Response(serializer.data)


