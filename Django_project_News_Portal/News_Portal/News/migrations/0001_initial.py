# Generated by Django 4.2.4 on 2023-09-15 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255)),
                ('author_surname', models.CharField(max_length=255)),
                ('article_topic', models.CharField(max_length=255)),
                ('article_title', models.CharField(max_length=255)),
                ('autor_rating', models.SmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_of_articles', models.CharField(choices=[('sprt', 'Sports'), ('pltc', 'Politics'), ('educ', 'Education'), ('mrkt', 'Markets'), ('ecms', 'Economics'), ('tech', 'Technology'), ('wlth', 'Wealth'), ('news', 'Breaking news')], default='news', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreations', models.DateTimeField(auto_now_add=True)),
                ('article_title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrougt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.category')),
                ('postThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='News.PostCategory', to='News.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0)),
                ('comment_text', models.CharField(max_length=100)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('comment_rating', models.IntegerField()),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]