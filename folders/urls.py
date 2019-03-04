
from django.conf.urls import include, url
#from django.contrib.auth.views import login
from folders import views


urlpatterns = [

    url(r'^$',views.dirstruc, name='dirstruc'),
  # url(r'^subdirectories/$',views.subfoldes,name='subfoldes'),
    url(r'^ajax/load-sub_directories/', views.subfoldes, name='sub_directories'),
    url(r'^list/', views.display_list, name='display_list'),


  
  ]