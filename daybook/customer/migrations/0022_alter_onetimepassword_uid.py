# Generated by Django 4.1.8 on 2023-04-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_alter_onetimepassword_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='uid',
            field=models.CharField(blank=True, default='<function uuid4 at 0x000002065E181FC0>', max_length=200, null=True),
        ),
    ]
