# Generated by Django 3.1.2 on 2020-10-30 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20201029_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cat',
            name='color_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Color', to='cats.color'),
        ),
        migrations.AlterField(
            model_name='hunting',
            name='cat_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cat', to='cats.cat'),
        ),
        migrations.AlterField(
            model_name='hunting',
            name='prey_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Prey', to='cats.prey'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='usr',
            name='cat1_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cat1', to='cats.cat'),
        ),
        migrations.AddField(
            model_name='usr',
            name='cat2_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cat2', to='cats.cat'),
        ),
        migrations.AddField(
            model_name='usr',
            name='cat3_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cat3', to='cats.cat'),
        ),
        migrations.AddField(
            model_name='usr',
            name='cat4_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Cat4', to='cats.cat'),
        ),
    ]