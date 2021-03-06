# Generated by Django 2.1.7 on 2019-07-13 17:14

from django.db import migrations, models
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestKit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', model_utils.fields.StatusField(choices=[('available', 'available'), ('processing', 'processing'), ('complete', 'complete')], default='available', max_length=100, no_check_for_status=True)),
                ('invoice', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('results', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Test Kit',
                'verbose_name_plural': 'Test Kits',
            },
        ),
    ]
