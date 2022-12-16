# Generated by Django 4.0.6 on 2022-12-16 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.device')),
                ('mqtt_topic', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('humidity', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('pressure', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('air_quality', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            bases=('backend.device',),
        ),
        migrations.AlterModelOptions(
            name='switch',
            options={'verbose_name_plural': 'Switches'},
        ),
    ]
