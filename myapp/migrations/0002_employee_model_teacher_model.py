# Generated by Django 4.2.7 on 2023-12-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100, null=True)),
                ('Last_Name', models.CharField(max_length=100)),
                ('DepartMent_Name', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100, null=True)),
                ('Last_Name', models.CharField(max_length=100)),
                ('DepartMent_Name', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
    ]