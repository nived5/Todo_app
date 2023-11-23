from django.urls import path

from newapp2 import views
# from newapp2 import views
from study5 import urls

urlpatterns=[
    # path('',views.newstudy,name = 'newstudy'),
    path('',views.home,name = 'home'),
    path('page2',views.dashboard,name = 'dashboard'),
    path('page3',views.create,name = 'page3'),
    path('page4',views.read,name ='page4'),
    path('delt/<int:id>/',views.delt,name='delt'),

    path('update/<int:id>/',views.update,name='update')
]