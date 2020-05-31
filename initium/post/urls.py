from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('charge/', views.charge, name='charge'),
    path('donationPage/', views.donationPage, name='donationPage'),
    path('success/<str:args>/', views.success, name='success'),
    path('paypalDonation/<int:args>/<int:pk>/<int:pid>', views.paypal, name='paypal'),
    path('posts/', views.posts, name='posts'),
    path('posts/<str:args>/',views.showPost, name='showPost'),
    path('paypalCharge/<int:pk>/<int:pid>', views.paypalCharge, name='paypalCharge'),
    path('paypalAmount/<int:pk>/<int:pid>/', views.paypalAmount, name='paypalAmount'),
    path('test/', views.test, name='test'),
    path('history/<int:pk>', views.history, name='history')
]

# <app>/<model>_<viewtype>.html