from __future__ import unicode_literals #python 2.x 지원

from django.db import models

# python 2.x에 python 3.x 버전의 문자열을 지원 하도록 도와주는 모듈
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible #python 2.x 지원

# Blog모델(테이블)정의
class Blog(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True) #타이틀 칼럼
	url = models.URLField('url', unique=True) #url 칼럼

	#python3 문법이며 객체를 문자열로 표현할 때 사용하는 함수
	#Admin사이트나 장고 셸등에서는 테이블 명을 보여주어야 하는데 이때, __str__() 함수를
	#사용하지 않으면 테이블명이 제대로 표기되지 않는다. 
	def __str__(self):
		return self.title

