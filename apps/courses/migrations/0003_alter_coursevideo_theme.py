# Generated by Django 4.1.1 on 2022-10-22 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_subject_class_subject_alter_coursevideo_theme_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_themes', to='courses.theme'),
        ),
    ]
