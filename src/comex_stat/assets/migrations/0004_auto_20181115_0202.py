# Generated by Django 2.1.2 on 2018-11-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20181115_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncm',
            name='ncm_name_en',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ncm',
            name='ncm_name_es',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ncm',
            name='ncm_name_pt',
            field=models.TextField(),
        ),
    ]