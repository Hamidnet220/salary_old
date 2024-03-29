# Generated by Django 2.0.7 on 2019-02-18 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseInfo', '0006_auto_20190218_1426'),
        ('wage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseInfo.Employee')),
                ('wage_sum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wage.WageSum')),
            ],
        ),
    ]
