# Generated by Django 3.1.4 on 2020-12-23 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.optionsize'),
        ),
    ]
