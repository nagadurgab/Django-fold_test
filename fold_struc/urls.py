



from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView


urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^folders/',include('folders.urls')),
    ]
   
