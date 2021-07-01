from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="home"),
    path('register/',views.register,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('add/',views.addProjects,name='addProjects'),
    path("myProjects",views.myProjects,name='myProjects'),
    path("user/<str:pk>",views.viewProjects,name='viewProjects'),
    path("project/<int:pid>",views.onlyProject,name='onlyProject'),
    path("delete/<int:pid>",views.delProjects,name='delProjects')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
