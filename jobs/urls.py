from django.urls import path
from . import views

urlpatterns=[
    path('',views.start,name='home1'),

    path('firstlog',views.login,name='home'),

    path('signup',views.signup,name='home2'),

    path('signin',views.regsave),

    path('signinagain',views.login,name='home3'),

    path('loginnext',views.loginauth),

    path('logout',views.logout),

    path('first',views.first,name='first'),

    path('pro',views.pro1,name='pro2'),

    path('pro2data',views.pro2data),
    path('jobdel',views.jobdel),

    path('seek1',views.seek1,name='seek1'),
    path('seek2data',views.seek2data),
    path('jobsel',views.jobsel),


    path('viewseekers',views.viewseekers),

    path('features',views.features),
    path('pricing',views.pricing)
]