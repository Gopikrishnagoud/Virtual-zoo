from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    #path("zoo/",include("zoo.urls"))
    path('',views.page,name='main_page'),
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    # path('login/',views.Login,name='login'),
    path('direction/',views.Direct,name='direct'),
    path('wild/', views.page1, name='page1'),
    path('mammals/',views.mammals,name='mammals'),
    path('deers/',views.deers,name='deers'),
    path('snakes/',views.snakes,name='snakes'),
    path('crocodiles',views.crocodiles,name='crocodile'),
    path('turtules/',views.turtules,name='turtules'),
    path('birds/',views.birds,name='birds'),
    path('aquatic animals/',views.aquatic,name='aquatic'),
    path('mammalias/',views.mammalia,name='mammalia'),
    path('bears/',views.bears,name='bears'),
    path('lizards/',views.lizards,name='lizards'),
    path('Extinct_Animals/',views.Extinct_Animals,name='Extinct_Animals'),
    path('mammalias/',views.mammalias,name='mammalias'),
    path('hybrid/',views.hybrid,name='hybrid'),
    path('horse/',views.horse,name='horse'),
    path('logout/',views.logout,name='logout'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)