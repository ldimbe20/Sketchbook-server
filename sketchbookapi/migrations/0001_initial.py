# Generated by Django 4.0.3 on 2022-03-24 15:26

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
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MediumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sketchbookapi.medium')),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('image_url', models.ImageField(null=True, upload_to='actionimages')),
                ('notes', models.CharField(max_length=1000)),
                ('private', models.BooleanField()),
                ('mediums_used', models.ManyToManyField(related_name='mediums_used', through='sketchbookapi.MediumPost', to='sketchbookapi.medium')),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_mood', to='sketchbookapi.mood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_artist', to='sketchbookapi.artist')),
            ],
        ),
        migrations.AddField(
            model_name='mediumpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sketchbookapi.post'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='sketchbookapi.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_artist', to='sketchbookapi.artist')),
            ],
        ),
    ]
