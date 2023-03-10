# Generated by Django 4.1.7 on 2023-03-09 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link to original source')),
                ('agent_name', models.CharField(max_length=150, null=True, verbose_name='Agent Name')),
                ('agent_whats_up', models.URLField(null=True, verbose_name='Agent Whats App')),
                ('bedroom', models.CharField(max_length=5, verbose_name='No. of bedrooms')),
                ('amenities', models.CharField(blank=True, choices=[('Kitchen', 'Kitchen'), ('AC', 'AC'), ('Private pool', 'Private pool'), ('Shared pool', 'Shared pool'), ('Wi-Fi', 'Wi-Fi'), ('Shower', 'Shower'), ('Bathtub', 'Bathtub'), ('Cleaning service', 'Cleaning service'), ('TV', 'TV'), ('Parking area', 'Parking area')], max_length=244, null=True, verbose_name='Amenities')),
                ('rent_term', models.CharField(blank=True, choices=[('DAY', 'DAY'), ('MONTH', 'MONTH'), ('YEAR', 'YEAR')], max_length=5, null=True, verbose_name='Rental term')),
                ('image', models.ImageField(upload_to='')),
                ('price_rup', models.IntegerField(null=True, verbose_name='Price in Rupee')),
                ('price_usd', models.IntegerField(null=True, verbose_name='Price in USD')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Location Name')),
            ],
        ),
        migrations.CreateModel(
            name='RentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Surname')),
                ('username', models.CharField(max_length=150, null=True, verbose_name='Telegram Username')),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='Telegram ID')),
                ('register', models.DateTimeField(verbose_name='Date Registration')),
                ('last_activity', models.DateTimeField(verbose_name='Last Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_a', models.CharField(max_length=155, verbose_name='Type of appeal')),
                ('text', models.TextField()),
                ('answer', models.TextField(null=True)),
                ('appart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appart.apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appart.rentuser')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appart.location', verbose_name='Location'),
        ),
    ]