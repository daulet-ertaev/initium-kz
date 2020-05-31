from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from post.models import Post, Donation
from .serializers import *
from .forms import CreateUserForm
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    """
    API endpoint that allows groups to be viewed or edited.

    """
    api_urls = {
        'UserList': '/user-list/',
        'UserDetail': '/user-detail/<str:pk>/',
        'UserCreate': '/user-create/',
        'UserUpdate': '/user-update/<str:pk>/',
        'UserDelete': '/user-delete/<str:pk>/',
        'PostList': '/post-list/',
        'PostDetail': '/post-detail/<str:pk>/',
        'PostCreate': '/post-create/',
        'PostUpdate': '/post-update/<str:pk>/',
        'PostDelete': '/post-delete/<str:pk>/',
        'DonationList': '/donation-list/',
        'DonationDetail': '/donation-detail/<str:pk>/',
        'DonationCreate': '/donation-create/',
        'DonationUpdate': '/donation-update/<str:pk>/',
        'DonationDelete': '/donation-delete/<str:pk>/',
    }
    return Response(api_urls)
    # queryset = Customer.objects.all()
    # serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])          ######################################################
def UserList(request):
    users = User.objects.all()

    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    form = CreateUserForm(request.data)
    print(request.data)
    if serializer.is_valid():
        form.save()
    return Response(serializer.data)

@api_view(['GET'])          ######################################################
def PostList(request):
    orders = Post.objects.all()
    serializer = PostSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PostDetail(request,pk):
    orders = Post.objects.get(id=pk)
    serializer = PostSerializer(orders,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def PostCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def PostUpdate(request,pk):
    orders = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=orders,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def PostDelete(request,pk):
    orders = Post.objects.get(id=pk)
    orders.delete()

    return Response("Item is deleted successfully!")

@api_view(['GET'])          ######################################################
def DonationList(request):
    orders = Donation.objects.all()
    serializer = DonationSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DonationDetail(request,pk):
    orders = Donation.objects.get(id=pk)
    serializer = DonationSerializer(orders,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def DonationCreate(request):
    serializer = DonationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def DonationUpdate(request,pk):
    orders = Donation.objects.get(id=pk)
    serializer = DonationSerializer(instance=orders,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DonationDelete(request,pk):
    orders = Donation.objects.get(id=pk)
    orders.delete()

    return Response("Item is deleted successfully!")
