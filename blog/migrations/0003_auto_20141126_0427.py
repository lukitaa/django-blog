# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('text', models.TextField(help_text='The text of the comment.')),
                ('created', models.DateField(help_text='Creation date of the comment.', auto_now_add=True)),
                ('commenter', models.CharField(max_length=50, help_text='Author of the comment.')),
                ('article', models.ForeignKey(to='blog.Article')),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(help_text='Creation date of the article.', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modified',
            field=models.DateField(auto_now=True, help_text='Modification date of the article.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(help_text='The text of the article (in Markdown).'),
            preserve_default=True,
        ),
    ]
