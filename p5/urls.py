from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('life/', include('life.urls')),
#   path('login/', auth_views.login, name='login'),
#   path('logout/', auth_views.logout, name='logout')
#   path(r'^accounts/login/$', views.login, name='login'),
#     url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
