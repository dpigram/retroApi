# django imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# rest framework imports
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

#retor api imports
from retroAPI.serializers import UserSerializer, TeamSerializer, RetroSerializer, RetroItemSerializer
from models import Team, Retro, RetroItem

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

# teams
class TeamView(generic.ListView):
    template_name = 'retro/dashboard.html'
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

# login
@api_view(['POST'])
def webLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        print("Successfully Logged in")
        request.session['userid'] = user.id
        print("Session modified: " + str(request.session.modified))
        return HttpResponseRedirect(reverse('retro:dashboard'))
    else:
        print("User was not logged in")
        return render(request, 'retro/login.html', {
            'error_message': "Invalid Username and Password"
        })

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
