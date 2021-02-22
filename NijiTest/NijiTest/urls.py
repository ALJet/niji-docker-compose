"""NijiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, re_path, include
from niji import urls as niji_urls
from django.conf.urls.static import  static
from django.conf import settings
from niji import views



urlpatterns = [
    re_path(r'', include(niji_urls, namespace="niji")),
    # path('testurl', include(niji_urls)),
    path('admin/', admin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
]

#设置上传图片的路径 而且添加了图片资源展示 #
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#百度富文本添加静态路径才能显示图片
if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR,settings.MEDIA_ROOT)

    urlpatterns += static(settings.MEDIA_URL,document_root=media_root)


handler404 = views.page_not_found
handler500 = views.page500

