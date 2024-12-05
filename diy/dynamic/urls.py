from django.urls import path
from . import views

urlpatterns = [
    path('project_list/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('chat/',views.bot,name="bot"),
    path('',views.home,name="home"),
    path('About-us/',views.aboutus,name="About-us")
]
