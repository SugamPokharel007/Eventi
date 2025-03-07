# Generated by Django 5.1.4 on 2024-12-31 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0003_usersubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='formsubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='dropdown_option',
            field=models.CharField(choices=[('workshop', 'Workshop'), ('concert', 'Concert'), ('sports', 'Sports Event'), ('community', 'Community Events')], max_length=50),
        ),
    ]
