from django.conf.urls import url
from django.urls import path
from bank import views 
 
urlpatterns = [ 
    url(r'^api/bank/$', views.tutorial_list),
    path('api/bank/<str:branch>', views.tutorial_detail),
    #url(r'^api/bank/(?P<branch>[A-Za-z])/$', views.tutorial_detail),
    url(r'^api/bank/published$', views.tutorial_list_published)
]