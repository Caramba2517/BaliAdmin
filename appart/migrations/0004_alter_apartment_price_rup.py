# Generated by Django 4.1.7 on 2023-03-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appart', '0003_alter_apartment_price_usd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='price_rup',
            field=models.BigIntegerField(null=True, verbose_name='Price in Rupee'),
        ),
    ]