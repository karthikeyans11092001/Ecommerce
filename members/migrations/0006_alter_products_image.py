# Generated by Django 4.2.1 on 2023-06-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
