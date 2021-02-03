# Generated by Django 2.2.18 on 2021-02-03 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0005_auto_20210224_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='Faculty',
            field=models.CharField(choices=[('FOE', 'FOE'), ('FAD', 'FAD'), ('BUS', 'BUS'), ('FOST', 'FOST'), ('General', 'General')], default='General', max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='faculty',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
