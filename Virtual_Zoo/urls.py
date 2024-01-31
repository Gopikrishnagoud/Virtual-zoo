from django.contrib import admin
from django.urls import path,include
from zoo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("zoo.urls")),
    # path('',views.Register,name="register"),
    # # path('direction/',views.Directions,name="direct"),
]
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('', include('z.urls')),
#     path('admin/', admin.site.urls),
# ]