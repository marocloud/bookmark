from django.db import models

# 모델, 뷰, url 이 한 쌍
# 데이터베이스에 어떤 데이터를 어떻게 저장할 것인가?
# O.R.M. : 오브젝트 릴레이티드 매핑 - 객체와 대응되는 데이터베이스 매핑 관리

# Create your models here.

# 데이터베이스 한 테이블을 하나의 클래스(모델)로 묘사한다. 모델을 클래스로 구현한다.
# models -> views -> urs -> templates

class Bookmark(models.Model):
    # 하나의 필드를 만든다.
    # 컬럼 이름 = 컬럼 종류(제약 조건)
    site_name = models.CharField(max_length=100)
    url = models.URLField('url') # vervose name

    # 모델의 옵션
    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return self.site_name
