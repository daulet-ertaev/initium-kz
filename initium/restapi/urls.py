from django.urls import path,include
from . import views

urlpatterns = [
    path('api/',views.apiOverview, name='api-Overview'),
    path('api/user-list/', views.UserList, name='user_list'),
    path('api/user-create/', views.UserCreate, name='user_create'),
    path('api/post-list/', views.PostList, name='post_list'),
    path('api/post-detail/<str:pk>/', views.PostDetail, name="post_detail"),
    path('api/post-create/', views.PostCreate, name='post_create'),
    path('api/post-update/<str:pk>/', views.PostUpdate, name='post_update'),
    path('api/post-delete/<str:pk>/', views.PostDelete, name='post_delete'),
    path('api/donation-list/', views.DonationList, name='donation_list'),
    path('api/donation-detail/<str:pk>/', views.DonationDetail, name="donation_detail"),
    path('api/donation-create/', views.DonationCreate, name='donation_create'),
    path('api/donation-update/<str:pk>/', views.DonationUpdate, name='donation_update'),
    path('api/donation-delete/<str:pk>/', views.DonationDelete, name='donationt_delete'),
]