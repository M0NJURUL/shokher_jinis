# Generated by Django 4.1.7 on 2023-03-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(null=True)),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
