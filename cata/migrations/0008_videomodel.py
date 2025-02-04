# Generated by Django 5.1.4 on 2025-01-06 17:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cata', '0007_article_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videomodel',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('video_file', models.FileField(max_length=300, upload_to='media/videos')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='cata.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
