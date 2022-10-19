
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signUp,name='home'),
    path('messPage', views.mainApp, name='mainApp'),
    path('login/', views.login, name='login'),
    path('logOut',views.logOut,name='logOut'),
    path('<int:pk>',views.delete_post),
    # path('<str:username>/',views.profile_view),
]