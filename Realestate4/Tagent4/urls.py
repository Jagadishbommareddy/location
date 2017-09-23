from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AgentList.as_view(), name='agent-list'),


    url(r'agent/add/$', views.AgentAddrLocArefCreate.as_view(), name='agent-add'),
    url(r'agent/(?P<pk>[0-9]+)/$', views.AgentAddrLocArefUpdate.as_view(), name='agent-update'),
    url(r'agent/(?P<pk>[0-9]+)/delete/$', views.AgentDelete.as_view(), name='agent-delete'),

]