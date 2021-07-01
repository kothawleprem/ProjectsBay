# Generated by Django 3.2.4 on 2021-07-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('age', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('profession', models.CharField(max_length=200, null=True)),
                ('organization', models.CharField(max_length=200, null=True)),
                ('ctag', models.CharField(max_length=200, null=True)),
                ('portfolio', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('created', models.CharField(max_length=200, null=True)),
                ('completed', models.CharField(max_length=200, null=True)),
                ('achievements', models.CharField(max_length=200, null=True)),
                ('tech', models.CharField(max_length=200, null=True)),
                ('github', models.CharField(max_length=200, null=True)),
                ('live', models.CharField(max_length=200, null=True)),
                ('opf1', models.CharField(max_length=200, null=True)),
                ('opfl1', models.CharField(max_length=200, null=True)),
                ('opf2', models.CharField(max_length=200, null=True)),
                ('opfl2', models.CharField(max_length=200, null=True)),
                ('opf3', models.CharField(max_length=200, null=True)),
                ('opfl3', models.CharField(max_length=200, null=True)),
                ('opf4', models.CharField(max_length=200, null=True)),
                ('opfl4', models.CharField(max_length=200, null=True)),
                ('imgl', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
