from django.urls import path, re_path
from .views import BookmarkListView


app_name = 'bookmark'
urlpatterns = [
    # http://localhost:8000/bookmark
    # 2차 url로 라우팅을 해준다. (앱에게 토스해준다, 기능을 동작시키지 않고 앱에게 던져준다)
    path('', BookmarkListView.as_view(), name='index' ),
#    path('', IndexPage.as_view(), name='index'),
]
