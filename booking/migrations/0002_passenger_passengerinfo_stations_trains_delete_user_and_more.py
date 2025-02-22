# Generated by Django 4.2.7 on 2023-11-15 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'Passenger',
            },
        ),
        migrations.CreateModel(
            name='PassengerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('berth', models.CharField(choices=[('1AC', '1AC'), ('2AC', '2AC'), ('3AC', '3AC'), ('2AS', '2AS')], max_length=10)),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.passenger')),
            ],
            options={
                'db_table': 'PassengerInfo',
            },
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('station_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('station_code', models.CharField(max_length=10)),
                ('station_location', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Stations',
            },
        ),
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=50)),
                ('train_number', models.IntegerField()),
                ('dep_time', models.TimeField()),
                ('arv_time', models.TimeField()),
                ('run_days', models.CharField(max_length=50)),
                ('seats_avl', models.CharField(max_length=100)),
                ('seat_quotas', models.CharField(max_length=100)),
                ('seat_classes', models.CharField(max_length=50)),
                ('arv_station', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='booking.stations')),
                ('dep_station', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='booking.stations')),
            ],
            options={
                'db_table': 'Trains',
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='passenger',
            name='from_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='booking.stations'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='to_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='booking.stations'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='train_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='trainname', to='booking.trains'),
        ),
    ]
