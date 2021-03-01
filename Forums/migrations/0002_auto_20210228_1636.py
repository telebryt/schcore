# Generated by Django 3.0.6 on 2021-02-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='Faculty',
            field=models.CharField(choices=[('BUS', 'BUS'), ('FOST', 'FOST'), ('General', 'General'), ('FAD', 'FAD'), ('FOE', 'FOE')], default='General', max_length=250),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='Status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='Published', max_length=50),
        ),
    ]
