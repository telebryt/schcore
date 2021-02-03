# Generated by Django 3.1.6 on 2021-02-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='Faculty',
            field=models.CharField(choices=[('General', 'General'), ('FOE', 'FOE'), ('FAD', 'FAD'), ('BUS', 'BUS'), ('FOST', 'FOST')], default='Published', max_length=250),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='Status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='University', max_length=50),
        ),
    ]
