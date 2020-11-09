# Generated by Django 3.0.6 on 2020-11-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id'], 'verbose_name': '题目', 'verbose_name_plural': '题目'},
        ),
        migrations.AddField(
            model_name='papers',
            name='paper_score',
            field=models.IntegerField(default=0, verbose_name='分数'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, verbose_name='答案'),
        ),
    ]
