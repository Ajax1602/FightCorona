# Generated by Django 3.0.4 on 2020-03-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicesandrequests', '0002_auto_20200326_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='district',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='servicesandrequests.District'),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='servicesandrequests.States'),
        ),
    ]
