
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

admin.site.site_title = 'Saboten HighLow Set ユーザー管理サイト'
admin.site.site_header = 'Saboten HighLow Set ユーザー管理サイト'
admin.site.index_title = 'メニュー'
admin.site.unregister(Group)

urlpatterns = [
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('reviewpost.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)