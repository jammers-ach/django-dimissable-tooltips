from django.conf.urls import patterns,url
from . import views


urlpatterns = patterns('',

    url(r'^hide_popup/$',views.hide_popup,name='hide_popup'),
    url(r'^get_popup/$',views.get_popup,name='get_popup'),

)
