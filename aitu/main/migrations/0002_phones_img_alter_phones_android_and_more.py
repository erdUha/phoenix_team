# Generated by Django 4.2 on 2023-04-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='img',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='android',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='bad_cost',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='battery',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='color',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='cores',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='cost',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='cpu',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='cpu_frequency',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='frequency',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='front_camera',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='glass',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='main_camera',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='matrix_type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='max_brightness',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='ram',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='screen_dimensions',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='screen_size',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='sim_type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='sims',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='storage',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='video',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='phones',
            name='warranty',
            field=models.CharField(default='', max_length=255),
        ),
    ]
