from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('qna.urls')),
    path('users/',include('users.urls')),
    path('users/login',LoginView.as_view(),name='login'),
    path('users/logout',LogoutView.as_view(),name='logout'),
]


