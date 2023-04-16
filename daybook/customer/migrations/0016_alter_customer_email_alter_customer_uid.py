# Generated by Django 4.1.8 on 2023-04-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_alter_customer_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001C049381FC0>', max_length=200),
        ),
    ]
