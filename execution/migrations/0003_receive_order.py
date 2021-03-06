# Generated by Django 3.1.2 on 2021-04-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0002_flower_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receive_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('address_2', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=20)),
            ],
        ),
    ]
