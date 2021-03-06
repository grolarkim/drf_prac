# Generated by Django 4.0.5 on 2022-06-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, null=True, verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name='생일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='realname',
            field=models.CharField(max_length=50, null=True, verbose_name='이름'),
        ),
    ]
