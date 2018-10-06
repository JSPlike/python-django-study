from django.contrib import admin

from blog.models import Blog
# Register your models here.

#admin 사이트에 보일 칼럼 목록 정의
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'url')


# admin 사이트에 두 클래스 등록
admin.site.register(Blog, BlogAdmin)
		