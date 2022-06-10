from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('user/',views.user,name='user'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersignup/',views.usersignup,name='usersignup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addbook/',views.addbook,name='addbook'),
        

    path('SignupBackend/',views.SignupBackend,name='SignupBackend'),
    path('LoginBackend/',views.LoginBackend,name='LoginBackend'),
    path('AddBookSubmission/',views.AddBookSubmission,name='AddBookSubmission'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    #path('undobook/<int:id>',views.undobook,name='undobook'),
    path('HandleLogout/',views.HandleLogout,name='HandleLogout'),
    path('Search/',views.Search,name='Search'),
    path('editbookdetails/<int:id>',views.editbookdetails,name='editbookdetails'),
    path('<int:id>/updatedetails/',views.updatedetails,name='updatedetails'),
    
]
