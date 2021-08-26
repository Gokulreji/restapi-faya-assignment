# Generated by Django 2.2 on 2021-08-26 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imageUrl', models.URLField()),
                ('status', models.BooleanField()),
                ('date_added', models.DateField()),
                ('created', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='restapi.Register')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
