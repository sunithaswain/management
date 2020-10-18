from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^regi/', views.regisin, name='registering'),
    url(r'^log/',views.login, name='logging'),
    url(r'^index',views.indexing, name='indexing1'),
    url(r'^userprofile/(?P<user_id>[\d]+)',views.profiling, name='userprofiles'),
    url(r'^pass_chnge/',views.changingpassword, name='change_pwd'),
    url(r'^contact/', views.content, name='content_details'),
    url(r'^out/',views.logoutin, name='logout'),
    url(r'^email_sending/',views.email, name='email_call'),


    
    
    ]