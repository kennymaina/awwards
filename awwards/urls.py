from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
       url('^$',views.home,name = 'home'),
       url(r'^search/', views.search_results, name='search_results'),
       url(r'^profile/', views.profile, name='profile'),
       url(r'^project/', views.project, name='project'),
       url(r'^upload/', views.upload_project, name='upload'),
       url(r'^accounts/update/', views.edit, name='update_profile'),
     

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)