from django.shortcuts import render

# 페이지의 어떤 기능을 만들어 주는 곳
# URLS . py 에 내가 뷰스에 만든 기능이 어떤 url로 접속했을때 동작하게 할 것인지 설정.

# Create your views here.

from django.views.generic.base import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

from django.views.generic.list import ListView
from .models import Bookmark
class BookmarkListView(ListView):
    model = Bookmark
