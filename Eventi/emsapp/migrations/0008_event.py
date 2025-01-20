# Generated by Django 5.1.4 on 2025-01-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0007_rename_usersubmission_ticketform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Concerts', 'Concerts'), ('Sports', 'Sports'), ('Workshop', 'Workshop'), ('Community', 'Community Events')], max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image1', models.ImageField(upload_to='events/')),
                ('image2', models.ImageField(upload_to='events/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
