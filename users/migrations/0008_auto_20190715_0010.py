# Generated by Django 2.1.7 on 2019-07-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190715_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='testkits',
            field=models.ManyToManyField(blank=True, null=True, related_name='testkits', to='testkit.TestKit'),
        ),
    ]
