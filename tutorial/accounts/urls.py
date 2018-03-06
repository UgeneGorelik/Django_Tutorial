from django.conf.urls import url,include


from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)


urlpatterns = [

    # url(r'^$',views.home,name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register,  name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='profile_pk'),
    url(r'^profile/edit',views.edit_profile,name='editprofile'),
    url(r'^change-password',views.change_password,name='change_password'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
]
