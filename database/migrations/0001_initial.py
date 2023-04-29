# Generated by Django 4.2 on 2023-04-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(default='Bengaluru', max_length=100)),
                ('state', models.CharField(default='Karnataka', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PayingGuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(default='Bengaluru', max_length=100)),
                ('state', models.CharField(default='Karnataka', max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.category')),
                ('college', models.ManyToManyField(blank=True, to='database.college')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.division')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.division'),
        ),
    ]