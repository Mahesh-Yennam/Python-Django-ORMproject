# Generated by Django 4.0.5 on 2022-08-05 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0004_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education2',
            fields=[
                ('emp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ormapp.emp')),
                ('ssc', models.IntegerField()),
                ('hsc', models.IntegerField()),
                ('grad', models.IntegerField()),
            ],
            bases=('ormapp.emp',),
        ),
    ]