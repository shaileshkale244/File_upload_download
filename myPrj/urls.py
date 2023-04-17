from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from fileUpload import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('showlist/', views.showlist, name='showlist'),
    path('login/', views.login, name='login'),
    path('open/<file_name>', views.open, name='open'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
