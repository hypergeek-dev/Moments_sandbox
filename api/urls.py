from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from .views import logout_route

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/logout/', logout_route),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include('profiles.urls')),
    path('api/', include('meetings.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')