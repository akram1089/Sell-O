# Generated by Django 4.1.4 on 2023-01-28 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_admin_login_sys_admin_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to='P_images'),
        ),
    ]
