"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from bookmark.views import BookmarkListView #index.view 에서 수정

urlpatterns = [
    # http://localhost:8000/admin
    # 2차 url로 라우팅을 해준다. (앱에게 토스해준다, 기능을 동작시키지 않고 앱에게 던져준다)
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('admin/', admin.site.urls),
    path('', BookmarkListView.as_view(), name='index'),
]
