# Generated by Django 3.2 on 2021-04-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetcategory',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='budget',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]