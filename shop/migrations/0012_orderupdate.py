# Generated by Django 3.2.9 on 2023-05-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_dateadded'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('updateId', models.AutoField(primary_key=True, serialize=False)),
                ('orderId', models.IntegerField(default='')),
                ('updateDesc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
