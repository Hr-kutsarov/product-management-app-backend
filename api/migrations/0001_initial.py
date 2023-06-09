# Generated by Django 4.1.7 on 2023-03-18 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('contacts', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/images')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.store')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.section')),
            ],
        ),
    ]
