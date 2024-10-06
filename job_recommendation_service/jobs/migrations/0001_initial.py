# Generated by Django 5.1 on 2024-10-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('required_skills', models.JSONField()),
                ('location', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract')], max_length=50)),
                ('experience_level', models.CharField(choices=[('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Senior', 'Senior')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('skills', models.JSONField()),
                ('experience_level', models.CharField(choices=[('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Senior', 'Senior')], max_length=50)),
                ('preferences', models.JSONField()),
            ],
        ),
    ]
