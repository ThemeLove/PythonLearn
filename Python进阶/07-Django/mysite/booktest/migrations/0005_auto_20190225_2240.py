# Generated by Django 2.1.7 on 2019-02-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_areainfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bcomment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='heroinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
