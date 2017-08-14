# django imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.http import JsonResponse

# rest framework imports
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

#retor api imports
from retroAPI.serializers import UserSerializer, TeamSerializer, RetroSerializer
from models import Team, Retro

class RetroViewSet(viewsets.ModelViewSet):
    queryset = Retro.objects.all()
    serializer_class = RetroSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('-name')
    serializer_class = TeamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

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
