# Generated by Django 3.1.2 on 2020-10-29 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20201029_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Color', to='cats.color'),
        ),
    ]
