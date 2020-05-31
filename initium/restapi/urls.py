from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.apiOverview, name='api-Overview'),
    path('user-list/', views.UserList, name='user_list'),
    path('user-create/', views.UserCreate, name='user_create'),
    path('post-list/', views.PostList, name='post_list'),
    path('post-detail/<str:pk>/', views.PostDetail, name="post_detail"),
    path('post-create/', views.PostCreate, name='post_create'),
    path('post-update/<str:pk>/', views.PostUpdate, name='post_update'),
    path('post-delete/<str:pk>/', views.PostDelete, name='post_delete'),
    path('donation-list/', views.DonationList, name='donation_list'),
    path('donation-detail/<str:pk>/', views.DonationDetail, name="donation_detail"),
    path('donation-create/', views.DonationCreate, name='donation_create'),
    path('donation-update/<str:pk>/', views.DonationUpdate, name='donation_update'),
    path('donation-delete/<str:pk>/', views.DonationDelete, name='donationt_delete'),
]