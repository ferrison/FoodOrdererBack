# Generated by Django 3.2.9 on 2021-12-03 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_food_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.food'),
        ),
    ]
