# Generated by Django 4.1.4 on 2023-01-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_login_sys_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_sys',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_pics'),
        ),
    ]
