from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.decorators import *
from .models import *
from django.http import HttpResponse
from .id_generator import get_id
from django.contrib.auth import authenticate, login, logout
import datetime as date 
# Create your views here
@api_view(['POST','GET'])
def user_create(request):
    try :
        name = request.POST.__getitem__('name')
        username = request.POST.__getitem__('username')
        password = request.POST.__getitem__('password')
        email = request.POST.__getitem__('email')
        user_id = get_id()
        dob = request.POST.__getitem__('dob')
        user_log.objects.create_user(email = email,password = password,username = username)
        user_log.save
        Person.objects.create(fname = name , user_id = user_id, email = email, dob = dob)
        Person.save
        
        context = { 
            "message": "User Registered Successfully",
            "user_id" : user_id,
        
        }
        return Response(context)
    
    except Exception as e:
        print(e)
        print(str(e).split())
        if "UNIQUE" in str(e).split():
            context = { "message": "Credentials Used"
        
            }
        else:
            context = {
                "message" : "Unknown error occured"
            }
        return Response(context)

@api_view(['POST','GET'])
def auth(request):
    print(request.user.is_authenticated)
    try:
        username = request.POST.__getitem__('username')
        password = request.POST.__getitem__('password')
        user = authenticate(request, username = username, password = password)
        print(user)
        print(username)
        print(password)
        if user is not None: 
            context = {
                'status' : 'user authenticated successfully'
            }
            return Response(context)

        else:
            context  = {
                'status' : 'Check Credentials'
            }
            return Response(context)
    except Exception as e :
        print(e)
        return HttpResponse(e)

@api_view(['GET'])
def deauth(request):
    if request.user.is_authenticated:
        w = logout(request)
        print(w)
        if w:
            context = {
                'status': 'user logged out successfully',
            }
            return Response(context)

        else:
            context = {
                'status' : 'Some error occured',
            }
            return Response(context)
    else:
        context = {
            'status' : 'user is not logged in',
        }
        return Response(context)


def index(request):
    context = {

    }
    return render(request,'index.html',context)

def try_reg(request):
    context = {

    }
    return render(request, 'TryReg.html', context)

def try_auth(request):
    context = {

    }
    return render(request,'TryAuth.html',context)
