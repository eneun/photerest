# Generated by Django 2.2.3 on 2019-08-13 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190813_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/static/account/images/basic-profile-img.png', upload_to='images/profile'),
        ),
    ]