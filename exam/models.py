from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Papers(models.Model):
    paper_title = models.CharField('标题', max_length=30)
    subject = models.CharField('主题', max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    paper_score = models.IntegerField('分数', default=0)

    

    class Meta:
        db_table = 'Papers'
        verbose_name = ("卷子")
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.paper_title

    
    def get_absolute_url(self):
        return reverse("set_questions")



class Question(models.Model):
    paper_title = models.ForeignKey(Papers, on_delete=models.CASCADE)
    title = models.TextField('题目')
    answer = models.TextField('答案', blank=True)
    right_answer = models.TextField('答案')
    score = models.IntegerField('分数', default=1)

    class Meta:
        db_table = 'question'
        verbose_name = ("题目")
        verbose_name_plural = verbose_name
        ordering = ['id']



    def get_absolute_url(self):
        return reverse("result", kwargs={"pk": self.pk})


