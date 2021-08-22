# Generated by Django 3.0.11 on 2021-08-22 14:29

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
            name='HouseSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'house_sizes',
            },
        ),
        migrations.CreateModel(
            name='HouseStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'house_styles',
            },
        ),
        migrations.CreateModel(
            name='HousingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'housing_types',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('house_size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.HouseSize')),
                ('house_style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.HouseStyle')),
                ('housing_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.HousingType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'spaces',
            },
        ),
        migrations.CreateModel(
            name='PostBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=256)),
                ('content', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Post')),
                ('space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Space')),
            ],
            options={
                'db_table': 'post_blocks',
            },
        ),
    ]
