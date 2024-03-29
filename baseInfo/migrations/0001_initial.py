# Generated by Django 2.0.7 on 2019-02-18 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('is_maride', models.BooleanField()),
                ('id_number', models.CharField(max_length=50)),
                ('bank_account', models.CharField(max_length=26)),
                ('insurance_id', models.CharField(max_length=8)),
                ('description', models.TextField(blank=True, null=True)),
                ('add_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
