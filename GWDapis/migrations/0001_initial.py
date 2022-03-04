# Generated by Django 2.2 on 2022-03-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GW_General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WellNo', models.CharField(max_length=10)),
                ('Well_Type', models.CharField(max_length=18)),
                ('Agency', models.CharField(max_length=5)),
                ('State', models.CharField(max_length=9)),
                ('District', models.CharField(max_length=23)),
                ('Block_Taluk', models.CharField(max_length=20)),
                ('GP_Mandal', models.CharField(max_length=25)),
                ('Village', models.CharField(max_length=25)),
                ('Basin', models.CharField(max_length=8)),
                ('Minor_Basin', models.CharField(max_length=15)),
                ('Geology', models.CharField(max_length=28)),
                ('Geomorphology', models.CharField(max_length=19)),
                ('Toposheet_No', models.CharField(max_length=5)),
                ('LatD', models.CharField(max_length=2)),
                ('LatM', models.CharField(max_length=2)),
                ('LatS', models.CharField(max_length=4)),
                ('LonD', models.CharField(max_length=2)),
                ('LonM', models.CharField(max_length=2)),
                ('LonS', models.CharField(max_length=4)),
                ('Easting', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Northing', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Method', models.CharField(max_length=9)),
                ('Command_Area', models.CharField(max_length=5)),
                ('MP', models.CharField(max_length=1)),
                ('DWLR_installed', models.CharField(max_length=5)),
                ('dwlr_no', models.CharField(max_length=8)),
                ('DWLR_type', models.CharField(max_length=1)),
                ('Category', models.CharField(max_length=10)),
                ('Select', models.CharField(max_length=5)),
                ('Filter', models.CharField(max_length=4)),
                ('Repl', models.CharField(max_length=5)),
                ('Urban', models.CharField(max_length=5)),
            ],
        ),
    ]
