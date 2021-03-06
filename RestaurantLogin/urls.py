from django.urls import path #Include path function
from . import views # import views file within the same folder (from .)

# RESTful
#Starts with restaurantlogin/
urlpatterns = [
    path('',views.index), # render login form
    path('register',views.register), # render registration form
    path('login',views.login), # process login request
    path('logout',views.logout), # process logout request
    path('create',views.create), # process registration request
    path('editroute',views.editroute), # route from navbar to edit form
    path('edit/<int:restaurantID>',views.edit), # render edit account form
    path('update/<int:restaurantID>',views.update), # process registration request
    path('ajax-regval',views.testunique), # ajax reg validation
    path('ajax-logval',views.testlogin), # ajax login validation
    path('welcome',views.welcome), # render welcome page for valid id
    path('ajax-editval',views.testlogin), # ajax edit validation
    path('logout',views.logout), # flush session
]