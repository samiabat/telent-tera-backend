from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.home, name = 'home'),
    path('authorize/', views.authorize, name = 'profile'),
    path('proposals/', views.proposalApi, name = "proposals"),
    path('proposals/<str:pk>/', views.proposalApi, name = "proposals"),
    path('proposals/<str:job>/', views.getProposalByJob),
    path('customers/<str:username>/', views.getUserByusername),
    path('jobs/', views.jobApi, name = "jobs"),
    path('jobs/<str:pk>/', views.jobApi, name = "jobs"),
    path('user/', views.userApi),
    path('reviews/<str:pk>/', views.getReview),
    path('reports/<str:pk>/', views.getReport),
    path('reviews/', views.review),
    path('reports/', views.report, name = "reports"),
    path('report/<str:id>/', views.reporting, name = "reporting"),
    # path('messages/', views.message),
    path('messages/', views.getMessage),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]