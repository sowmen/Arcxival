# Generated by Django 2.2.3 on 2019-07-07 23:24

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
            name='course',
            fields=[
                ('course_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=100)),
                ('course_credit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('teacher_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('batch', models.CharField(max_length=4)),
                ('session_id', models.CharField(default='default-session', max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('running', models.BooleanField(default=True)),
                ('course_code', models.ForeignKey(default='def_cor', on_delete=django.db.models.deletion.SET_DEFAULT, to='teacher.course')),
                ('teacher_code', models.ForeignKey(default='notea', on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_code',
            field=models.ForeignKey(default='NoTea', on_delete=django.db.models.deletion.SET_DEFAULT, to='teacher.teacher'),
        ),
    ]
