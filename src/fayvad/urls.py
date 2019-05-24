from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import transport.urls
import common.urls
import driving.urls
import rent.urls
from . import views
#from cruds.urls import crud_for_app

admin.site.site_title = 'Fayvad Site Admin'
admin.site.site_header = 'Fayvad Administration'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('manage/transport/', views.ManageTransport.as_view(), name='transport'),
    path('manage/common/', views.ManageCommon.as_view(), name='common'),
    path('manage/driving/',views.ManageDriving.as_view(), name='driving'),
    path('manage/rent/',views.ManageRent.as_view(), name='rent'),
    path('users/', include(profiles.urls, namespace='profiles')),
    path('transport/', include(transport.urls, namespace='transport')),
    path('common/', include(common.urls, namespace='common')),
    path('driving/', include(driving.urls, namespace='driving')),
    path('rent/', include(rent.urls, namespace='rent')),
    path('fm/', admin.site.urls),
    path('', include(accounts.urls, namespace='accounts')),
]
#urlspatterns += crud_for_app('transport')

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
