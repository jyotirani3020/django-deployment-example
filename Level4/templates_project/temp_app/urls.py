from django.conf.urls import url
from temp_app import views

#for template tagging
app_name = 'temp_app'


urlpatterns = [
    url(r'^relative/$', views.relative, name = 'relative'),
    url(r'other/$', views.other, name = 'other'),
    ]


