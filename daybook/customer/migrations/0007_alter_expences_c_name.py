# Generated by Django 4.2 on 2023-04-14 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_expences_c_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expences',
            name='c_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
