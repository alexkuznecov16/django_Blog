# Generated by Django 5.0.6 on 2024-05-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_postitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
