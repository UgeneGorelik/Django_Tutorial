from django.conf.urls import url,include
# from home.views import home
from . import views

urlpatterns = [
    # url(r'^$', home.as_view(), name='home'),
     url(r'^$', views.HomeView.as_view(),name='home'),
     url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')

]