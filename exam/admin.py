from django.contrib import admin
from .models import Question, Papers
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
	list_display = ['paper_title', 'id', 'title', ]
	search_fields = ['paper_title']


class PapersAdmin(admin.ModelAdmin):
	list_display = ['paper_title', 'id', 'subject', 'created_time']
	search_fields = ['paper_title']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Papers, PapersAdmin)  # 把文章模型注册到admin模块
