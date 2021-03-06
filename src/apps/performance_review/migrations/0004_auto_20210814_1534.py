# Generated by Django 3.2.5 on 2021-08-14 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance_review', '0003_auto_20210709_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criteria',
            options={'ordering': ('id',), 'verbose_name': 'Criteria', 'verbose_name_plural': 'Criterias'},
        ),
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ('id',), 'verbose_name': 'Goal', 'verbose_name_plural': 'Goals'},
        ),
        migrations.AlterModelOptions(
            name='performancereview',
            options={'ordering': ('-year',), 'verbose_name': 'Performance Review', 'verbose_name_plural': 'Performance Reviews'},
        ),
    ]
