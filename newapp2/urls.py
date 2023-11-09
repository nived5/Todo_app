from django.urls import path

from newapp2 import views
# from newapp2 import views
from study5 import urls

urlpatterns=[
    path('',views.newstudy,name = 'newstudy'),
    path('page1',views.home,name = 'home'),
    path('page2',views.dashboard,name = 'dashboard'),
    path('page3',views.create,name = 'create')
]