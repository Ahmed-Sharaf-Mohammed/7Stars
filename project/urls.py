from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [

    path("i18n/", include("django.conf.urls.i18n")), #https://docs.djangoproject.com/en/4.2/topics/i18n/translation/#django.views.i18n.set_language ,
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('registration/', include('registration.urls', namespace='registration')),
    # هنا انا استخدمت كل ال methods الداخلية فى ال django
    # الجاهزة اللى موجودة فى ال registration
    # اللى هى كتبناها فى فايل txt

    path("accounts/", include("django.contrib.auth.urls")),
    # عشان اوصل لمكان ال template
    # واعرف اساميهم امشى على نفس المسار اللى مكتوب
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
