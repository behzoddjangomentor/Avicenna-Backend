from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = i18n_patterns(
    path('i18n/',include('django.conf.urls.i18n') ),

)
urlpatterns +=[
    path('admin/',admin.site.urls),
    path('api/v1/',include('url.urls')),
    path('api/v2/',include('class.urls')),
    path('api/auth/',include('djoser.urls')),
    path('api/auth',include('djoser.urls.authtoken')),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)