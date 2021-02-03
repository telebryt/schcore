# Generated by Django 3.1.6 on 2021-02-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0002_auto_20210224_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='Faculty',
            field=models.CharField(choices=[('FOE', 'FOE'), ('FAD', 'FAD'), ('BUS', 'BUS'), ('FOST', 'FOST'), ('General', 'General')], default='Published', max_length=250),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='Status',
            field=models.CharField(choices=[('published', 'published'), ('draft', 'draft')], default='University', max_length=50),
        ),
    ]